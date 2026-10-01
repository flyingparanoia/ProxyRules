#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Build script to compile Clash YAML rule-providers and external lists
into sing-box binary rule-sets (.srs) and source JSON (.json).
"""

import os
import sys
import glob
import yaml
import json
import shutil
import urllib.request
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(REPO_ROOT, "srs")

HAGEZI_LIGHT_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/light.txt"

def parse_yaml_payload(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        return None

    payload = data.get("payload", [])
    if not isinstance(payload, list):
        return None

    domain, domain_suffix, domain_keyword, ip_cidr = [], [], [], []

    for raw in payload:
        item = str(raw).strip()
        if not item or item.startswith("#"):
            continue

        if item.startswith("+."):
            domain_suffix.append(item[2:])
        elif item.startswith("."):
            domain_suffix.append(item[1:])
        elif item.startswith("DOMAIN-SUFFIX,"):
            domain_suffix.append(item.split(",", 1)[1].strip())
        elif item.startswith("DOMAIN-KEYWORD,"):
            domain_keyword.append(item.split(",", 1)[1].strip())
        elif item.startswith("DOMAIN,"):
            domain.append(item.split(",", 1)[1].strip())
        elif item.startswith("IP-CIDR,") or item.startswith("IP-CIDR6,"):
            ip_cidr.append(item.split(",", 1)[1].strip())
        else:
            # Plain domain name
            domain.append(item)

    r = {}
    if domain:
        r["domain"] = list(dict.fromkeys(domain))
    if domain_suffix:
        r["domain_suffix"] = list(dict.fromkeys(domain_suffix))
    if domain_keyword:
        r["domain_keyword"] = list(dict.fromkeys(domain_keyword))
    if ip_cidr:
        r["ip_cidr"] = list(dict.fromkeys(ip_cidr))

    return {
        "version": 2,
        "rules": [r] if r else []
    }

def compile_custom_rules():
    print("=== [1/2] Compiling Custom Clash YAML Rules ===")
    yaml_files = sorted(glob.glob(os.path.join(REPO_ROOT, "*.yaml")))
    success_count = 0

    for yf in yaml_files:
        base_name = os.path.splitext(os.path.basename(yf))[0]
        json_path = os.path.join(DIST_DIR, f"{base_name}.json")
        srs_path = os.path.join(DIST_DIR, f"{base_name}.srs")

        rule_data = parse_yaml_payload(yf)
        if rule_data is None:
            print(f"  [SKIP] {base_name}.yaml: no valid payload found")
            continue

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(rule_data, f, indent=2, ensure_ascii=False)

        cmd = ["sing-box", "rule-set", "compile", json_path, "-o", srs_path]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            size_kb = os.path.getsize(srs_path) / 1024
            print(f"  [OK] {base_name}.srs ({size_kb:.1f} KB)")
            success_count += 1
        else:
            print(f"  [ERR] {base_name}: {res.stderr.strip()}", file=sys.stderr)
            sys.exit(1)

    print(f"Successfully compiled {success_count} custom rule sets.\n")

def compile_external_rules():
    print("=== [2/2] Fetching and Compiling External Rules ===")
    # 1. HaGeZi Multi LIGHT
    hagezi_tmp = os.path.join(DIST_DIR, "hagezi_light_adblock_tmp.txt")
    hagezi_srs = os.path.join(DIST_DIR, "hagezi-light.srs")

    print(f"  Downloading HaGeZi Light from: {HAGEZI_LIGHT_URL} ...")
    req = urllib.request.Request(
        HAGEZI_LIGHT_URL,
        headers={"User-Agent": "Mozilla/5.0 (ProxyRules-Builder)"}
    )
    with urllib.request.urlopen(req) as resp, open(hagezi_tmp, "wb") as out_f:
        shutil.copyfileobj(resp, out_f)

    cmd = ["sing-box", "rule-set", "convert", "--type", "adguard", "--output", hagezi_srs, hagezi_tmp]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(hagezi_tmp):
        os.remove(hagezi_tmp)

    if res.returncode == 0:
        size_kb = os.path.getsize(hagezi_srs) / 1024
        print(f"  [OK] hagezi-light.srs ({size_kb:.1f} KB)")
    else:
        print(f"  [ERR] HaGeZi compile failed: {res.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    print("Successfully compiled external rule sets.\n")

def main():
    os.makedirs(DIST_DIR, exist_ok=True)
    compile_custom_rules()
    compile_external_rules()
    print("All rule sets compiled successfully into 'dist/' directory!")

if __name__ == "__main__":
    main()
