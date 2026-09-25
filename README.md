# ProxyRules

个人代理与分流规则集合 (Stash / Clash Rule-Providers)。

## 规则列表

### 1. YouTube、X (Twitter) 与全球主流成人媒体合集 (`YouTube-Porn-X.yaml`)
全量合并 YouTube 与 X-Porn 体系，直接对应 `mixed.yaml` 中的 `🎬 YouTube Porn X Select` 策略组：
* **全量覆盖**：集成了 YouTube 32 条全生态音视频与移动端心跳规则 + X (Twitter) 官方全量体系与 ASN BGP IP 段 + 全球 8 大成人视讯与点播切片 CDN 矩阵（共 202 条精细规则，0 冗余冲突）。
* **使用策略**：专用的 `🎬 YouTube Porn X` 流媒体策略组或高质量代理。

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

### 11. 学术数据库与文献资源直连规则 (`Academic-Direct.yaml`)
严格提取自 `mixed.yaml`（`🎓 学术资源类 —— 直连便于认证 / 学术网络识别`）并配套主流学术云补充，涵盖：
* **全球权威学术检索与分析**：Web of Science 核心正站（`webofscience.com`）、中国镜像（`webofscience.clarivate.cn`）、Clarivate 统一身份网关（`access.clarivate.com`、`clarivate.com`）、EI 工程索引（`engineeringvillage.com`）、MathSciNet（`mathscinet.ams.org`、`ams.org`）。
* **四大科学出版商与顶级期刊**：Elsevier / ScienceDirect（`sciencedirect.com`、`elsevier.com`）、Nature 自然出版集团（`nature.com`）、Science 科学杂志（`science.org`）、Wiley 在线图书馆（`onlinelibrary.wiley.com`、`wiley.com`、`ietresearch.onlinelibrary.wiley.com`）、Springer Nature（`springer.com`、`springernature.com`）。
* **工程与专业学术学会**：IEEE Xplore（`ieee.org`）、ACM 计算机学会（`acm.org`）、美国物理学会（`aps.org`）、美国物理联合会（`aip.org`）、美国机械工程师协会（`asme.org`）。
* **技术实战与国内主流平台**：O'Reilly 学习平台（`learning.oreilly.com`、`oreilly.com`）、中国知网（`cnki.net`）、超星学习通（`chaoxing.com`）、万方数据（`wanfangdata.com.cn`）、维普网（`cqvip.com`）、学术静态 CDN（`xslb.net`）。
* **高校校外身份认证**：CARSI 国家级高校身份认证联盟（`carsi.edu.cn`、`cernet.edu.cn`）。
* **使用策略**：`DIRECT`（直连，确保校园网 IP / CARSI 机构身份正常识别，避免代理引发文献下载受阻）。

### 12. 中国大陆主流服务直连规则 (`China-Direct.yaml`)
严格提取自 `mixed.yaml`（`🎯 全球直连 / 🎯 其他国内可信加速`）并经全网域深度清洗，涵盖 565 条中国大陆高频互联网服务与基础设施资产（已彻底剥离抖音/字节跳动官方资产至 `Douyin.yaml`，并排除了已单独分流的学术与应用规则）：
* **顶级域名与国区通配**：通配 `.cn`、`.中国`、`.公司`、`.网络` 及 `-cn` 关键词。
* **主流大厂核心生态 (BAT/JD/网易/米华等)**：阿里巴巴/蚂蚁金服（淘宝、天猫、支付宝、阿里云、钉钉等 38 条）、腾讯与微信（QQ、微信、腾讯云、微云等 24 条）、百度（搜索、网盘 PCS、百度云等 14 条）、京东（商城、京东云、京东支付等 12 条）、网易（163/126 邮箱、有道、LOFTER 等 11 条）、哔哩哔哩（15 条）、小米科技（8 条）、华为与鸿蒙云（9 条）、美团与大众点评（7 条）、快手短视频（4 条）、新浪与微博（6 条）、奇虎 360 与安全搜索（14 条）、搜狐门户（7 条）、金山办公 WPS（3 条）。
* **社交、社区与知识平台**：知乎、豆瓣、小红书、虎扑、酷安、果壳、简书、个人图书馆、互动百科、色影无忌等 20 条。
* **影视流媒体、音乐与网络视听**：爱奇艺、优酷土豆、芒果TV、央视CCTV/直播中国、酷狗音乐、酷我音乐、咪咕视讯、喜马拉雅 FM、荔枝 FM、虎牙直播、斗鱼、YY 语音、乐视、迅雷、人人影视/天天美剧等 103 条。
* **数字阅读与网络文学**：阅文集团、起点中文网、红袖添香、17K 小说网、笔趣阁等 12 条。
* **出行导航、铁路客运与快递物流**：12306 铁路购票、高德地图、滴滴出行、携程、去哪儿、同程旅行、顺丰速运等 16 条。
* **电商购物、品牌特卖与二手闲置**：拼多多、唯品会、苏宁易购、当当网、什么值得买、凡客诚品、聚美优品、转转二手等 24 条。
* **金融支付、商业银行与企业信用**：工农中建交四大行及招行、东方财富、雪球投资、天眼查、银联 95516、易宝支付等 8 条。
* **生活分类、房产租赁与汽车资讯**：58 同城、赶集网、房天下、乐居网、易车网、二手车 168 等 9 条。
* **时政新闻、地方门户与数码新媒体**：新华网、凤凰网、东方网、南方周末、36氪、IT之家、少数派、cnBeta、蓝点网、ZEALER、威锋网等 22 条。
* **开发者社区、在线教育与求职招聘**：CSDN、开源中国、51CTO、菜鸟教程、SegmentFault、51job 前程无忧、智联招聘、猎聘、学堂在线、中国大学 MOOC、科大讯飞等 22 条。
* **游戏生态、国服加速与玩家社区**：Steam 国区下载加速 CDN、CSGO/DOTA2 完美世界国服、暴雪战网国区、PlayStation 国区加速、TapTap、17173、3DM 等 37 条。
* **BT / PT 种子下载与 Private Tracker**：Announce/Torrent/Tracker 关键词及国内外知名 PT 站（直连省流并防止被 PT 站误判代理封号）共 32 条。
* **云计算平台、国内公共 CDN 与网络基建**：七牛云、又拍云、Staticfile、BootCDN、加速乐、网宿 CDN、DNSPod 等 32 条。
* **基础电信运营商**：中国电信、中国联通、中国移动基础网络服务。
* **办公协同、网盘存储与效率软件**：印象笔记、幕布、秀米、115网盘、永硕E盘、群晖 NAS、IPIP 定位、极验验证码等 31 条。
* **生活便民与实用工具**：中国天气网、墨迹天气、空气质量、下厨房菜谱、欧路词典等。
* **系统连通性测试与远程工具**：Windows 网络连通性测试 (NCSI) 与 TeamViewer 协同。
* **使用策略**：`DIRECT`（直连，享受本地千兆宽带低延迟高速直达）。

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

  # 2. 订阅 YouTube、X (Twitter) 与全球主流成人媒体合集
  youtube-porn-x:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/YouTube-Porn-X.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/YouTube-Porn-X.yaml"
    path: ./ruleset/youtube-porn-x.yaml
    interval: 86400

  # 3. 订阅抖音官方直连规则集
  douyin:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Douyin.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Douyin.yaml"
    path: ./ruleset/douyin.yaml
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

  # 11. 订阅学术数据库与文献资源直连规则集
  academic-direct:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Academic-Direct.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Academic-Direct.yaml"
    path: ./ruleset/academic-direct.yaml
    interval: 86400

  # 12. 订阅中国大陆主流服务直连规则集
  china-direct:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/China-Direct.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/China-Direct.yaml"
    path: ./ruleset/china-direct.yaml
    interval: 86400

rules:
  # 必须排在最前面：优先阻断所有 P2P 偷跑连接与轻量广告
  - RULE-SET,china-video-apps-pcdn,🛑 全球拦截
  - RULE-SET,hagezi-light,🛑 全球拦截

  # 学术数据库走直连（保障高校机构与 CARSI 认证免登录下载正文）
  - RULE-SET,academic-direct,DIRECT

  # 中国大陆主流互联网服务直连加速
  - RULE-SET,china-direct,DIRECT

  # 抖音官方核心业务直连
  - RULE-SET,douyin,👁️ Douyin

  # TikTok 全量生态走专用海外流媒体策略组（解锁节点）
  - RULE-SET,tiktok,👁️ TikTok

  # Apple TV+ 专属流媒体走支持区域版权解锁的节点
  - RULE-SET,appletv,👁️ AppleTV

  # Apple 全生态基础服务（可走 DIRECT 或专属策略组）
  - RULE-SET,apple-services,🍎 Apple Services

  # YouTube、X 与全球主流成人影视走专属流媒体策略组
  - RULE-SET,youtube-porn-x,🎬 YouTube Porn X

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

