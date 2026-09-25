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

### 4. 全球综合与专业前沿新闻规则 (`News.yaml`)
基于真实 Chrome 浏览器历史记录全量深度分析（8万+记录），系统梳理并涵盖：
* **全球综合大报与通讯社**：纽约时报、华尔街日报、英国卫报、泰晤士报、每日电讯报、洛杉矶时报、法兰克福汇报、世界报、时代周报、费加罗报、读卖新闻、东亚日报、美联社、CNN、CBS、NBC、德国之声、法国国际广播、联合国新闻等。
* **数字报刊与聚合平台**：PressReader（全球报刊亭旗舰）。
* **深度财经与宏观经济**：金融时报、道琼斯、彭博法律、CNBC、第一财经、上海证券报、国际商报、中国银行保险报、投资界、创业邦、NBER（美国国家经济研究所）、AEA（美国经济学会）等。
* **科技前沿与数码媒体**：Ars Technica、Wired、VentureBeat、TNW、钛媒体、The Register、9to5Mac、Android Authority、Notebookcheck、Chrome Unboxed、Electrek、The Quantum Insider、SpaceNews 等。
* **影视娱乐与流行文化**：Deadline Hollywood、Collider、Vulture、The A.V. Club、Dexerto、Rolling Stone、Top Gear、Consumer Reports、Pocketmags 等。
* **垂直专业与细分行业新闻**：科学美国人、Science/ScienceInsider、Nature News、STAT News（生物医药）、Medscape（临床医学）、C&EN（化学工程）、USNI News（海军防务）、The War Zone（军事实战前沿）、Food Dive（食品制造工业）、Courthouse News（全美司法法庭）、Times Higher Education 等。
* **华语海外报刊与区域媒体**：联合早报、世界日报、人民报、大纪元、文学城、香港01、香港商报、紫荆网、台湾风传媒、台湾INSIDE、马来西亚南洋商报、新加坡商业时报、泰国民族报、泰国Prachachat、韩国亚洲经济、韩国每日经济、日本经济新闻/日经中文网、印度经济时报等。
* **国内权威与行业专业报纸**：人民日报数字报、新华每日电讯、中国日报、央广网、解放日报/上观新闻、新京报数字报、南方日报数字报、科技日报、人民法院报、法治日报、中国警察网/人民公安报、中国知识产权报、中国组织人事报、中国煤炭报等。
* **使用策略**：`PROXY` 或专用的 `新闻资讯` / `媒体` 策略组。

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

  # 4. 订阅全球新闻与专业媒体规则集
  news:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/News.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/News.yaml"
    path: ./ruleset/news.yaml
    interval: 86400

rules:
  # 必须排在最前面：优先阻断所有 P2P 偷跑连接
  - RULE-SET,pcdn-block,REJECT

  # 抖音官方核心业务直连
  - RULE-SET,douyin,DIRECT

  # YouTube 流量走代理或指定策略组
  - RULE-SET,youtube,PROXY

  # 全球与专业新闻媒体走代理（或指定 [News] 策略组）
  - RULE-SET,news,PROXY

  # 后续其他分流规则
  - DOMAIN-SUFFIX,google.com,PROXY
  - GEOIP,CN,DIRECT
  - MATCH,FINAL
```
