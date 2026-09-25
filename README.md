# ProxyRules

个人代理与分流规则集合 (Stash / Clash Rule-Providers)。

## 规则列表

### 1. 抖音与字节跳动全量规则 (`Douyin.yaml`)
基于真实抓包与业务实践分析，涵盖抖音主站、短视频点播切片（VOD）、直播拉流（FLV）、图床、对象存储（TOS）、前端公共基建（Goofy/Gecko）与相关字节产品线（西瓜/火山/头条）。

#### 在 Stash 中引用配置示例：

```yaml
rule-providers:
  douyin:
    type: http
    behavior: classical
    format: yaml
    # GitHub Raw 链接
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Douyin.yaml"
    # 国内加速镜像备用（如遇连接超时可选用）:
    # url: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Douyin.yaml"
    path: ./ruleset/douyin.yaml
    interval: 86400

rules:
  - RULE-SET,douyin,DIRECT
```
