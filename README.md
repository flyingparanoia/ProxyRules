# ProxyRules

个人代理与分流规则集合 (Stash / Clash Rule-Providers)。

## 规则列表

### 1. YouTube 全量分流规则 (`YouTube.yaml`)
基于 Mac 桌面网页端 + iPhone 客户端双端实测抓包，涵盖 YouTube 主站、点播与直播流媒体 CDN (`googlevideo.com`)、移动端历史同步与进度心跳 (`s.youtube.com`)、移动端视频调度器 (`redirector.googlevideo.com`)、图床及各类子产品。
* **使用策略**：`Proxy` 或专用的流媒体策略组（如 `YouTube`）

### 2. 抖音与字节跳动官方规则 (`Douyin.yaml`)
涵盖抖音主站、短视频点播切片（VOD / zjcdn）、直播拉流（FLV）、图床、对象存储（TOS）、前端公共基建（Goofy/Gecko）与相关字节产品线（西瓜/火山/头条）。
* **使用策略**：`DIRECT`（直连）

### 3. 大陆视频网站与 App PCDN 偷跑阻断规则 (`China-Video-Apps-PCDN.yaml`)
专门收集国内主流视频/直播 App（抖音、B站、爱优腾等）偷偷利用用户设备上行充当免费 CDN 节点的 P2P 调度域名。
* **使用策略**：`REJECT`（拦截后 App 会自动降级走官方直连 CDN，视频顺畅播放且手机不再发烫偷跑上传）

### 4. 全球海外综合与专业前沿新闻规则 (`Foreign-News.yaml`)
基于真实 Chrome 浏览器历史记录全量深度分析（8万+记录），专门剔除了中国大陆境内媒体，专为科学上网分流与海外优质资讯代理设计。涵盖：
* **全球综合大报与通讯社**：纽约时报、华尔街日报、英国卫报、泰晤士报、每日电讯报、洛杉矶时报、法兰克福汇报、世界报、时代周报、费加罗报、读卖新闻、东亚日报、美联社、CNN、CBS、NBC、德国之声、法国国际广播、联合国新闻等。
* **数字报刊与聚合平台**：PressReader（全球报刊亭旗舰，高频阅读数千次）。
* **深度财经与宏观经济**：金融时报、道琼斯、彭博法律、CNBC、香港瑞恩资本、香港经济通、NBER（美国国家经济研究所）、AEA（美国经济学会）等。
* **科技前沿与数码媒体**：Ars Technica、Wired、VentureBeat、TNW、The Register、9to5Mac、Android Authority、Notebookcheck、Chrome Unboxed、Electrek、The Quantum Insider、SpaceNews 等。
* **影视娱乐与流行文化**：Deadline Hollywood、Collider、Vulture、The A.V. Club、Dexerto、Rolling Stone、Top Gear、Consumer Reports、Pocketmags 等。
* **垂直专业与细分行业新闻**：科学美国人、Science/ScienceInsider、Nature News、STAT News（生物医药）、Medscape（临床医学）、C&EN（化学工程）、USNI News（海军防务）、The War Zone（军事实战前沿）、Food Dive（食品制造工业）、Courthouse News（全美司法法庭）、Times Higher Education 等。
* **华语海外报刊与港澳台及亚洲重点**：联合早报、世界日报、人民报、大纪元、文学城、香港01、香港商报、紫荆网、台湾风传媒、台湾INSIDE、马来西亚南洋商报、新加坡商业时报、泰国民族报、泰国Prachachat、韩国亚洲经济、韩国每日经济、日本经济新闻/日经中文网、印度经济时报等。
* **使用策略**：`PROXY` 或专用的 `Foreign-News` / `媒体` 策略组。

### 5. OpenAI / ChatGPT 全量生态分流规则 (`OpenAI.yaml`)
结合 `mixed.yaml` 与 `MESL+tempjms-apple.yaml` 深度提取与合并，涵盖：
* **OpenAI 核心主站**：`openai.com`、`chatgpt.com`、`sora.com`、`ai.com`、`oaistatic.com`、`oaiusercontent.com`。
* **反代与专属 CDN 网关**：Azure Front Door / Edge (`azurefd.net`, `azureedge.net`)、Cloudflare 边缘反代节点、Imgix。
* **人机风控与认证授权**：Arkose Labs 人机验证 (`arkoselabs.com`)、Persona 实名风控 (`inquiry.withpersona.com`)、Auth0。
* **实时语音高级模式 WebRTC**：LiveKit 核心音视频中继 (`chatgpt.livekit.cloud`, `turn.livekit.cloud`, `host.livekit.cloud`)。
* **实验灰度与监控遥测**：Statsig (`statsigapi.net`)、Datadog (`browser-intake-datadoghq.com`)、Sentry、LaunchDarkly。
* **插件生态与支付**：Stripe 信用卡充值网关 (`api.stripe.com`)、插件市场、OneDrive 与 Mapbox 集成。
* **拓展主流 AI**：Claude / Anthropic、Grok、Perplexity、Cursor、OpenRouter。
* **使用策略**：`PROXY` 或专用的 `OpenAI` / `AI` 策略组。

### 6. Google 全球搜索与 Gemini 智能生态规则 (`GoogleSearch-Gemini.yaml`)
结合 `mixed.yaml`（Google-Search 精细优化 + Gemini 会话锁）与 `MESL+tempjms-apple.yaml`（全球各地区顶级域名与搜索基建），涵盖：
* **搜索主域与短链**：`google.com`、`g.co`、`goo.gl`、`466453.com`、`toolbarqueries.google.com`。
* **Google Gemini / AI 全量生态**：`gemini.google.com`、`bard.google.com`、`aistudio.google.com`、`makersuite.google.com`、`ai.google`、`ai.google.dev`、`generativelanguage.googleapis.com`（模型 API）、`proactivebackend-pa.googleapis.com`、`alkalicore-pa.clients6.google.com`、`deepmind.google`、`deepmind.com`。
* **全球各国家/地区顶级域名 (ccTLD)**：`google.com.hk`、`google.co.jp`、`google.com.tw`、`google.co.uk`、`google.de`、`google.ca` 等 40+ 主流国家搜索后缀。
* **静态多媒体与字体**：`gstatic.com`、`ssl.gstatic.com`、`fonts.gstatic.com`、`fonts.googleapis.com`、`googleusercontent.com`、`1e100.net`。
* **统一身份与核心服务**：`accounts.google.com`、`ogs.google.com`（九宫格组件）、`googleapis.com`、`clients6.google.com`、`maps.googleapis.com`。
* **安全验证与证书**：reCAPTCHA (`recaptcha.net`)、Google PKI 证书体系 (`pki.goog`, `o.pki.goog`)、安全浏览。
* **移动加速标准 (AMP)**：`ampproject.org`、`ampproject.net`、`amp.dev`、`schema.org`。
* **推送服务与防会话撕裂**：FCM / MTalk (`mtalk.google.com`)、Google Public DNS (`dns.google`)、IPv6 规则。
* **设计优势**：将 Google 搜索与 Gemini 统一绑定走同一代理出口，彻底解决跨应用不同出口引发的 Google 账号异地风控与 Gemini 区域阻断。
* **使用策略**：`PROXY` 或专用的 `Google` / `Google-Gemini` 策略组。

### 7. 英国主流流媒体与全媒体规则 (`UK-Media.yaml`)
结合 `mixed.yaml`（UK Broadcast）与 `MESL+tempjms-apple.yaml`（BBC 全量 Akamai/Limelight 播流 CDN 矩阵），涵盖：
* **BBC 全量生态**：BBC 主站（`bbc.co.uk`, `bbc.com`）、BBC iPlayer、BBC Sounds 网页及移动组件（`bbci.co.uk`, `bbci.co`）、全球新闻及多语言广播。
* **BBC 核心流媒体 CDN 播流调度**：Akamai 实时音视频 DASH/HLS 切片（`aod-dash-uk-live.akamaized.net`, `vod-dash-uk-live.akamaized.net`, `vod-hls-uk-live.akamaized.net` 等）、Limelight Networks（`bbcfmt.hs.llnwd.net`）。
* **ITV 全量生态**：`itv.com`、`itvstatic.com`、ITVX 流媒体移动端 Akamai CDN。
* **Channel 4 / All 4**：`channel4.com`、`c4assets.com`。
* **Channel 5 (My5) & BritBox & Sky**：`channel5.com`、`my5.tv`、`britbox.co.uk`、`nowtv.com`、`skygo.co.uk`。
* **使用策略**：专用 `英国节点` 策略组（必须选择能解锁 BBC iPlayer / ITV 英区版权限制的英国住宅或原生代理节点）。

### 8. Apple TV / Apple TV+ 专属流媒体规则 (`AppleTV.yaml`)
结合 `mixed.yaml`（Streaming AppleTV）与真实流量深度分析，精准提炼：
* **Web 与客户端主站**：`tv.apple.com`、`linear.tv.apple.com`（线性频道直播流）、`tv.applemusic.com`。
* **音视频切片流媒体 CDN**：`play-edge.itunes.apple.com`（核心加密点播切片）、`np-edge.itunes.apple.com`、`hls.itunes.apple.com`、`hls-amt.itunes.apple.com`。
* **地域版权验证与鉴权元数据**：`gspe1-ssl.ls.apple.com`（地理位置与区域授权验证，防版权限制核心）、`uts-api.itunes.apple.com`、`umc-api.itunes.apple.com`。
* **使用策略**：`PROXY` 或专用的 `AppleTV` 流媒体策略组（选择美区、台区、港区、日区等支持 Apple TV+ 原生解锁的代理节点）。

### 9. Apple 全生态基础服务规则 (`Apple-Services.yaml`)
结合 `mixed.yaml` 与 `MESL+tempjms-apple.yaml`（Apple 全量生态），涵盖：
* **App Store 与 TestFlight**：`appstore.com`、`appsto.re`、`itunes.com`、`mzstatic.com`、`testflight.apple.com`。
* **iCloud 云服务与同步**：`icloud.com`、`icloud-content.com`（照片与大文件传输）、`apple-cloudkit.com`（跨设备同步）、`me.com`。
* **官方主站与静态 CDN**：`apple.com`、`apple.co`、`aaplimg.com`、`cdn-apple.com`、`organicfruitapps.com`。
* **Apple News（新闻服务）**：`apple.news`、`news-client.apple.com`、`news-edge.apple.com`（有严格区域限制）。
* **Siri 智能助手与搜索建议**：`guzzoni.apple.com`、`smoot.apple.com`。
* **推送服务 (APNs) 与 Private Relay 隐私中继**：`push.apple.com`、`apple-relay.apple.com`、`apple-relay.cloudflare.com`。
* **使用策略**：`DIRECT`（国内直连加速）或由专用 `Apple` 策略组智能托管。

### 10. TikTok 全量生态分流规则 (`TikTok.yaml`)
结合 Mac 桌面网页端 + iPhone 客户端双端实机抓包深度分析，涵盖：
* **全端共用核心主站与 API**：`tiktok.com`、`tiktokv.com`、`tiktokv.us`（美区核心 API 网关）、`tiktokw.us`（网页端安全 SDK）、`tik-tokapi.com`。
* **音视频与多媒体 CDN**：`tiktokcdn.com`（全球核心音视频/图片 CDN）、`tiktokcdn-us.com`（美区核心切片流媒体 CDN）、`ttcdn-us.com`（美区电商与综合资源 CDN）、`-tiktokcdn-com`（Akamai 边缘节点专线）。
* **iPhone / 移动端特有架构**：美区“德州计划”(Project Texas) 甲骨文云专属合规网关与遥测代理（`config.mtp.sag.us-ashburn-1.oci.oraclecloud.com`、`proxy.telemetry.us-ashburn-1.oci.oraclecloud.com`）、端智能 AI 架构 Pitaya 与 Tako 推荐模型（`pitaya-clientai.com`）、滤镜特效（`byteeffecttos-g.com`）、TikTok 专属 AppsFlyer 归因打点（`roovza.*.appsflyersdk.com`）、客户端进程（`com.zhiliaoapp.musically`、`TikTok`）。
* **Mac 桌面网页端特有资源**：网页端核心静态与登录鉴权（`ttwstatic.com` / `sf16-website-login`）、内核容器（`ttwebview.com`）、通用图床（`ibyteimg.com`）。
* **海外基建、电商与衍生生态**：TikTok Shop 美区电商（`tiktokshops.us`）、TikTok Music（`tiktokmusic.app`）、剪映海外版 CapCut（`capcut.com`）、字节跳动海外技术底座（`byteoversea.com`、`ibytedtos.com`、`bytedapm.com`、`bytegecko-i18n.com`、`ipstatp.com`、`sgpstatp.com`）、Musical.ly 历史兼容资产。
* **使用策略**：专用的 `TikTok` 流媒体策略组（选择美区、新加坡、日本等支持 TikTok 解锁的住宅或原生代理节点，注意避开国内/香港节点）。

### 11. X (Twitter) 与全球主流成人媒体规则 (`X-Porn.yaml`)
结合 Mac 桌面网页端 + iPhone 客户端双端实机抓包深度分析，涵盖：
* **X (Twitter) 全量官方生态**：`x.com`、`twitter.com`、`t.co`（官方跳转短链）、`twimg.com`（核心图床与音视频分发 CDN）、`tweetdeck.com`、`twvid.com`、`twitter.biz`、`twtrdns.net` 等。
* **Pornhub 全球生态与多媒体 CDN**：`pornhub.com`、`phncdn.com`（全量加密点播切片与图片 CDN）、`pornhubpremium.com`、`youporn.com`、`redtube.com`、`brazzers.com` 等。
* **XVideos & XNXX 核心生态**：`xvideos.com`、`xvideos-cdn.com`（全球核心 HLS 视频切片 CDN）、`xnxx.com`、`xnxx-cdn.com` 等。
* **其他主流平台与日韩影视**：`xhamster.com`、`stripchat.com`、`spankbang.com`、`dmm.co.jp`、`javdb.com`、`javbus.com` 等。
* **使用策略**：`PROXY` 或专用的 `X-Porn` / `流媒体` 策略组。

---

## 在 Stash 中的标准配置示例

```yaml
rule-providers:
  # 1. 订阅大陆主流视频网站与 App PCDN 偷跑拦截规则集
  china-video-apps-pcdn:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/China-Video-Apps-PCDN.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/China-Video-Apps-PCDN.yaml"
    path: ./ruleset/china-video-apps-pcdn.yaml
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

  # 4. 订阅全球海外新闻与专业媒体规则集
  foreign-news:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Foreign-News.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Foreign-News.yaml"
    path: ./ruleset/foreign-news.yaml
    interval: 86400

  # 5. 订阅 OpenAI / ChatGPT 全量生态规则集
  openai:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/OpenAI.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/OpenAI.yaml"
    path: ./ruleset/openai.yaml
    interval: 86400

  # 6. 订阅 Google 全球搜索与 Gemini 智能生态规则集
  google-gemini:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/GoogleSearch-Gemini.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/GoogleSearch-Gemini.yaml"
    path: ./ruleset/google-gemini.yaml
    interval: 86400

  # 7. 订阅英国全媒体与流媒体规则集 (BBC / ITV / C4)
  uk-media:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/UK-Media.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/UK-Media.yaml"
    path: ./ruleset/uk-media.yaml
    interval: 86400

  # 8. 订阅 Apple TV+ 专属流媒体规则集
  appletv:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/AppleTV.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/AppleTV.yaml"
    path: ./ruleset/appletv.yaml
    interval: 86400

  # 9. 订阅 Apple 全生态基础服务规则集
  apple-services:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Apple-Services.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Apple-Services.yaml"
    path: ./ruleset/apple-services.yaml
    interval: 86400

  # 10. 订阅 TikTok 全量生态规则集
  tiktok:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/TikTok.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/TikTok.yaml"
    path: ./ruleset/tiktok.yaml
    interval: 86400

  # 11. 订阅 X (Twitter) 与全球主流成人媒体规则集
  x-porn:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/X-Porn.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/X-Porn.yaml"
    path: ./ruleset/x-porn.yaml
    interval: 86400

rules:
  # 必须排在最前面：优先阻断所有 P2P 偷跑连接与轻量广告
  - RULE-SET,china-video-apps-pcdn,🛑 全球拦截
  - RULE-SET,hagezi-light,🛑 全球拦截

  # 抖音官方核心业务直连
  - RULE-SET,douyin,👁️ Douyin

  # TikTok 全量生态走专用海外流媒体策略组（解锁节点）
  - RULE-SET,tiktok,👁️ TikTok

  # Apple TV+ 专属流媒体走支持区域版权解锁的节点
  - RULE-SET,appletv,👁️ AppleTV

  # Apple 全生态基础服务（可走 DIRECT 或专属策略组）
  - RULE-SET,apple-services,🍎 Apple Services

  # YouTube 流量走代理或专属流媒体组
  - RULE-SET,youtube,🎬 YouTube

  # X (Twitter) 与主流成人影视走专属策略组或流媒体代理
  - RULE-SET,x-porn,🔞 X Porn

  # Google 全球搜索与 Gemini 走专用代理节点（统一出口避免风控）
  - RULE-SET,google-gemini,🔍 Google Gemini

  # OpenAI / ChatGPT 生态走专用代理节点
  - RULE-SET,openai,🤖 OpenAI

  # 英国全媒体走英国专属原生/住宅解锁节点 (BBC iPlayer / ITV)
  - RULE-SET,uk-media,📡 UK Media

  # 全球海外新闻与专业媒体走专属代理策略组
  - RULE-SET,foreign-news,📰 Foreign News

  # 后续其他分流规则
  - GEOIP,CN,🎯 全球直连
  - MATCH,🐟 漏网之鱼
```

