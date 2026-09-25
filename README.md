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

### 3. 全球海外综合与专业前沿新闻规则 (不含 NYT / WSJ) (`Foreign-News-no-NYT-WSJ.yaml`)
基于真实 Chrome 浏览器历史记录全量深度分析（8万+记录），专门剔除了中国大陆境内媒体，专为科学上网分流与海外优质资讯代理设计。涵盖：
* **全球综合大报与通讯社**：英国卫报、泰晤士报、每日电讯报、洛杉矶时报、法兰克福汇报、世界报、时代周报、费加罗报、读卖新闻、东亚日报、美联社、CNN、CBS、NBC、德国之声、法国国际广播、联合国新闻等（注：纽约时报 NYT 与华尔街日报 WSJ 已单独剥离至专属规则集 `NYT-WSJ.yaml`）。
* **数字报刊与聚合平台**：PressReader（全球报刊亭旗舰，高频阅读数千次）。
* **深度财经与宏观经济**：金融时报、彭博法律、CNBC、香港瑞恩资本、香港经济通、NBER（美国国家经济研究所）、AEA（美国经济学会）等（注：道琼斯集团及旗下媒体已移至 `NYT-WSJ.yaml`）。
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

### 13. 纽约时报、华尔街日报与美国轻量金融/敏感服务 (`NYT-WSJ-US-Light.yaml`)
基于真实 iPhone 移动客户端与 Mac 桌面浏览器双端实机抓包深度分析，完整提取 The New York Times 与 The Wall Street Journal（含道琼斯 Dow Jones 集团）核心资产，并融合美国原生轻量金融与敏感资产（已从 `Foreign-News-no-NYT-WSJ.yaml` 及其他规则中完全剥离解耦）：
* **The New York Times (NYT / 纽约时报)**：纽约时报核心主站、国际版、中文网、Samizdat GraphQL API 网关（`samizdat-graphql.nytimes.com`）、核心多媒体/短域（`nyt.com`、`a1.nyt.com`、`g1.nyt.com`）、高清图床 CDN（`nytimg.com`）、集团公司（`nytco.com`）、时尚版（`nytstyle.com`）、版本对比（`nytdiff.com`）与官方品牌域（`newyorktimes.com`）。
* **The Wall Street Journal (WSJ / 华尔街日报)**：华尔街日报核心主站（`wsj.com`）、移动端与 Web API（`follow-api.wsj.com`、`video-api.wsj.com`）、报纸数字版（`pbc.wsj.com`、`pblog.wsj.com`）、核心音视频流媒体（`wsjstream.wsj.net`）、图床与静态组件 CDN（`wsj.net`、`images.wsj.net`、`opinion-images.wsj.net`）、读者会员权益（`wsjplus.com`）。
* **Dow Jones (道琼斯集团与 News Corp 商业矩阵)**：道琼斯公司官网与统一单点登录 SSO 鉴权网关（`dowjones.com`、`sso.accounts.dowjones.com`）、道琼斯云原生微服务与公共共享数据网关（`dowjones.io`、`shared-data.dowjones.io`）、订单订阅系统（`dowjoneson.com`、`oms.dowjoneson.com`）、巴伦周刊（`barrons.com`）、MarketWatch 实时金融行情（`marketwatch.com`）、Mansion Global 豪宅不动产（`mansionglobal.com`）、Factiva 商业情报库（`factiva.com`）、新闻集团统一平台（`newscgp.com`）。
* **抓包定制接口与读者鉴权通道**：Adobe 专为道琼斯定制的分析节点（`dowjones.hb-api.omtrdc.net`、`dowjones.sc.omtrdc.net`）、道琼斯专用 AWS 资产存储桶（`djcm-pnp.s3.amazonaws.com`、`djcs-multi-region-assets-ohio.s3.us-east-2.amazonaws.com`）、波士顿公共图书馆读者卡免登录鉴权联动（`bpl.org` / EZProxy 联动 `partner.wsj.com`）。
* **美国轻量金融、支付与权威快讯**：PayPal、Venmo、Braintree、Xoom、BillMeLater，彭博社 Bloomberg、路透社 Reuters、Reddit、Perplexity 等。
* **使用策略**：专用的优质美国原生/静态代理策略组（如 `🇺🇸 US Light Data Usage Select`），享受纯净 IP 避免被两报严格的风控系统拦截或触发验证码。
* **附：NYT 与 WSJ 的广告体系构成与分流/拦截深度剖析**：
  在实际阅读中，部分用户希望完整保留两家大报的广告（例如欣赏高质量商业品牌赞助、避免触发网站“检测到广告拦截插件 `Ad-blocker detected`”的阻断弹窗），而部分用户则希望彻底去除。深入理解两家大报的广告分层构成是进行精准分流配置的前提：
  1. **第一层：第一方自营赞助与原生内容广告（1st-Party Native & Direct Sponsorship）**
     * **架构特征**：由报业集团直接向高端商业品牌（如劳力士、保时捷、路易威登、各大投行等）直接招商，深度内嵌于版面、正文信息流与特约专栏（Paid Post / Sponsor Content）中的自营图文与视频。
     * **核心接口与分发域名**：
       * **The New York Times (NYT)**：通过 GraphQL 网关 `samizdat-graphql.nytimes.com` 随正文直接下发元数据，第一方广告服务器与事件打点为 `adx.nytimes.com`、`et.nytimes.com`（Event Tracker）、`purr.nytimes.com`（隐私与广告授权协议），静态素材由官方高防图床 `static01.nyt.com` 承载。
       * **The Wall Street Journal (WSJ / Dow Jones)**：依托道琼斯商业矩阵，使用专为大型出版商定制的 Kevel / Adzerk 原生广告系统 `dj.adzerk.net`，以及道琼斯第一方媒体分发接口 `s.wsj.net`、`images.wsj.net`、`dowjones.hb-api.omtrdc.net`。
     * **分流与拦截表现**：此类广告与正文主站同域或挂在出版商第一方域名下，直接收录于 `NYT-WSJ-US-Light.yaml` 并路由至美国原生代理出口。默认完全畅通，不仅能欣赏高质量品牌广告，还能彻底避免触发两报前端的反广告拦截插件检测（Ad-Blocker Detection）。
  2. **第二层：第三方程序化展示广告与头部竞价（3rd-Party Programmatic Display & Header Bidding）**
     * **架构特征**：正文中间穿插的嵌入式方块横幅（Display Banner）、侧边栏浮动推荐、通栏广告与视频贴片，通过全球广告联盟与即时竞价网络（RTB）动态拉取。
     * **底层基建（Google Ad Manager / DoubleClick）**：两报最主要的展示广告基础设施供应商，核心域名包括 `doubleclick.net`（含 `googleads.g.doubleclick.net`、`adx.g.doubleclick.net`）、`googleadservices.com`、`googlesyndication.com`、`adservice.google.com`。
     * **程序化交易与头部竞价伙伴（Ad Exchanges / Header Bidding）**：`rubiconproject.com`（Magnite）、`criteo.com` / `criteo.net`、`casalemedia.com`（Index Exchange）、`amazon-adsystem.com`（Amazon A9 广告系统）、`scorecardresearch.com` / `chartbeat.com`（广告可见度与阅读热度监测）。
     * **分流与拦截表现**：此类跨域商业广告会直接命中通用的去广告规则集（如 `AdBlock.yaml`、`hagezi-light`）并被 `REJECT` 拦截丢弃。
  3. **用户策略选择指引（想看广告 vs 彻底去广告）**：
     * **需求 A：想看广告 / 彻底避免反拦截弹窗**：
       * *仅看第一方原生赞助*：只需确保 `NYT-WSJ-US-Light.yaml` 规则集正常生效即可，第一方广告自然展示且完全不影响日常阅读。
       * *全量看横幅与方块广告（复刻 MESL 表现）*：在客户端主配置中，将 `doubleclick.net`、`googleadservices.com`、`googlesyndication.com` 从 `REJECT` 列表移出，改走 Google 策略组（或直接放行走代理）。
     * **需求 B：追求纯净阅读与极致省电**：
       * 保持 `AdBlock.yaml` 位于规则前列，优先丢弃所有第三方程序化广告和追踪监测，大幅减少网络请求并发与后台基带能耗。


### 14. 微软全生态服务规则 (`Microsoft.yaml`)
涵盖 Microsoft 核心主站、Windows 系统更新、Office 365 / Microsoft 365 协同套件、OneDrive 云盘、Azure 云计算基础设施、Bing 必应搜索、Teams/Skype 统一通讯、Xbox 游戏网络与世纪互联运营中国区资产：
* **Microsoft 账户与核心认证**：`microsoft.com`、`live.com`、`msftauth.net`、`msauth.net`、`msidentity.com`、`account.microsoft.com`、`login.microsoftonline.com` 等。
* **Office 365 / Microsoft 365 协作套件**：`office.com`、`office365.com`、`sharepoint.com`、`onenote.com`、`sway.com`、`yammer.com`、`mstea.ms`、`teams.microsoft.com` 等。
* **OneDrive / SkyDrive 云存储客户端**：`1drv.ms`、`onedrive.com`、`livefilestore.com`、进程名 `OneDrive` 与 `OneDriveUpdater`。
* **Azure 云计算基础设施**：`azure.com`、`azure.net`、`azureedge.net`、`cloudapp.net`、`trafficmanager.net`、`azurewebsites.net` 等。
* **Windows 系统生态与 Edge 浏览器**：`windows.com`、`windowsupdate.com`、`msedge.net`、`microsoftstore.com` 等。
* **Bing 搜索、MSN 与 Skype 通讯**：`bing.com`、`msn.com`、`skype.com`、`lync.com` 等。
* **世纪互联运营中国区资产**：`21vbc.com`、`21vbluecloud.com`、`azure.cn`、`partner.microsoftonline.cn` 等。
* **使用策略**：`🖥 Microsoft` 或 `DIRECT` / `PROXY` 节点策略组。

### 15. Prime Video、Pluto TV、CBS 及其他海外流媒体合集 (`Prime-Pluto-CBS-Other.yaml`)
整合 Amazon Prime Video、Pluto TV 以及 CBS / Paramount+ / Showtime 全量海外流媒体分发、API 与播放调度（共 78 条高精度规则）：
* **Amazon Prime Video**：`primevideo.com`、`amazonvideo.com`、`pv-cdn.net`、`aiv-cdn.net`、`aiv-delivery.net`、CloudFront 媒体流切片节点、macOS/iOS 客户端进程。
* **Pluto TV 电视直播**：`pluto.tv`、`plutotv.net`。
* **CBS / Paramount+ / Showtime / Viacom 矩阵**：`cbs.com`、`cbsnews.com`、`paramount.com`、`paramountplus.com`、`pplusstatic.com`、`showtime.com`、`viacomcbs.com` 等。
* **使用策略**：`👁️ Prime Pluto CBS` 或专用的海外版权解锁代理策略组。

### 16. 常用广告与开屏追踪拦截补充规则集 (`AdBlock.yaml`)
专为中国大陆主流互联网服务、社交、长短视频与外媒移动端深度定制的广告与商业追踪阻断规则集（收录 570+ 条精选高价值规则）：
* **开屏广告与商业化分发调度**：Bilibili 商业化分发 (`cm.bilibili.com`)、优酷开屏追踪 (`sealine.youku.com`)、字节营销引流落地页 (`+.lf-leads-fe-scm.bytecdn.com`)、Google AdMob 国内 CDN (`+.doubleclick-cn.net`) 等。
* **移动端广告联盟矩阵**：腾讯广点通 GDT (`mi.gdt.qq.com`, `qzs.gdt.qq.com`, `v.gdt.qq.com`, `adsmind.gdt.qq.com`)、百度移动联盟 (`mobads.baidu.com`, `mobads-logs.baidu.com`)、微博商业投放 (`sdkapp.uve.weibo.com`, `adstrategy.biz.weibo.com`)、知乎商业化 (`appcloud2.in.zhihu.com`, `sugar.zhihu.com`)。
* **曝光监控、打点统计与归因监测**：B站广告曝光与打点 (`bimp.hdslb.com`, `boss.hdslb.com`)、Apple Search Ads 归因 (`ca.iadsdk.apple.com`)、IAS 广告可见度监测 (`dt.adsafeprotected.com`)。
* **外媒嵌入式高并发程序化广告与追踪**：Permutive、Piano.io、BidSwitch、3Lift、Media.net、Parse.ly、Spot.im、Datadog RUM 等高并发追踪器（有效阻断外媒阅读时的电池偷跑与机身发烫）。
* **使用策略**：`REJECT` 或专用的 `🛑 全球拦截` 策略组。

---

## 开屏广告与商业追踪深度治理指南 (不同 App 架构与实战分析)

基于多次 iPhone 实机运行抓包日志（含 B站、抖音、优酷、阿里系/闲鱼、外媒及各类系统服务）与内核行为分析，去广告与防追踪方案必须**因 App 制宜**，绝不能盲目一刀切。

### 1. 核心原则：为什么必须因 App 制宜？

不同互联网大厂的客户端在网络底层实现、安全策略和接口架构上存在本质差异：
* **网络底层与协议栈差异**：标准系统网络库（如 Apple CFNetwork / NSURLSession） vs 自研定制网络栈（如字节跳动基于 Chromium 深度定制的 TTNet/Cronet、阿里巴巴 Agoo/mTOP 网关）。
* **接口设计解耦程度差异**：独立广告分发路径（如 `/x/v2/splash/`） vs 复合多合一业务网关（如 `is.snssdk.com` 同时承载设备激活、登录凭证、配置拉取与开屏广告）。
* **安全与防抓包机制差异**：标准 TLS 通信 vs 严格证书锁定（SSL Pinning）、全链路请求签名防篡改（如 `X-Gorgon` / `X-Khronos`）、动态环境检测（如阿里无线保镖 SecurityGuardSDK）。

如果忽视这些差异，盲目全局开启 MITM 并挂载 Script：
1. **加剧设备发烫与掉电**：iOS 系统每遇到挂载脚本的请求，代理都需要唤醒 JavaScriptCore 虚拟机进行 JSON 树的深度遍历与反序列化，频繁触发垃圾回收（GC），是导致 iOS 代理软件后台发烫的核心诱因；
2. **引发 App 异常断网或风控**：遇到强证书锁定或防篡改验签的 App，中间人解密会导致 TLS 握手失败、请求直接报错甚至触发账户异地风控。

### 2. 各大主流 App 架构特征与具体处理策略（结合实机日志分析）

| 分类 | 典型 App / 域名 | 底层网络特征 | 最佳处理方案 | 为什么这么做（避免发热与报错） |
| :--- | :--- | :--- | :--- | :--- |
| **类型一：独立商业/开屏分发主域** | **哔哩哔哩** (`cm.bilibili.com`, `bimp.hdslb.com`)<br>**优酷** (`sealine.youku.com`)<br>**Google AdMob** (`+.doubleclick-cn.net`)<br>**腾讯广点通 GDT** (`*.gdt.qq.com`)<br>**百度移动联盟** (`mobads.baidu.com`) | 广告请求走独立子域名或独立 CDN，与核心业务流量完全解耦 | **域名层拦截 (REJECT)**<br>*(收录于 `AdBlock.yaml`)* | **最省电、零发热**：内核级字典匹配，纳秒级直接丢弃。App 探测超时或断开后内置逻辑直接跳过广告进首页，完全不需要 MITM。 |
| **类型二：业务广告同域，但有独立 API 路径** | **知乎** (`/commercial_api/real_time/launch`)<br>**微博** (`/2/ad/*`)<br>**网易云音乐** (`/api/ad/get`)<br>**哔哩哔哩备用开屏** (`/x/v2/splash/`) | 与核心 API 共用域名，但开屏由独立 REST 路径下发，无强防篡改校验 | **MITM + Rewrite**<br>*(本地 Mock `reject-dict`)* | **秒进首页且不发烫**：Stash 代理内核用正则命中后直接在本地返回空字典 `{}`（耗时仅 0.05ms），无需连接远端服务器，无需拉起 JS 虚拟机，避免了 Script 带来的 CPU 与发热开销。 |
| **类型三：严格证书锁定 / 自研网络栈 / 复合网关** | **抖音 / 今日头条** (`is.snssdk.com`)<br>**闲鱼 / 淘宝 / 支付宝** (`acs.m.goofish.com`, `amdc.alipay.com`)<br>**微信 / 银行金融客户端** | 采用 Chromium TTNet / mTOP 网关，开启强制 SSL Pinning，含全链路动态哈希验签（如 `X-Gorgon`），多业务混用 | **严禁开启 MITM 与 Script！**<br>*(仅封禁其外挂打点域名如 `lf-leads-fe-scm.bytecdn.com`)* | **防断网与风控**：一旦解密解开，客户端会报证书不受信任直接中断网络；若用脚本篡改响应，验签失败会导致无法登录、信息流空白。维持纯网络直连最安全。 |
| **类型四：混合复合包且校验非空字段** | **极个别顽固小众 App** | 开屏广告与 App 冷启动核心参数硬编码在同一个 JSON 结构体中，返回空包会导致 App 崩溃 | **MITM + 针对性 Script (按需单点使用)** | **保底兼容**：仅对特定 URL 单点挂载极简 JS 脚本剔除广告节点。严禁全局通配挂载，避免后台全天候高频消耗 CPU。 |

### 3. 三种拦截手段的性能与发热能耗对比

```
【方案 A：DNS / 域名 REJECT】（当前 AdBlock.yaml 采用）：
  TCP 连接 -> 规则集 Hash 命中 -> 立即 REJECT 丢弃
  ⚡️ 耗时: < 0.01 ms | 💻 CPU/内存占用: 接近 0 | 🔋 手机发热: 零发热，最省电

【方案 B：MITM + URL Rewrite (reject-dict / reject-200)】：
  HTTPS 握手 -> 代理内核 URL 正则匹配 -> 本地直接构造 HTTP 200 {} 返回
  ⚡️ 耗时: ≈ 0.05 ms | 💻 CPU/内存占用: 极低（纯 Go/C 内核层处理） | 🔋 手机发热: 几乎无感

【方案 C：MITM + Script (JavaScript 响应体篡改)】：
  HTTPS 握手 -> 连远端服务器 -> 接收几十KB数据 -> 启动 JavaScriptCore 虚拟机
  -> 跨语言内存拷贝 -> JSON.parse 解析 -> JS 遍历删除节点 -> JSON.stringify 序列化
  -> 跨语言拷贝回网络栈 -> 触发 JS 引擎垃圾回收 (GC) -> 返回给 App
  ⚡️ 耗时: 10 ~ 50 ms | 💻 CPU/内存占用: 极高 (频繁内存分配与 GC) | 🔋 手机发热: ⚠️ 严重，手机发烫掉电的主要诱因之一
```

### 4. 落地配置最佳实践决策树

1. **第一优先级（首选）**：只要该 App 的开屏请求能抓到独立的广告域名/CDN，**一律加入 `AdBlock.yaml` 走纯域名层 REJECT**。
2. **第二优先级（次选）**：如果无法通过域名拦截（例如拦截后无法正常登录），但该 App 开屏有单独的 API 路径且不受 SSL Pinning 限制，**在 MITM 中仅解密该域名，并使用 Rewrite (`reject-dict`) 进行本地空 Mock**。
3. **第三优先级（保底）**：只有在以上两步都无法解决、且 App 强依赖开屏响应体中的其他必要字段时，**才针对单一 URL 配置极简 Script 脚本**。

---

## 在 Stash 中的标准配置示例

```yaml
rule-providers:
  # 1. 订阅 YouTube、X (Twitter) 与全球主流成人媒体合集
  youtube-porn-x:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/YouTube-Porn-X.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/YouTube-Porn-X.yaml"
    path: ./ruleset/youtube-porn-x.yaml
    interval: 86400

  # 2. 常用广告与开屏追踪拦截补充规则集 (AdBlock)
  adblock:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/AdBlock.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/AdBlock.yaml"
    path: ./ruleset/domain-AdBlock.yaml
    interval: 86400

  # 3. 订阅抖音官方直连规则集
  douyin:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Douyin.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Douyin.yaml"
    path: ./ruleset/douyin.yaml
    interval: 86400

  # 4. 订阅全球海外新闻与专业媒体规则集 (不含 NYT / WSJ)
  foreign-news:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Foreign-News-no-NYT-WSJ.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Foreign-News-no-NYT-WSJ.yaml"
    path: ./ruleset/foreign-news-no-nyt-wsj.yaml
    interval: 86400

  # 5. 订阅 OpenAI / ChatGPT 全量生态规则集
  openai:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/OpenAI.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/OpenAI.yaml"
    path: ./ruleset/openai.yaml
    interval: 86400

  # 6. 订阅 Google 全球搜索与 Gemini 智能生态规则集
  google-gemini:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/GoogleSearch-Gemini.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/GoogleSearch-Gemini.yaml"
    path: ./ruleset/google-gemini.yaml
    interval: 86400

  # 7. 订阅英国全媒体与流媒体规则集 (BBC / ITV / C4)
  uk-media:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/UK-Media.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/UK-Media.yaml"
    path: ./ruleset/uk-media.yaml
    interval: 86400

  # 8. 订阅 Apple TV+ 专属流媒体规则集
  appletv:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/AppleTV.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/AppleTV.yaml"
    path: ./ruleset/appletv.yaml
    interval: 86400

  # 9. 订阅 Apple 全生态基础服务规则集
  apple-services:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Apple-Services.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Apple-Services.yaml"
    path: ./ruleset/apple-services.yaml
    interval: 86400

  # 10. 订阅 TikTok 全量生态规则集
  tiktok:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/TikTok.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/TikTok.yaml"
    path: ./ruleset/tiktok.yaml
    interval: 86400

  # 11. 订阅学术数据库与文献资源直连规则集
  academic-direct:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Academic-Direct.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Academic-Direct.yaml"
    path: ./ruleset/academic-direct.yaml
    interval: 86400

  # 12. 订阅中国大陆主流服务直连规则集
  china-direct:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/China-Direct.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/China-Direct.yaml"
    path: ./ruleset/china-direct.yaml
    interval: 86400

  # 13. 订阅纽约时报、华尔街日报与美国轻量金融服务合并规则集
  nyt-wsj-us-light:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/NYT-WSJ-US-Light.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/NYT-WSJ-US-Light.yaml"
    path: ./ruleset/nyt-wsj-us-light.yaml
    interval: 86400

  # 14. 订阅微软全生态服务规则集 (Windows / Office 365 / Azure / OneDrive)
  microsoft:
    type: http
    behavior: domain
    format: yaml
    url: "https://raw.githubusercontent.com/flyingparanoia/ProxyRules/main/Microsoft.yaml"
    # 国内加速备用: "https://cdn.jsdelivr.net/gh/flyingparanoia/ProxyRules@main/Microsoft.yaml"
    path: ./ruleset/microsoft.yaml
    interval: 86400

rules:
  # 必须排在最前面：优先阻断广告与商业化追踪
  - RULE-SET,adblock,🛑 全球拦截
  - RULE-SET,hagezi-light,🛑 全球拦截

  # 学术数据库走直连（保障高校机构与 CARSI 认证免登录下载正文）
  - RULE-SET,academic-direct,🎯 全球直连

  # 中国大陆主流互联网服务直连加速
  - RULE-SET,china-direct,🎯 全球直连

  # 抖音官方核心业务直连
  - RULE-SET,douyin,👁️ Douyin

  # 纽约时报、华尔街日报与美国轻量金融服务走专用美国轻量/高防风控代理 (防账号风控与频繁验证码)
  - RULE-SET,nyt-wsj-us-light,🇺🇸 US Light Data Usage Select

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

  # 微软全生态服务走专有策略组 (或 DIRECT / PROXY)
  - RULE-SET,microsoft,🖥 Microsoft

  # 英国全媒体走英国专属原生/住宅解锁节点 (BBC iPlayer / ITV)
  - RULE-SET,uk-media,📡 UK Media

  # 全球海外新闻与深度媒体走专属代理策略组 (如 🚀 节点选择)
  - RULE-SET,foreign-news,🚀 节点选择

  # 后续其他分流规则
  - GEOIP,CN,🎯 全球直连
  - MATCH,🐟 漏网之鱼
```

---

## 移动端性能避坑指南：机场官方订阅配置（以 MESL 为例）在 iOS 端的性能灾难分析

在 iOS 环境下使用 Stash / Clash 等代理客户端时，许多用户常遭遇**机身严重发烫、掉电如崩盘、甚至代理频繁后台被系统杀死（闪退断网）**的问题。经对知名中转/家宽机场（以 MESL 官方订阅导出的 Stash/Clash 完整配置 `MESL-debug.yaml` 为例）及实机内核日志（`2026-09-26-055305.log`，测试时长不足 2 分钟）进行深度逆向与追踪分析，揭示了其在移动端性能极其糟糕的五大底层架构缺陷。

### 1. 核心病因深度剖析（实机内核数据实锤）

#### ① 3,500+ 条纯 Classical 线性规则：CPU 陷入 $O(N)$ 匹配黑洞
* **机制缺陷**：
  Stash 官方在《编写高效配置文件》中明确告诫：
  > *“严禁在配置中使用大量 Classical 类型的规则集合，因为此类规则仅支持顺序匹配，会显著增加匹配耗时和内存占用。”*
  
  MESL 官方配置将多达 **3,523 条规则**全部以明文形式平铺在配置文件的 `rules:` 根节点下。此类古典规则无法被编译为前缀树（Trie Tree）或基数树（Radix Tree），每一个数据包都必须经历从第 1 条逐行扫描到第 3,523 条的低效线性比对。
* **实测日志数据**：
  在短短 100 秒的日常使用日志中，共记录 267 个 TCP 连接，其中**多达 162 个连接（占比超 60%）命中末尾的 `MATCH` 规则**。这意味着：
  $$\text{规则匹配次数} \approx 162 \times 3,523 \approx 570,000 \text{ 次/百秒}$$
  仅仅处理百秒内的日常后台连接，手机 CPU 就承受了近 60 万次字符串与正则扫描，导致 CPU 核心主频被持续拉高，机身发烫不可避免。

#### ② 内存逼近 iOS 硬上限：触发系统级内存压缩（Memory Warning 轰炸）
* **机制缺陷**：
  iOS 系统对网络扩展（Network Extension）进程设置了极为严苛的内存配额（通常阈值为 30MB~50MB，超出立即触发 Jetsam 机制强制强杀）。
  MESL 官方配置内定义了 172 个节点，并在多达 31 个策略组中**全量重复平铺**这 172 个节点（产生 5,300+ 个节点引用对象），同时承载 3,500+ 个规则数据结构。
* **实测日志数据**：
  ```log
  [INFO] [05:53:06] [CORE] stash core started, used memory: 23.2M
  [WARN] [05:53:28] [OS] receive memory warning from OS, available memory: 12.9M
  [WARN] [05:53:58] [OS] receive memory warning from OS, available memory: 10M
  [WARN] [05:54:00] [OS] receive memory warning from OS, available memory: 9.9M
  ...（30 秒内连续爆发 9 次系统级 Memory Warning）
  ```
* **发烫元凶**：
  启动即吃掉 **23.2 MB**，可用内存瞬间跌破 10 MB。当 iOS 系统高频下发 `Memory Warning` 时，iOS 内核级内存压缩器（`vm_compressor`）与 Stash 内部 GC 垃圾回收器会以最高 CPU 优先级拼命执行内存腾挪与换页，极短时间内将整机烧成“暖手宝”，且随时面临闪退风险。

#### ③ 尾部 IP/GEOIP 规则缺失 `no-resolve`：引发 DNS 级联雪崩
* **机制缺陷**：
  在配置的第 3,737~3,747 行，尾部内网段规则（如 `IP-CIDR,127.0.0.0/8,DIRECT` 等）与 `GEOIP,CN,DIRECT` **均未声明 `no-resolve` 参数**。
* **后果**：
  根据分流内核规范，当一个域名经过前 3,500 条域名规则未被命中时，一旦遇到没有 `no-resolve` 的 IP 规则，代理内核**必须暂停分流匹配，强制向远端发起 DNS 解析**以获取该域名的真实 IP。
* **实测日志数据**：
  在 100 秒内记录了多达 **229 次 `[RSV] resolve` 远程 DNS 查询**，且全部请求发往高端口 DoH（`https://zone.rlose.com:39933`）。Wi-Fi/蜂窝基带芯片与 TLS 加密握手引擎完全无法进入睡眠状态，持续高负荷偷跑电量。

#### ④ 26 个 Benchmark 测速 Worker 后台并发空转
* **机制缺陷**：
  由于在每个策略组中均内嵌了 Fallback/Auto 等动态测速组，Stash 启动瞬间拉起了多达 **26 个后台测速 Worker**，每个 Worker 定时并发探测上百个节点，导致大量无意义的并发 TLS 握手与网络唤醒。

#### ⑤ 缺乏前置广告阻断：商业追踪全部穿透至海外代理
* **实测日志数据**：
  `criteo.com`、`chartbeat.com`、`rubiconproject.com`、`scorecardresearch.com` 等大量第三方监控与广告追踪域名，因缺乏高效的前置拦截规则，全部穿透 3,500 条规则直至末尾 `MATCH`，并通过 TLS 转发至海外家宽节点，无端空耗流量与加密运算资源。

---

### 2. 架构对比：机场官方订阅 vs 本项目优化架构

| 评估维度 | 机场官方默认配置（以 MESL 为例） | 本项目优化架构 (`ProxyRules`) |
| :--- | :--- | :--- |
| **规则匹配算法** | **$O(N)$ 逐条线性扫描**（3,523 条规则无索引） | **$O(1) \sim O(k)$ 前缀树 (Trie) / 基数树 (Radix)** |
| **规则存储形式** | 3,500+ 行 Classical 明文写死在主配置 | 模块化 `rule-providers`（由内核编译索引） |
| **主配置文件体积** | **345 KB**（充斥大量冗余重复节点定义） | **18 KB**（极其轻量，极速加载） |
| **内存占用表现** | **启动 23.2 MB**，可用余量 < 10 MB，**频繁报警告** | **启动 15~17 MB**，余量充沛，**零告警** |
| **DNS 负载行为** | 未命中规则强制触发远端 DoH 递归解析 | Fake-IP 瞬时响应，IP 规则显式解耦 |
| **垃圾追踪拦截** | 无前置拦截，流氓追踪全部穿透走代理 | 首部字典命中 `REJECT`，纳秒级直接丢弃 |
| **测速任务开销** | 26 个 Worker 轮询全量节点，常驻耗电 | 极简策略组定向测速，按需唤醒 |

---

### 3. 移动端最佳迁移与拯救方案（“借其肉，换其骨”）

**强烈建议切勿在 iPhone 等移动设备上直接运行机场导出的原生臃肿配置**。最佳的使用姿势为：

1. **提取纯节点信息**：
   仅提取机场订阅中的节点链接，或将机场订阅作为 `proxy-providers` 引入；
2. **挂载本项目高性能规则集**：
   将规则层彻底替换为本项目的 `rule-providers` 架构（如 `AdBlock.yaml`、`China-Direct.yaml`、各应用分流规则集）；
3. **保持 DNS 架构精简**：
   使用轻量高效的 Fake-IP 模式配合国内顶级公共 DNS 直连，彻底根治发热、掉电与杀后台断网。


