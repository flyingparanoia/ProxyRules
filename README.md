# ProxyRules

个人代理与分流规则集合 (Stash / Clash Rule-Providers)。

## 规则列表

### 1. YouTube 全量分流规则 (`YouTube.yaml`)
基于 Mac 桌面网页端 + iPhone 客户端双端实测抓包，涵盖 YouTube 主站、点播与直播流媒体 CDN (`googlevideo.com`)、移动端历史同步与进度心跳 (`s.youtube.com`)、移动端视频调度器 (`redirector.googlevideo.com`)、图床及各类子产品。
* **使用策略**：`Proxy` 或专用的流媒体策略组（如 `YouTube`）

### 2. 抖音与字节跳动官方规则 (`Douyin.yaml`)
涵盖抖音主站、短视频点播切片（VOD / zjcdn）、直播拉流（FLV）、图床、对象存储（TOS）、前端公共基建（Goofy/Gecko）与相关字节产品线（西瓜/火山/头条）。
* **使用策略**：`DIRECT`（直连）

### 3. PCDN / P2P 偷跑上行阻断规则 (`PCDN.yaml`)
专门收集国内主流视频/直播 App（抖音、B站、爱优腾等）偷偷利用用户设备上行充当免费 CDN 节点的 P2P 调度域名。
* **使用策略**：`REJECT`（拦截后 App 会自动降级走官方直连 CDN，视频顺畅播放且手机不再发烫偷跑上传）

---

## 在 Stash 中的标准配置示例

```yaml
rule-providers:
  # 1. 订阅 PCDN 偷跑拦截规则集
  pcdn-block:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/PCDN.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/PCDN.yaml"
    path: ./ruleset/pcdn-block.yaml
    interval: 86400

  # 2. 订阅抖音官方直连规则集
  douyin:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Douyin.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Douyin.yaml"
    path: ./ruleset/douyin.yaml
    interval: 86400

  # 3. 订阅 YouTube 规则集
  youtube:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/YouTube.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/YouTube.yaml"
    path: ./ruleset/youtube.yaml
    interval: 86400

rules:
  # 必须排在最前面：优先阻断所有 P2P 偷跑连接
  - RULE-SET,pcdn-block,REJECT

  # 抖音官方核心业务直连
  - RULE-SET,douyin,DIRECT

  # YouTube 流量走代理或指定策略组
  - RULE-SET,youtube,PROXY

  # 后续其他分流规则
  - DOMAIN-SUFFIX,google.com,PROXY
  - GEOIP,CN,DIRECT
  - MATCH,FINAL
```
