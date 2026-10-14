# SQ1：海外主流 AI 绘画 / 文生图产品全景（产品形态 · 功能 · 目标用户 · 商业模式）

> 调研执行时间：2026-10-12。所有数值均标注 `unit / timepoint / scope`；`source_grade`：A=官方/财报/学术，B=行业头部媒体或头部分析机构，C=个人博客/UGC/中小媒体/聚合站。
> 事实类型标注：`hard_fact` / `estimate` / `forecast` / `rumor`。
> 引用编号 `[S#]` 对应文末「来源清单表」。无类比段。

---

## 1. 产品对比大表

### 1.1 主表（产品 / 公司 / 上线时间 / 核心功能 / 目标用户 / 商业模式 / 定价 / 体量 / 底层模型）

| # | 产品 / 公司 / 上线时间 | 核心功能（文生图之外） | 面向用户 | 商业模式 | 定价（币种+单位+时间点+套餐范围） | 公开体量数据 | 底层模型 |
|---|---|---|---|---|---|---|---|
| 1 | **Midjourney** / Midjourney, Inc.（自筹，David Holz）/ 2022 年以 Discord bot 形态公开发布 `[S16][S17]`（`hard_fact` 级别上线时间 `[待确认]`） | 图生图、Omni Reference（角色/物体一致性）、Style Reference、局部重绘 inpainting、Retexture、Web Editor 画布编辑、扩图、视频生成（SD/HD，消耗同一 Fast GPU 时长池）、批量/Repeat-Permutation、Stealth 私有生成 | 泛 C 端创作者、概念艺术家、建筑/影视前期、品牌与广告 | 纯订阅（4 档），**无免费层**；按"Fast GPU 小时"计量而非按张数；额外 GPU 时长 $4/小时；年付 8 折；>$1M 营收企业强制 Pro/Mega `[S1]` | Basic **$10/月**；Standard **$30/月**；Pro **$60/月**；Mega **$120/月**（2026，官网文档 `[S1]`）。年付：**$96 / $288 / $576 / $1,152**（一次性付清）。Fast GPU 时长：3.3 / 15 / 30 / 60 小时/月。额外时长 **$4/小时** | ARR **约 $500M–600M（2026，estimate）** `[S16]`；2024 年 PitchBook 记录 **$300M** `[S17]`；注册用户 **2,000 万+（estimate）** `[S16]`；员工约 40–60 人；**融资 $0** `[S16]`。2026-07-24 宣布收购占星 App Co-Star（4.3M MAU，金额未披露）`[S17]` | **自研**（V7 / V8.x / Niji），不开源、无公开 API `[S1][S36]` |
| 2 | **Stable Diffusion / Stability AI** / Stability AI（伦敦）/ 公司成立 2019；SD 首个公开版本 2022-08 `[S11][S27]` | 文生图、图生图、inpainting、upscale、3D/4D 视频、音频；开源权重可自托管；API；企业自托管授权 | 开发者、研究者、自托管玩家、企业（营销/游戏/影视/零售） | 开源权重免费 + API 按量 + 企业授权/自托管许可 + 专业服务；营收 >$1M 需企业许可（商业使用）`[S27][S32]` | API 约 **$0.03–$0.08 / 张（2026）** `[S32]`（`estimate`/`[待确认]`：未在本次检索中找到官方 API 定价页原文） | 融资：Series B **$76M（2026-08-25）**，累计 **$232M**（UMG/Sony Music/Warner Music/EA/AMD Ventures 参投）`[S11]`（hard_fact）。ARR **约 $90M（2026，estimate）** `[S27]`。累计生成 **70 亿+ 张**（2026 年中，公司口径）`[S27]` | **自研 + 开源权重**（SD 3.5 Large/Medium/Turbo）`[S27]` |
| 3 | **ComfyUI / Comfy Org** / 开源项目 2023 起；公司化融资 2026-04 `[S12]` | 节点式（node graph）工作流编排；图像/视频/3D/音频；本地运行 + Comfy Cloud；60,000+ 社区节点；工作流以 JSON 存储、可版本化 | 技术美术、VFX 自由职业者、工作室/代理公司、企业管线工程师 | 开源免费（承诺永久开源）+ Comfy Cloud 云服务（团队/算力）| 本地版 **$0**；Comfy Cloud 具体价格 `[待确认]`（本次未找到官方价目表） | **4,000,000 用户**、**60,000+ 社区节点**、**150,000+ 日下载**（2026-04-25，官方博客）`[S12]`（hard_fact）。融资 **$30M，估值 $500M，累计 $47M**（Craft Ventures 领投）`[S12]` | **第三方模型编排层**（本身不训练底模；可接 SD/FLUX 等任意开源权重）`[S12]` |
| 4 | **Adobe Firefly（含 Photoshop Generative Fill）** / Adobe / 公测 **2023-03-21**，商业版 **2023-09-13**；Photoshop Generative Fill 2023-05 进 beta `[S28]` | 文生图、Generative Fill（局部重绘）、Generative Expand（扩图）、Text to Vector、Generative Recolor、Firefly Boards（无限灵感板）、Firefly Graph（节点式工作流）、视频/音频/翻译、Content Credentials 溯源、Firefly Custom Models（企业训练自有模型） | 专业设计师、企业市场部、影视/零售/教育 | 「订阅 + 生成式积分」双轨：标准生成（含 Generative Fill）付费档**不限量**；高级功能（视频/音频/伙伴模型）消耗积分；积分加购包；企业层含 IP 赔付 | Free（每日免费额度）；Standard **$9.99/月**（2,000 积分）；Pro **$19.99/月**（4,000）；Pro Plus **$49.99/月**（10,000）；Premium **$199.99/月**（50,000，含 Firefly Video Model 无限）（2026-10，官网 `[S2]`）。团队版：$19.99 / $49.99 / $199.99 **per license/月**（年付月结）`[S2]` | **Firefly ending ARR 接近 $300M**（FY26 Q2，官方业绩材料）`[S10]`（hard_fact）；Adobe 整体 **AI-first ARR >$6.5 亿，同比 +>150%**（FY26 Q3）`[S9]`；创意类免费 MAU **破 1 亿，同比 +>70%** `[S9]`；FY26 Q3 总营收 **$67.6 亿，同比 +12%** `[S9]` | **自研**（Firefly Image 4 Ultra / Image 5）+ **第三方伙伴模型**（Google、OpenAI、ElevenLabs、Topaz、Runway 等）`[S2][S35]` |
| 5 | **OpenAI DALL·E / GPT-4o 原生图像 / GPT Image 2** / OpenAI / ChatGPT 2022-11；GPT Image 2 于 **2026 年发布**（具体月份 `[待确认]` `[S37]`） | 对话式迭代出图（在 ChatGPT 内）、图生图、局部编辑、Thinking Mode 先推理后出图 + 联网校准、最长边约 3840px、多语言文字渲染 | 泛 C 端、PM/运营、设计师快速出稿、开发者 | 订阅（ChatGPT 套餐含图像额度）+ API 按 token 计费；两条线独立收费 | ChatGPT：Free **$0**；Go **$8/月**；Plus **$20/月**；Pro **起价 $100/月**（2026-10，官方 `[S8]`）。API GPT-Image-2：图像输入 **$8.00/1M tokens**、缓存输入 **$2.00/1M**、输出 **$30.00/1M**（2026-10，官方 `[S7]`）。1024² 单张估算 **$0.006（低）–$0.21（高）** `[S37]`（estimate） | 单列图像收入未披露（`[待确认]`）。模型侧公开排名：LMArena 文生图与图像编辑双榜第一（2026-07 初）`[S37]`（C 级来源，见薄弱清单） | **自研**（GPT Image 2），闭源 `[S7]` |
| 6 | **Google Imagen / Nano Banana（Gemini 图像）** / Google DeepMind / Nano Banana（Gemini 2.5 Flash Image）2025；Nano Banana Pro（Gemini 3 Pro Image）2025 年末；Nano Banana 2（Gemini 3.1 Flash Image）2026-02；2.1 与 2 Lite 2026 `[S19][S20]` | 文生图、图生图、自然语言局部编辑、角色一致性（最多 5 角色 / 14 物品）、多参考图、4K 输出、SynthID 水印 | 泛 C 端（Gemini App）、开发者（API）、企业（Workspace/Vertex） | C 端订阅（Google AI 套餐）+ API 按输出 token 计费（图像模型 **无免费 API 层**）+ Batch/Flex 半价 | API：Nano Banana Pro **1K/2K 每张 $0.134；4K 每张 $0.24**；Batch/Flex **$0.067 / $0.12**；$120/1M 图像输出 token（2026，`[S19]`，C 级）。Nano Banana 2：0.5K **$0.045**、1K **$0.067**、2K **$0.101**、4K **$0.151** `[S19]`。Nano Banana 2.1：1K **$0.0336** `[S20]`。C 端订阅：Google AI Plus **$4.99/月**、Pro **$19.99/月**、Ultra **$99.99 或 $199.99/月** `[S20]` | Gemini App **9 亿 MAU**（2026-05，Google I/O 2026）`[S18]`；**Nano Banana 系列累计生成超 500 亿张图**（2026-05）`[S18]`；SynthID 已标记 **1,000 亿+ 图像/视频** `[S18]` | **自研**（Gemini 图像系列），闭源 `[S18][S19]` |
| 7 | **Ideogram** / Ideogram（多伦多）/ 公司 2022 成立 `[S29]`；产品上线时间 `[待确认]` | 文生图、图生图、Magic Fill（局部重绘）、Remix、Upscale（2K）、**Batch Generation（上传表格批量出图）**、Style/Character Reference（单图即可角色一致性）、去背景、自定义调色板、API | 品牌/平面设计师、海报/Logo/包装、电商与社媒、需要图内文字的场景 | 免费层（每周额度）+ 订阅积分（Priority credits）+ 加购积分（可结转）+ Team 按席位 + Enterprise（私有定制模型训练） | Free **$0**（每周额度）；Plus **$20/月**（年付 **$15/月，$180/年**）含 **2,400 积分/月**；Pro **$60/月**（年付 **$42/月，$504/年**）含 **7,500 积分/月**；Team **$30/用户/月**（年付 **$20/用户/月**）含 **3,600 积分/用户/月**（最少 2 席）；Enterprise 定制（2026-10，官方 `[S3]`） | 累计融资 **$96.5M**（含 a16z 领投 **$80M Series A**）`[S29]`；ARR **$7M（2025-09，estimate）** `[S29]`；团队 49 人 `[S29]` | **自研**（Ideogram 4.5 / 4.0 / 3.0 / 2a），闭源；提供 API `[S3]` |
| 8 | **Leonardo.Ai** / Leonardo.Ai（悉尼，**2024-07 被 Canva 收购**）`[S22]` / 2022-12 成立 | 文生图、Realtime Canvas（实时画布）、Realtime Generation、inpainting/outpainting、自训练模型（Personal AI models，最多 50 个）、Motion 视频、API、Canva 集成 | 游戏美术、概念艺术家、电商/产品图、Canva 生态用户 | 免费层（每日 token）+ 订阅（Fast Tokens + 滚存银行）+ 加购 token + API（按量/PAYG）+ 团队共享池 | Free **$0**（150 Fast Tokens/天）；Essential **$12/月**（8,500/月 + 25,500 滚存）；Premium **$30/月**（25,000/月 + 75,000）；Ultimate **$60/月**（60,000/月 + 180,000）（2026，`[S21]`，C 级；官网 leonardo.ai/pricing 本次抓取失败）。团队 Starter/Growth：共享 75,000 / 180,000 token `[S21]` | 体量未单独披露（`[待确认]`）。母公司 Canva：见第 11 行 | **自研**（Phoenix / Lucid Origin / Lucid Realism）+ **第三方**（FLUX、Nano Banana Pro、Veo、Kling、Sora 2 等）`[S21]` |
| 9 | **Runway** / Runway AI, Inc. / 2018 起，Gen 系列 2023 起 | 以**视频**为核心：Gen-4.5/Gen-4、Act-Two、Motion Brush、inpainting、唇形同步；图像生成（Gen-4 Images）、4K 放大、Runway MCP、自定义音色；与 Adobe Firefly 合作将其模型作为伙伴模型接入 | 影视/广告制作、专业创意工作室、 filmmakers | 订阅 + 信用分（credits）；API 信用分独立购买（$0.01/credit）；Enterprise 定制 | Free **$0**（125 一次性 credits）；Standard **$12/月**（年付，625 credits/月）；Pro **$28/月**（年付，2,250 credits/月）；Max **约 $95/月**（年付约 $76/月）（2026-10，官网 `[S6]` Standard/Pro 为 A 级；Max 数字来自 `[查证]`二级 `[S31]`） | ARR **约 $300M（2025 年末，estimate）**、**30 万+ 客户**（`[S31]`，C 级） | **自研**（Gen 系列）+ **第三方聚合**（Kling 3.0、Nano Banana Pro、Seedance 等均在界面内）`[S6]` |
| 10 | **Recraft** / Recraft, Inc. / 2022 | 文生图、**矢量（SVG）生成**（核心差异点）、Canvas 画布编辑、自然语言参考图编辑、局部修改、去背景、图像矢量化、放大、可复用 Style | 平面/品牌设计师、服装与印花、印刷、图标与插画 | 免费层（每日额度，产出公开且归 Recraft 所有，**无商用权**）+ 订阅积分 + 永不过期加购积分 + Team/Enterprise（SSO） | Free **$0**（约 50 积分/天）；Basic **$12/月**（月付）/**$10/月（年付 $120）**，1,000 积分；Pro 2K **$20/月（$16 年付）**、4K **$40（$32）**、8K **$80（$64）**、16K **$160（$128）**；Teams 2,000 积分 **$22/席/月（$18 年付）**（2026，官方 docs `[S4]`）。1 积分 = 1 张位图，矢量 = 2 积分 `[S34]` | 未披露（`[待确认]`） | **自研**（Recraft V4 / V4.1，2026-05-14 发布 V4.1）`[S34]`；有独立公开 API `[S4]` |
| 11 | **Canva Magic Studio / Magic Media（含 Dream Lab）** / Canva（悉尼）／Magic Studio 2023-10 发布 | 模板内生成、Magic Media（文生图/视频）、Magic Edit、Magic Eraser、去背景、Magic Write、Brand Kit 品牌约束、AI 可编辑图层、Affinity（收购）专业桌面套件 | 非设计师的营销/社媒/中小企业、企业内部沟通、教育 | Freemium + 订阅（Pro/Business/Enterprise）；AI 按"使用次数"分层（Standard/Premium/Ultra），非纯积分制；AI Pass 加购包（价格未公开） | 官方中文站 2026-10：**Pro US$180/年/人**；**Business US$250/年/人**；Enterprise 面议 `[S14]`（A 级；注意：多个第三方记录 Pro 为 **$15/月（月付）**，存在口径差异）。AI 额度：Pro/Teams 为免费版的 **10 倍**，Business/Enterprise 为 **20 倍** `[S14]` | ARR **约 $40 亿**（2026 年初）；MAU **2.65 亿**；估值 **$420 亿**；持有现金 $14.7 亿；2026 Q2 营收 **$9.219 亿，同比 +25.2%**（`[S15]`/`[S38]`，C 级）。2026 年将收入增速指引 **从 30% 下调至 20%** `[S15]` | **自研 + 收购（Leonardo.Ai）+ 第三方**（Stable Diffusion 系、DALL·E 等）`[S38]` |
| 12 | **Flux / Black Forest Labs（BFL）** / 德国弗莱堡 / 2024-08 成立 | 文生图、图生图、**最多 10 张参考图**、bounding-box 布局控制、像素级精确局部编辑、hex 精确配色、结构化 JSON prompt、文字渲染；开放权重授权；FLUX 3 Video | 开发者/企业（API 集成）、设计工具厂商（OEM）、自托管用户 | API 按张计费（无订阅、无席位费）+ 开放权重商业授权（Builder/Platform/Professional/Enterprise 分档）+ 合成数据授权 | FLUX 3 Image：**$0.041/张（768×768）**、**$0.048（1K）**、**$0.07（1.5K）**、**$0.10（2K）**、**$0.607（4K）**（2026-10，官网 `[S5]`，A 级；FLUX 3 于 2026-10-01 上线，10-08 前有 5 折首发价）。FLUX.2（2026-09）：[pro] 生成 **$0.03**、编辑 **$0.045**；[klein] 4B **$0.014**；[max] **$0.07**（`[S33]`，C 级）。1 credit = $0.01 `[S33]` | **Series B $300M，估值 $32.5 亿（2025-12-01）**；种子轮 **$31M（2024-08，a16z 领投）**；累计约 **$331M**（`[S13]`，B 级）。Est. Revenue $16M–$163M（Seedtable 估算，区间过大，`estimate`）`[S13]`；员工 131 人 `[S13]` | **自研**（FLUX 家族）；部分开放权重（Apache 2.0 的 klein 等）+ 商业授权 `[S5][S33]` |
| 13 | **Microsoft Designer / Image Creator** / Microsoft / Designer 2022-10 | 模板内文生图（DALL·E）、Background Remover、Generative Erase、Restyle Image；内嵌 Word / PowerPoint / Photos / Copilot；无独立 API | 泛 C 端、Microsoft 365 用户、非设计师 | **无独立付费 SKU**；免费层 + 通过 Microsoft 365 / Copilot Pro 订阅获得更多 AI 积分（与 Copilot 共享额度） | Designer 免费 **15 AI 积分/月**；Microsoft 365 Personal/Family **60 积分/月**（2026，Microsoft Support 口径 `[S23]`，C 级）。Microsoft 365 Personal 约 **$6.99/月**（第三方记录，各家口径 $6.99 / $9.99 不一，`[待确认]`）`[S23]` | 未单独披露（`[待确认]`） | **第三方**（OpenAI DALL·E 3）`[S23]`；Azure 上独立 DALL·E 服务 2026 年已停用 `[S23]` |
| 14 | **DeviantArt DreamUp** / DeviantArt（Wix 旗下）/ 2022-11 | 文生图、起始图引导（图生图）、默认放大、多次重跑、风格/画幅/负向提示词；与 DeviantArt 社区与 Sta.sh 打通；创作者可设置 noai 训练偏好 | 插画/同人/社区创作者、爱好者 | **不单独售卖**，捆绑在 DeviantArt Core 会员中；免费周额度；额外 points 购买提示词 | Free：约 **10 prompts/周（最多 30 张）**；Core+ **约 $6.67/月**（200 prompts/月，600 张）；Core Pro **约 $8.33/月**（300 prompts，1,200 张）；Core Pro+ **约 $12.50/月**（500 prompts，2,000 张）；Core Max **约 $16.67/月**（1,000 prompts，4,000 张）（2026，`[S24]`，C 级，均为年付折算价） | 未披露（`[待确认]`） | **第三方**（Stable Diffusion 系）`[S24]` |
| 15 | **NightCafe** / NightCafe Studio（澳洲）/ 2019 | 多模型聚合（Nano Banana Pro、GPT Image 2 Low、Seedream 4、FLUX 2 Dev/Klein、HiDream、Z-Image Turbo 等 50+）、社区挑战赛与画廊、赚 Relax Credits、角色一致性、批量、AI 视频 | AI 艺术爱好者、社区型创作者、轻度商用 | 免费层（每日登录送额度）+ 订阅 Fast Credits（**订阅积分按月滚存、购买积分不过期**）+ 社区赚分 | Free **$0**（约 5 积分/天）；AI Hobbyist **$12.50/月**（200 Fast Credits）；AI Enthusiast **$25/月**（500）；AI Creator **$40/月**（850）；AI Artist **$62.50/月**（1,400）（2026-09-02 核对官方页面，`[S25]`，C 级）。年付约 **6 折**（$7.49/$14.99/$23.99/$37.49 月均）`[S25]` | 未披露（`[待确认]`） | **纯第三方聚合**（不自研底模）`[S25]` |
| 16 | **SeaArt** / SUNRISEAI PTE. LTD.（新加坡）/ 2022 | 文生图、图生图、inpainting、outpainting、风格迁移、LoRA 训练（20–30 张参考图即可）、ComfyUI 风格节点工作流、70 万+ 社区模型、视频、AI 角色聊天、MCP & CLI | 二次元/风格化插画、社媒创作者、中小商家 | 免费层（每日 Stamina 重置）+ SVIP 订阅（按日 Stamina）+ 算力充值（credits 有期限） | Free **130 Stamina/天**；Beginner SVIP **$5.99/月**（300/天）；Standard SVIP **$29.99/月**（700/天）；Professional SVIP **$59.99/月**（2,100/天）；Master SVIP **$149.99/月**（3,500–100,000/天）（2026，`[S26]`，C 级，引自 seaart.ai）。标准图约 6 Stamina/张 `[S26]` | 未披露（`[待确认]`）；平台侧：70 万+ 用户共享模型 `[S26]` | **第三方为主**（Stable Diffusion 系、FLUX、GPT Image、Seedream、Qwen Image）+ 社区 LoRA `[S26]` |

### 1.2 定价与计量单位对照表（补充视角）

| 产品 | 计量单位 | 单位是什么 | 是否滚存 | 免费层 | 年付折扣 | 来源 |
|---|---|---|---|---|---|---|
| Midjourney | Fast GPU 小时 | 算力时间（非张数） | 否 | **无** | 20% | `[S1]` |
| Adobe Firefly | 生成式积分 | 标准功能付费档不限量，高级功能计分 | 否 | 有（每日额度） | — | `[S2][S35]` |
| Ideogram | Priority credits | 按模型×渲染档位计分 | 订阅分否；加购分可结转 | 有（每周） | ~25–33% | `[S3]` |
| Leonardo.Ai | Fast Tokens | GPU 负载（非固定每张） | 有（Token Bank 滚存） | 有（150/天） | ~20% | `[S21]` |
| Recraft | credits | 1 积分 = 1 张位图 / 2 张矢量 | 否（加购分永不过期） | 有（~50/天，无商用权） | ~20% | `[S4][S34]` |
| Runway | credits | 按模型×秒数/张数 | 否 | 有（125 一次性） | 20% | `[S6]` |
| SeaArt | Stamina（日） + Credits（买断） | 日重置 Stamina；算力充值有期限 | Stamina 不累积 | 有（130/天） | 20–30% | `[S26]` |
| NightCafe | Fast Credits / Relax Credits | 订阅分 + 社区赚分 | **是（滚存）** | 有（~5/天） | ~40% | `[S25]` |
| OpenAI（API） | tokens | 图像输出 token | — | 无（API） | — | `[S7]` |
| Google（API） | 输出 token / 按张折算 | 1K-2K=1,120 tokens；4K=2,000 tokens | — | **图像模型无免费层** | — | `[S19]` |
| BFL（API） | 按张（按分辨率档） | 参考图与 prompt 不额外收费；失败/被拦截不计费 | — | 无 API 免费层 | — | `[S5]` |
| Canva | AI 使用次数（非积分） | Standard/Premium/Ultra 三档 | — | 有 | — | `[S14]` |
| Microsoft Designer | AI credits | 与 Copilot 共享 | 否 | 有（15/月） | — | `[S23]` |

---

## 2. 逐产品要点

### 2.1 Midjourney
- 商业模式是**唯一一个「无免费层 + 纯订阅 + 零外部融资」**的主流玩家；付费门槛从 $10/月起，且**年营收超 $1M USD 的公司被强制要求购买 Pro 或 Mega** `[S1]`（hard_fact）。
- 计量单位是「Fast GPU 小时」而不是张数：Basic 3.3 小时 / Standard 15 / Pro 30 / Mega 60；额外 **$4/小时**；Standard 起 Relax 模式无限出图，Pro/Mega 起含 SD 视频无限 + Stealth 私有 `[S1]`。
- ARR **$500M–600M（2026，estimate）**，员工约 40–60 人，**融资 $0** `[S16]` —— 人均产出是行业极端值，但该数字来自 Sacra 等第三方估算，**非官方披露**（`estimate`，C 级）。
- 2026-07-24 宣布收购占星 App **Co-Star（430 万 MAU）**，金额未披露，Co-Star 约 24 人团队加入，创始人 Banu Guler 任首席设计官；Bloomberg 首报、The Verge 确认 `[S17]`（B 级）。这是 Midjourney 史上首笔收购，指向"从模型提供方转向自有 C 端分发"。
- 模型：自研 V7 / V8.x / Niji；**不开源、不提供公开 API**（与 BFL、Stability 相反）`[S36]`。

### 2.2 Stable Diffusion / Stability AI
- 2026-08-25 完成 **$76M Series B，累计融资 $232M**；投资方为环球音乐、索尼音乐、华纳音乐、EA、AMD Ventures、Pacific Alliance Ventures `[S11]`（hard_fact，TechCrunch）。
- 战略从"开源权重分发"转向"面向娱乐行业的创意生产 + 专业服务"：与 UMG/EA（2025-10）、Warner（2025-11）签共同开发协议；英国 Getty 版权案基本胜诉，美国案仍在审 `[S11]`。
- ARR **约 $90M（2026，estimate）** `[S27]`；**估值数据自相矛盾**：一处称约 $28 亿 `[S32]`，另一处称 down round 后约 $3 亿 `[S27]`，均为 C 级 → `[待确认]`。
- 商业使用门槛：年营收 >$1M 需企业许可 `[S27][S32]`（C 级）。

### 2.3 ComfyUI
- 2026-04-25 宣布 **$30M 融资、估值 $5 亿、累计 $47M**（Craft Ventures 领投，Pace Capital、Chemistry、TruArrow 参投）`[S12]`（官方博客，A 级）。
- 官方披露体量：**400 万用户、60,000+ 社区节点、150,000+ 日下载** `[S12]`（hard_fact）。
- 定位是**编排层/基础设施而非模型商**：工作流以 JSON 保存、可版本化、可分享；已成为"ComfyUI artist"这一职位名称 `[S12]`。
- 明确承诺**永久开源**，资金投向 Comfy Cloud 与协作功能 `[S12]`。

### 2.4 Adobe Firefly（含 Photoshop Generative Fill）
- 时间线：2023-03-21 公测 → 2023-05 Generative Fill 进 Photoshop beta → 2023-09-13 商业发布 `[S28]`。训练数据为 Adobe Stock 授权内容 + 开放授权 + 公有领域，官方定位"商用安全"，并提供企业 IP 赔付 `[S28][S35]`。
- 定价（2026-10 官网）：Standard **$9.99/月（2,000 积分）**、Pro **$19.99/月（4,000）**、Pro Plus **$49.99/月（10,000）**、Premium **$199.99/月（50,000 + Firefly Video Model 无限）** `[S2]`（hard_fact）。
- 关键结构性设计：**付费档对"标准生成"（含 Generative Fill）不限量**，积分只用于视频/音频/伙伴模型等"高级功能" `[S2][S35]`（hard_fact）。
- 体量：Firefly ending ARR **接近 $3 亿**（FY26 Q2，官方）`[S10]`；Adobe 整体 AI-first ARR **>$6.5 亿、同比 +>150%**（FY26 Q3）`[S9]`；创意类免费 MAU **破 1 亿、同比 +>70%** `[S9]`。
- 生态已从"自研模型"转为"自研 + 第三方伙伴模型（Google/OpenAI/Runway/ElevenLabs/Topaz）"的**模型超市** `[S2][S35]`。

### 2.5 OpenAI GPT Image 2 / ChatGPT 图像
- API 定价（2026-10 官方）：GPT-Image-2 图像输入 **$8.00/1M tokens**、缓存输入 **$2.00/1M**、输出 **$30.00/1M tokens** `[S7]`（hard_fact）。
- ChatGPT 订阅（2026-10 官方）：Free **$0** / Go **$8/月** / Plus **$20/月** / Pro **起价 $100/月** `[S8]`（hard_fact）。图像额度在免费档受限，Thinking Mode 需付费档 `[S37]`。
- 单张成本估算：1024² 约 **$0.006（低质量）–$0.21（高质量）** `[S37]`（estimate，C 级）。
- 定位差异：先推理 + 联网校准再出图，因此慢（第三方基准平均约 109 秒/张）`[S37]`（C 级）。

### 2.6 Google Imagen / Nano Banana（Gemini 图像）
- C 端体量：**Gemini App 9 亿 MAU（2026-05）**，`Nano Banana 系列累计生成超 500 亿张图` `[S18]`（Google I/O 2026 数据，经两家媒体转述，B/C 级）。
- API 定价：Nano Banana Pro **1K/2K 每张 $0.134、4K $0.24**；Batch/Flex **$0.067 / $0.12**；**图像模型无免费 API 层** `[S19]`（三家二级来源一致引用 Google 官方定价页，C 级，见薄弱清单）。
- 产品分层：Nano Banana 2（Gemini 3.1 Flash Image，Gemini App 内免费默认）、Nano Banana 2 Lite、Nano Banana Pro（Gemini 3 Pro Image，4K 旗舰，需订阅或付费 API）`[S19][S20]`。
- 核心能力差异点：**最多 5 个角色 + 14 件物品跨生成一致性**、参考图 6 物体/5 角色/3 风格 `[S19][S20]`。
- C 端订阅：Google AI Plus **$4.99/月**、Pro **$19.99/月**、Ultra **$99.99 或 $199.99/月**；**只有 Ultra 去除可见 Gemini 水印**，SynthID 不可见水印全档保留 `[S20]`（C 级）。

### 2.7 Ideogram
- 定价（2026-10 官方）：Plus **$20/月（年付 $15/月，$180/年）含 2,400 积分/月**；Pro **$60/月（年付 $42/月，$504/年）含 7,500 积分/月**；Team **$30/用户/月（年付 $20/用户/月）含 3,600 积分/用户/月**；Enterprise 含"用你的视觉数据训练私有定制模型" `[S3]`（hard_fact）。
- 积分消耗按模型×渲染档明码标价，例如 Ideogram 4.5：Very Low 0.8 / Low 3 / Medium 6 / High 10 / High(带源图) 22 积分每张 `[S3]`（hard_fact）——**是少数公开逐操作成本的厂商**。
- 差异化功能：**Batch Generation（上传表格批量出图）**、Character Reference（单图即可角色一致性）、Magic Fill `[S3]`。
- 体量：累计融资 **$96.5M**（a16z 领投 $80M Series A）；ARR **$7M（2025-09，estimate）**，团队 49 人 `[S29]`（C 级）。

### 2.8 Leonardo.Ai
- **2024-07 被 Canva 收购** `[S22]`（多家二级来源一致，收购金额一处记为 **$370M** `[S38]`，`[待确认]`）。
- 定价（2026）：Free 150 Fast Tokens/天；Essential **$12/月**（8,500/月）；Premium **$30/月**（25,000/月）；Ultimate **$60/月**（60,000/月）`[S21]`（C 级；官网本次抓取失败）。
- 关键机制：**Token Bank 滚存**（Essential 25,500 / Premium 75,000 / Ultimate 180,000）；**unlimited relaxed generation 仅对第一方模型生效**（Phoenix、Lucid Origin/Realism、FLUX Dev/Schnell），第三方模型（Nano Banana Pro、Veo、Kling、Sora 2）始终扣 Fast Tokens `[S21]`。
- 面向游戏美术：**Personal AI models 训练槽位**（Essential 10 / Premium 20 / Ultimate 50）`[S21]`。

### 2.9 Runway
- 官网（2026-10）口径：Free **125 一次性 credits**；Standard **$12/月（年付，625 credits/月）**；Pro **$28/月（年付，2,250 credits/月）**；站点标题为 "AI Image and Video Pricing from $12/month" `[S6]`（hard_fact）。
- 官网明确把 credits 换算成产出："625 credits monthly = 52s of Gen-4.5, 104s of Gen-4 Turbo, or 78 Gen-4 Images (1080p)" `[S6]`（hard_fact）——**定价即成本透明化**。
- 已从"纯自研视频模型"转向**多模型聚合界面**：Gen-4.5、Kling 3.0、Nano Banana Pro、Seedance 2.5、Topaz 并列 `[S6]`（hard_fact）。
- 商业模式延伸：与 Adobe 合作，其 Gen-4.5 作为伙伴模型进入 Firefly `[S2][S31]`。
- ARR **约 $300M（2025 年末，estimate）**，30 万+ 客户 `[S31]`（C 级）。

### 2.10 Recraft
- 官方 docs 定价（2026）：Basic **$12/月（月付）/ $10/月（年付 $120）含 1,000 积分**；Pro 按积分包分档 2K **$20（$16）**、4K **$40（$32）**、8K **$80（$64）**、16K **$160（$128）**；Teams 2,000 积分 **$22/席/月（$18 年付）** `[S4]`（A 级）。
- 计量最干净：**1 积分 = 1 张位图，矢量/SVG = 2 积分，Creative Upscale = 20 积分** `[S34]`（C 级）。
- **商用权设计最激进**：免费层产出"归 Recraft 所有"、公开可见、**不可商用**；付费档才给完整所有权与商用权，且订阅结束后仍保留 `[S34]`（C 级）——主流厂商中唯一在免费层这样限制的。
- 差异化：真 SVG 矢量输出（非位图近似），按 Basic $12 档折算约 **$0.04/张矢量**（2026，`[S34]`，estimate）。

### 2.11 Canva Magic Studio / Magic Media
- 官方中文站（2026-10）价格：**Pro US$180/年/人**，**Business US$250/年/人**，Enterprise 面议；AI 额度用"倍数"表述——Pro/Teams 为免费版 **10 倍**，Business/Enterprise 为 **20 倍** `[S14]`（A 级）。
- AI 不是积分制而是**三档使用次数**（Standard / Premium / Ultra），Ultra 档最稀缺 `[S38]`（C 级）。
- 体量：**ARR 约 $40 亿（2026 年初）**、**MAU 2.65 亿**、估值 **$420 亿**、2026 Q2 营收 **$9.219 亿（+25.2% YoY）** `[S15][S38]`（C 级）。
- 重要信号：2026 年**主动把收入增速指引从 30% 下调到 20%**，官方理由是"宁可放慢产品发布，也不以不可持续的单位经济性上线 AI 功能"；同期宣称通过自研模型 + 收购把 **AI 服务成本降低约 90%**，图像模型运行成本为同级别前沿模型的 **1/30** `[S15]`（C 级）。

### 2.12 Flux / Black Forest Labs
- 融资：**Series B $300M，估值 $32.5 亿（2025-12-01）**；种子轮 $31M（2024-08，a16z 领投）；累计约 $331M；投资方含 Salesforce Ventures、a16z、NVIDIA、Canva、Figma、Adobe、AMD、Temasek、Shutterstock 等 `[S13]`（B 级）。
- API 定价（2026-10 官网，A 级）：FLUX 3 Image **$0.041/张（768）**、**$0.048（1K）**、**$0.07（1.5K）**、**$0.10（2K）**、**$0.607（4K）**；参考图与 prompt 不额外收费，失败/被拦不计费 `[S5]`。
- **无订阅、无席位费，纯按张计费**："No subscriptions, no seat fees. Only pay for what you generate." `[S5]`（hard_fact）。
- 双轨变现：API 按量 + **开放权重商业授权**（Builder 10K 张/月 / Platform 100K 张/月 / Professional / Enterprise）+ 合成数据授权 `[S5]`。
- 定位是**上游模型供应商**：其模型为 Meta、Canva、Adobe、Microsoft、Picsart 等提供底层图像能力 `[S30]`（C 级）。

### 2.13 Microsoft Designer
- **无独立付费 SKU**：免费 **15 AI 积分/月**；Microsoft 365 Personal/Family 提升到 **60 积分/月**（与 Copilot 共享额度）；Microsoft 365 Basic 不含 `[S23]`（C 级，引自 Microsoft Support）。
- 底层为 **OpenAI DALL·E 3**（第三方），Azure 上的独立 DALL·E 服务 2026 年已停用 `[S23]`。
- 免费层导出**无水印**，且 Office 生态原生嵌入（Word/PowerPoint/Photos）是核心价值 `[S23]`。

### 2.14 DeviantArt DreamUp
- **不单独售卖**，捆绑在 DeviantArt Core 会员里；免费约 **10 prompts/周（最多 30 张）**，付费档按 prompt 数分档 `[S24]`（C 级）。
- 底层为 **Stable Diffusion 系第三方模型**；提供创作者 `noai` 标签与训练偏好控制，是"伦理/权益"定位的差异化点 `[S24]`。
- 无公开 API `[S24]`。

### 2.15 NightCafe
- 定价（2026-09-02 对官方页面核对）：Free 约 **5 积分/天**；AI Hobbyist **$12.50/月（200）**、AI Enthusiast **$25/月（500）**、AI Creator **$40/月（850）**、AI Artist **$62.50/月（1,400）**；年付约 6 折 `[S25]`（C 级）。
- 双积分设计：**Fast Credits（买/订阅）+ Relax Credits（社区活动赚）**；**订阅积分按月滚存、购买积分永不过期** `[S25]`。
- 定位是**多模型聚合器**（50+ 模型：Nano Banana Pro、GPT Image 2 Low、Seedream 4、FLUX 2 Dev/Klein、HiDream、Z-Image Turbo），不自研底模 `[S25]`。

### 2.16 SeaArt
- 定价（引自 seaart.ai，2026）：Free **130 Stamina/天**；Beginner SVIP **$5.99/月（300/天）**、Standard **$29.99（700/天）**、Professional **$59.99（2,100/天）**、Master **$149.99（3,500–100,000/天）** `[S26]`（C 级）。
- 双轨：Stamina（日重置、不累积） + 算力充值 Credits（2026-04 起购买的可用两年）`[S26]`。
- 生态壁垒：**70 万+ 社区共享模型/LoRA**，LoRA 训练门槛低至 20–30 张参考图；内置 ComfyUI 风格节点工作流 `[S26]`。

---

## 3. 本轮发现的「可下注的判断」

### 判断 1：这个赛道已经分化为三种截然不同的商业模式，选错模式比做错功能更致命
证据：Midjourney 卖"算力时间"（Fast GPU 小时，$10–$120/月，**无免费层**）`[S1]`；Adobe 卖"积分 + 不限量标准功能"（付费档 Generative Fill 不限量，积分只管视频/音频/伙伴模型）`[S2][S35]`；BFL 卖"纯按张"（"No subscriptions, no seat fees"，$0.041–$0.607/张）`[S5]`。三种模式的单位经济性、留存曲线、可预测性完全不同。
→ **可下注**：面向 C 端/专业创作者的图像产品，2026 年的定价主战场已从"每月多少钱"转移到"计量单位是什么"（时间 / 积分 / 张 / 使用次数）。PM 面试里能讲清"为什么 Midjourney 用 GPU 小时而 Ideogram 用积分"是分水岭。

### 判断 2：「免费层是否有商用权」正在成为最锋利的分层刀，而不是「免费层有多少张」
证据：Recraft 官方口径明确免费层产出"归 Recraft 所有"、公开可见、不可商用，付费档才给完整所有权 `[S34]`；Leonardo.Ai 免费层生成内容公开且平台保留更宽使用权，私有化从 Essential（$12/月）开始 `[S21]`；Midjourney 则更极端——**完全没有免费层**，且年营收 >$1M 的公司必须买 Pro/Mega 才拥有商用权 `[S1]`。
→ **可下注**：对 B 端/商用场景，商用权与私有化（Stealth）比生成张数更能驱动付费升级。这是把免费用户转成付费用户最有效的一根杠杆。

### 判断 3：纯模型层正在被商品化，价值向上（工作流）和向下（分发）两端迁移
证据一（向下=分发）：Canva 2.65 亿 MAU、ARR 约 $40 亿 `[S15][S38]`；Gemini App 9 亿 MAU、Nano Banana 累计生成 500 亿+ 张 `[S18]`；Midjourney 用 $0 融资做到估算 $5–6 亿 ARR 后，2026-07 反过来收购一个 430 万 MAU 的 C 端 App（Co-Star）来获取"产品与设计的组织能力" `[S17]`。
证据二（向上=工作流）：ComfyUI 以 400 万用户、6 万+ 节点拿到 **$5 亿估值** `[S12]`；Adobe 推出 Firefly Graph 节点式工作流并对标准节点提前标价 `[S35]`。
→ **可下注**：模型质量本身不再是护城河（BFL 的模型同时供给 Meta、Canva、Adobe、Microsoft `[S30]`）。护城河在"用户每天打开的那个入口"和"可复用/可版本化的工作流"上。这也是 BFL 选择纯 API + 开放权重授权、不自己做 C 端产品的原因 `[S5]`。

### 判断 4：AI 功能的单位成本已经在倒逼产品决策，2026 年出现了公开的「主动降速」案例
证据：Canva 在 2026 Q2 投资者更新中把全年收入增速指引 **从 30% 下调到 20%**，CEO 表述为"宁可放慢产品发布节奏，也不以不可持续的单位经济性上线 AI 功能"；同期称通过自研模型 + 收购把 **AI 服务成本降低约 90%**，图像模型成本为同类前沿模型的 **1/30** `[S15]`。对比 Adobe：创意类免费 MAU 破 1 亿（+>70% YoY），但付费转化要到 FY2027 才见分晓 `[S9][S10]`。
→ **可下注**：2026 年 AI 绘画产品的核心 KPI 正在从"MAU / 生成量"切换到"每次 AI 调用的成本"和"免费→付费转化率"。任何只报生成量、不报单位成本与转化率的产品叙事都不可信。

### 判断 5：聚合器（模型超市）是一条被验证的独立生意，且定价能力来自"选择权"而非模型质量
证据：NightCafe 在同一界面提供 50+ 模型（Nano Banana Pro、GPT Image 2、Seedream 4、FLUX 2、HiDream、Z-Image Turbo）`[S25]`；Runway 界面内并列 Gen-4.5、Kling 3.0、Nano Banana Pro、Seedance 2.5 `[S6]`；Adobe Firefly 直接把 Google、OpenAI、Runway、ElevenLabs、Topaz 列为"伙伴模型"并用积分计费 `[S2][S35]`；SeaArt 聚合 70 万+ 社区模型 `[S26]`。
→ **可下注**：当单点模型能力趋同（LMArena 榜首每月易主），"同一 prompt 跨模型比稿"本身就是付费理由。这条路的成本风险是：伙伴模型被计为"高级功能"要消耗积分，用户感知成本会随模型涨价而失控（Adobe 的积分制正是这么设计的 `[S35]`）。

---

## 4. 来源清单表

| # | 来源名 | 类型 | 等级 | URL | 直接引文（原文） |
|---|---|---|---|---|---|
| S1 | Midjourney 官方文档《Comparing Midjourney Plans》 | 官方文档 | **A** | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans | "Monthly Price $10 $30 $60 $120 … Annual Price $96 ($8 / month) $288 ($24 / month) $576 ($48 / month) $1,152 ($96 / month) … Fast GPU Time 3.3 hr/month (200 minutes) 15 hr/month 30 hr/month 60 hr/month … Purchase Extra GPU Time $4/hr … You must purchase the Pro or Mega plan if you are a company making more than $1,000,000 USD in gross revenue per year." |
| S2 | Adobe 官方《Compare Firefly plans》 | 官方定价页 | **A** | https://www.adobe.com/products/firefly/plans.html | "Adobe Firefly Standard: US$9.99/mo — 2,000 generative credits … Adobe Firefly Pro: US$19.99/mo — 4,000 … Adobe Firefly Pro Plus: US$49.99/mo — 10,000 … Adobe Firefly Premium: US$199.99/mo — 50,000 generative credits plus unlimited Adobe Firefly Video Model access. All paid plans include unlimited standard image and vector generations." |
| S3 | Ideogram 官方 Pricing 页（2026-10-12 WebFetch 复核） | 官方定价页 | **A** | https://ideogram.ai/pricing | "Plus plan … $20 $15 per month, $180 billed annually … 2,400 credits/mo"; "Pro plan $60 $42 per month, $504 billed annually … 7,500 credits/mo"; "Team plan $30 $20 per user/month, billed annually … 3,600 credits/user/mo"; "Enterprise … Private custom models trained on your visual data"; "4.5 … Low 3 credits / 1 image … High 10 credits / 1 image" |
| S4 | Recraft 官方文档《Paid plans》 | 官方文档 | **A** | https://recraft.mintlify.dev/docs/plans-and-billing/paid-plans | "The Basic plan starts at: $12 per month (billed monthly) for 1,000 credits; $10 per month (billed annually, $120 per year) for 1,000 credits … 2000 credits — $20 per month (monthly) or $16 per month (billed annually) … 16000 credits — $160 per month (monthly) or $128 per month (billed annually) … All paid plans include private image generation and commercial usage rights while subscribed." |
| S5 | Black Forest Labs 官方 Pricing 页 | 官方定价页 | **A** | https://bfl.ai/pricing | "Pay as you go … FLUX 3 Image $0.041/img $0.048/img $0.07/img $0.10/img $0.607/img"; "No subscriptions, no seat fees. Only pay for what you generate."; "Rejected requests, failed generations and outputs withheld by moderation are not charged."; "Open Weights Licensing … Builder … 10K images / month … Platform … 100K images / month" |
| S6 | Runway 官方 Pricing 页（2026-10-12 WebFetch 复核） | 官方定价页 | **A** | https://runwayml.com/pricing | "AI Image and Video Pricing from $12/month"; "Free … 125 one-time credits"; "Standard … $12 … 625 credits/mo … 625 credits monthly = 52s of Gen-4.5, 104s of Gen-4 Turbo, or 78 Gen-4 Images (1080p)"; "Pro … $28 … 2250 credits/mo"; 模型并列 "Gen-4.5 / Kling 3.0 / Nano Banana Pro" |
| S7 | OpenAI 官方 API Pricing 页 | 官方定价页 | **A** | https://openai.com/api/pricing | "GPT-Image-2 State-of-the-art image generation model. Price Image: $8.00 / 1M tokens for inputs $2.00 / 1M tokens for cached inputs $30.00 / 1M tokens for outputs Text: $5.00 / 1M tokens for inputs $1.25 / 1M tokens for cached inputs" |
| S8 | OpenAI 官方 Pricing 页（简体中文版） | 官方定价页 | **A** | https://openai.com/pricing | "免费版 … US$0 /月"; "Go 扩展访问权限 US$8 /月"; "Plus … US$20 /月"; "Pro 大幅提升工作效率 起价 US$100 /月" |
| S9 | Adobe Q3 FY2026 Earnings Call Transcript（官方 IR PDF，2026-09-10） | 财报/官方 | **A** | https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/adbe-q3fy26-transcript.pdf | "Adobe reported a strong third quarter, achieving \$6.76 billion in revenue, representing 12% year-over-year growth."; "used by over 1 billion monthly active users across all businesses … with the creative freemium MAU crossing 100 million and growing greater than 70% year-over-year"; "AI-first ending ARR now exceeding \$650 million and growing more than 150% year-over-year" |
| S10 | Adobe FY26 Q2 Earnings script and slides（官方 IR PDF） | 财报/官方 | **A** | https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/11606202/c5y6yteraf.pdf | "Firefly ending ARR, including Firefly apps and credit plans and Enterprise Firefly offerings, approaching \$300 million"; "Creative freemium MAU … crossed 90 million, growing >70% Y/Y" |
| S11 | TechCrunch《Stability AI … raises $76 million in fresh funding》（2026-08-25） | 头部科技媒体 | **B** | https://techcrunch.com/2026/08/25/stability-ai-maker-of-image-generator-stable-diffusion-raises-76-million-in-fresh-funding/ | "has raised $76 million in Series B funding. The new haul brings the company's fundraising total to $232 million."; "Universal Music Group, Sony Music Group, Warner Music Group, and gaming giant Electronic Arts (EA) … AMD Ventures and Pacific Alliance Ventures" |
| S12 | ComfyUI 官方博客《ComfyUI raises $30M…》（2026-04-25） | 官方公告 | **A** | https://blog.comfy.org/p/comfyui-raises-30m-to-scale-open | "We're announcing a $30 million financing at a $500 million valuation, bringing our total funding to $47 million. The round was led by Craft…"; "That community now spans 4 million users, 60,000+ nodes built by contributors, and 150,000+ daily downloads." |
| S13 | EU-Startups / Seedtable 关于 BFL Series B | 行业媒体 / 数据库 | **B** | https://eustartups.news/black-forest-labs-raises-300-million-series-b-at-3-25-billion-valuation ; https://seedtable.com/companies/black-forest-labs | "secured $300 million in Series B funding at a valuation of $3.25 billion"; Seedtable: "raised a $300M Series B in December 2025 from investors including Andreessen Horowitz, NVIDIA and Temasek Holdings … Total Funding 331.0M USD" |
| S14 | Canva 官方定价页（简体中文，2026-10-12 抓取） | 官方定价页 | **A** | https://www.canva.com/pricing/ | "US$ 180 /年(每人)"（Pro）；"每人US$250/年"（商业版）；"AI 使用次数为Canva可画免费版的10倍（适用于Standard AI、Premium AI、UltraAI）"；商业版 "20倍"；企业版 "让我们聊聊吧" |
| S15 | Crypto Briefing 报道 Canva Q2 2026 投资者更新 | 中小媒体 | **C** | https://cryptobriefing.com/canva-cuts-revenue-forecast-ai-costs/ | "revised its 2026 revenue growth forecast from 30% down to 20%"; "Canva's Q2 2026 revenue came in at $921.9 million, representing 25.2% year-over-year growth"; "closed 2025 with annual recurring revenue of roughly $4 billion … $42 billion valuation"; "slash AI servicing costs by approximately 90%" |
| S16 | Value Add VC《$500M ARR, 0 Funding — How Midjourney Works》 | 分析站（引 Sacra） | **C** | https://valueaddvc.com/blog/how-does-midjourney-make-money-500m-arr-zero-funding-and-the-ai-image-business-model-explained | "Estimates from Sacra, Product Growth, and other trackers put Midjourney's 2026 annualized revenue between $500 million and $600 million, up from roughly $300 million in 2025 and about $200 million in early 2024."; "The company does not publish official financials" |
| S17 | The Verge（经 hamidun 转述）/ AIBase / Startup Fortune 关于 Midjourney 收购 Co-Star | 头部媒体转述 | **B** | https://news.hamidun.com/en/news/12684/midjourney-kupil-astrologicheskiy-servis-co-star-pervoe-pogl ; https://www.aibase.com/news/29903 | "On July 24, 2026, Midjourney announced the acquisition of Co-Star … financial terms of the deal, which reportedly closed in spring 2026, were not disclosed"; "Co-Star has approximately 4.3 million monthly active users"; Startup Fortune: "Forbes recently listed the same headcount while saying PitchBook put its 2024 revenue at $300 million" |
| S18 | Nation Thailand（引 Google《Gemini Report: Southeast Asia 2026》）/ PC Central（引 Google I/O 2026） | 媒体/会议报道 | **B/C** | https://www.nationthailand.com/business/tech/40068657 ; https://pccentral.net/google-io-2026-13-products-1-billion-users | "Gemini currently has 900 million monthly active users worldwide."; "users in Southeast Asia have generated more than 5 billion images through the Nano Banana model"; PC Central: "The Gemini app has more than 900 million monthly active users … The Nano Banana model has generated over 50 billion images." |
| S19 | AI Tool Analysis / Novoads / AI Free API 关于 Nano Banana Pro API 定价 | 聚合/分析站 | **C** | https://aitoolanalysis.com/?p=2015/ ; https://novoads.ai/en/blog/higgsfield-vs-nano-banana ; https://www.aifreeapi.com/zh/posts/nano-banana-pro-price | "Nano Banana Pro (gemini-3-pro-image) costs $120 per 1M image output tokens on the Standard paid tier. That works out to $0.134 per 1K/2K image and $0.24 per 4K image."; "a 1K or 2K image consumes 1,120 tokens, and a 4K image consumes 2,000"; "Nano Banana Pro 這一行的 API Free Tier 顯示為 Not available" |
| S20 | Fello AI / AI Content Drop 关于 Google AI 订阅与模型 | 聚合站 | **C** | https://felloai.com/fr/nano-banana-pricing/ ; https://aicontentdrop.com/blog/nano-banana-pro-pricing-2026 | "In the Gemini app you pay through a Google AI plan at $4.99, $19.99, $99.99 or $199.99 a month."; "Google states the visible Gemini watermark is removed only for Google AI Ultra subscribers" |
| S21 | SaaS Price Hub / AI Price Compare / Knowara 关于 Leonardo.Ai 定价 | 聚合站 | **C** | https://saaspricehub.io/questions/how-much-does-leonardo.ai-cost ; https://aipricecompare.org/apps/leonardo-ai.html ; https://knowara.com/ai-tools/image/leonardo-ai-review/ | "Free: free — 150 daily tokens; Essential (formerly Apprentice): $12/month ($10/month billed annually) — 8.5K tokens/mo; Premium (formerly Artisan): $30/month … 25K tokens/mo; Ultimate (formerly Maestro): $60/month … 60K tokens/mo"; "Unlimited relaxed generation applies only to first-party models" |
| S22 | AI Price Compare 关于 Canva 收购 Leonardo | 聚合站 | **C** | https://aipricecompare.org/apps/leonardo-ai.html | "Jul 2024 Acquired by Canva for an undisclosed sum" |
| S23 | Verdict.tools / RECATOOLS / AI Compare Ninja 关于 Microsoft Designer | 聚合站（引 Microsoft Support） | **C** | https://verdict.tools/status/microsoft-designer ; https://www.aicompare.ninja/en/tool/microsoft-designer | "Microsoft 365 Personal and Family include 60 AI credits per month, used across Designer, Create, Paint, Photos and other apps. Microsoft 365 Basic does not include these AI features."; "15 free credits per month for non-commercial use" |
| S24 | AIquiks / Mac Informer / Toolify 关于 DeviantArt DreamUp | 聚合站 | **C** | http://aiquiks.com/ai-tools/dreamup ; https://macdownload.informer.com/deviantart-dreamup | "Core+ $6.67/mo … Core Pro $8.33/mo … Core Pro+ $12.50/mo … Core Max $16.67/mo"; "Generate up to 30 images using 10 prompts per week (free weekly allowance)" |
| S25 | Everyday AI Tutorials《NightCafe Review》（声明 2026-09-02 核对官方页面） | 个人/中小媒体 | **C** | https://everydayaituts.com/ai-image-tools/nightcafe-review | "Confirmed directly against NightCafe's own live pricing page, 2026-09-02 … AI Hobbyist $12.50 / AI Enthusiast $25.00 / AI Creator $40.00 / AI Artist $62.50 … 200 / 500 / 850 / 1,400 [Fast Credits]"; "Relax Credits are earned free through daily activity" |
| S26 | AI Compare Ninja 关于 SeaArt（引 seaart.ai 官方） | 聚合站 | **C** | https://www.aicompare.ninja/en/tool/seaart-ai | "Free … 130 stamina/day"; "Beginner SVIP 5.99 US$ per month … 300 stamina/day"; "Standard SVIP 29.99 US$ per month"; "Professional SVIP 59.99 US$ per month"; "Master SVIP 149.99 US$ per month"; "SUNRISEAI PTE. LTD. (SeaArt) is based in Singapore" |
| S27 | Clink ARR Leaderboard 关于 Stability AI（引 Sacra / Presenc AI） | 数据站 | **C** | https://www.clinkbill.com/arr-leaderboard/stability | "~$90M Estimated ARR, 2026"; "Company never disclosed audited revenue; third-party estimates. Sacra / Presenc AI"; "7B+ Images generated with Stable Diffusion" |
| S28 | The Verge（2023-05-23）/ Adobe 官方博客《Firefly at one》 | 头部媒体 / 官方 | **A/B** | https://www.theverge.com/2023/5/23/23734027/adobe-photoshop-generative-fill-ai-image-generator-firefly ; https://blog.adobe.com/…/firefly-at-one | The Verge: "Adobe Photoshop is getting a new generative AI tool … Generative Fill … which was released as a web-only beta in March."; Adobe 博客: "Since its introduction in March 2023 … our community has produced more than 6.5 billion images" |
| S29 | sig.ai / WifiTalents 关于 Ideogram 融资与收入 | 数据站 | **C** | https://geo.sig.ai/brands/ideogram ; https://wifitalents.com/ideogram-ai-film-industry-statistics | "Raised $96.5M. $7M ARR with 49-person team."; "Ideogram raised $80 million in Series A funding … led by Andreessen Horowitz (a16z)" |
| S30 | Startup Intros 关于 BFL 客户 | 聚合站 | **C** | https://startupintros.com/orgs/black-forest-labs | "powering production workflows for major enterprises including Adobe, Canva, Meta, Microsoft, and Picsart" |
| S31 | AI Wiki（Runway） | 类百科 UGC | **C** | https://aiwiki.ai/wiki/runway_ml/revisions/1 | "Runway hit approximately $300 million in annualized recurring revenue by late 2025, serving over 300,000 customers." |
| S32 | AIpedia 关于 Stability AI | 数据站 | **C** | https://aipedia.wiki/companies/stability-ai/ | "Founded 2019 · London, UK · ~$225M raised; reported ~$2.8B valuation (2026)"；"Free (self-host) or ~$0.03-$0.08 per API image" |
| S33 | AI Free API 关于 FLUX.2 API 定价 | 聚合站 | **C** | https://www.aifreeapi.com/en/posts/flux-1-api-comprehensive-guide | "As of September 30, 2026, FLUX.2 [pro] starts at $0.03 per image and [klein] at $0.014."; "you buy credits at $0.01 each" |
| S34 | Price Per Token / OpenTools 关于 Recraft | 聚合站 | **C** | https://pricepertoken.com/recraft-pricing ; https://dev.opentools.ai/tools/recraft | "1 credit = 1 raster image (vector/SVG images cost 2 credits)"; "Free-plan images are Recraft's property and cannot be used commercially"; "Basic costs $12 monthly or $120 billed annually and includes 1,000 credits each month" |
| S35 | Adobe 官方《生成式积分常见问题》 | 官方文档 | **A** | https://helpx.adobe.com/cn/creative-cloud/apps/generative-ai/generative-credits-faq.html | "大多数标准生成式 AI 功能（例如使用 Photoshop 中 Adobe Firefly 模型的生成式填充）每次生成使用 1 积分"; "Google、OpenAI、ElevenLabs、Topaz 等合作伙伴模型也被归类为高级功能"; "Firefly Image 5 … 每次生成消耗 10 个积分" |
| S36 | 101 AI Tools / AI Tool Radar 关于 Midjourney 版本 | 聚合站 | **C** | https://101aitools.com/guides/guides-reviews-midjourney-2026 | "The model line moved to V8.1 in April 2026 (faster generation, 2K support …)"; "All plans include access to v7, v8 alpha, the web editor, and community features." |
| S37 | IMA Wiki 关于 GPT Image 2 | UGC 聚合 | **C** | https://ima.qq.com/wiki/?shareId=e43c0cc6a169fdb4dabacc763f822ae5073c20c2c5475fc566a7ad98725a00d5 | "OpenAI 的 GPT Image 2（2026 年 4 月发布）"; "API：每张 1024² 图像 $0.006（低质量）到 $0.21（高质量）" |
| S38 | Startup Intros / Stacked Review 关于 Canva | 聚合站 | **C** | https://startupintros.com/orgs/canva ; https://stackedreview.com/canva-statistics/ | "Key Metrics (Feb 2026) ARR: $4B … Monthly Active Users: 265M (+20% YoY) … AI Tool Uses: 800M/month"; "2024 Leonardo AI Australia Leonardo AI ($370 million) was Canva's largest acquisition" |

---

## 5. 「查不到 / 证据薄弱」清单

| # | 缺口 | 当前状态 | 已尝试渠道 | 处理 |
|---|---|---|---|---|
| 1 | **Google Nano Banana 官方 API 定价页未直接打开** | 三家二级来源一致给出 $0.134 / $0.24 / $0.067 / $0.12，均称引自 Google 官方定价页 | WebFetch `ai.google.dev/gemini-api/docs/pricing` → 被 302 到 Google 账号登录页；WebSearch 三轮 | 标 **C 级 + 多源一致**，不升为 A；建议二次复核时用未登录镜像或 Google Cloud 定价页 |
| 2 | **Stability AI 估值自相矛盾** | 一处 ~$28 亿（AIpedia，C），一处 ~$3 亿 down round（Presenc，C） | WebSearch「Stability AI valuation 2026」 | `[待确认]`。**不使用该数字下结论**；只用 TechCrunch(B) 的 $76M/$232M 融资额 |
| 3 | **Stability AI 官方 API 单价** | 只有 C 级"$0.03–$0.08/张"区间 | WebSearch；未找到 stability.ai 官方 API 价目页 | `[待确认]`，标注 estimate |
| 4 | **Leonardo.Ai 官方定价页抓取失败** | 三级来源（SaaS Price Hub / AI Price Compare / Knowara）一致给出 $12 / $30 / $60 | WebFetch `leonardo.ai/pricing` → fetch failed；WebSearch 两轮 | 标 C 级；数字本身多源一致，但**未取得 A 级直引** |
| 5 | **Runway Max 档价格** | 官网 Fetch 在 Max 卡片处被截断；二级来源给 $95/月、$76/月年付 | WebFetch `runwayml.com/pricing`（截断）；WebSearch | Standard $12 / Pro $28 为 A 级；**Max 标 C 级** |
| 6 | **Canva 定价口径冲突** | 官方中文站：Pro US$180/年/人、Business US$250/年/人；第三方多处记 $15/月（月付） | WebFetch `canva.com/pricing/` → Cloudflare 错误页；WebSearch 两轮 | 采用 A 级官方中文站数字并**显式标注冲突**；AI 使用次数三档（Standard/Premium/Ultra）仅 C 级 |
| 7 | **Midjourney ARR 无官方披露** | $500–600M（2026）vs $300M（PitchBook 2024）两个量级 | WebSearch 两轮；Midjourney 零融资无披露义务 | 全部标 **estimate + C 级**；不得当 hard_fact 使用 |
| 8 | **Midjourney 上线具体日期** | 仅"2022 年以 Discord bot 公开发布"（C 级） | WebSearch；docs.midjourney.com 未找到 About/历史页 | `[待确认]` |
| 9 | **Ideogram / SeaArt / NightCafe / DeviantArt 上线时间与体量（ARR、用户数）** | 全线无官方披露 | WebSearch 各一轮 | `[待确认]`；只用可交叉验证的融资额与定价 |
| 10 | **OpenAI 图像功能的独立收入/用户数** | OpenAI 不单独披露图像收入与图像额度 | WebSearch；官方定价页只给套餐价 | `[待确认]`；GPT Image 2 发布月份（2026-04）仅 C 级来源 |
| 11 | **Comfy Cloud 具体价目** | 官方博客只说在建，未给价格 | WebFetch 官方博客 | `[待确认]` |
| 12 | **Runway ARR ~$300M / 30 万客户** | 仅 AI Wiki（类百科 UGC）单一来源 | WebSearch | `[SINGLE_SOURCE]` + estimate + C 级 |
| 13 | **BFL 营收区间 $16M–$163M** | Seedtable 自估区间，跨度 10 倍 | WebSearch | 记录但**不用于任何结论** |
| 14 | **Canva 收购 Leonardo.Ai 的交易金额** | 一处记 $370M，另一处称"未披露" | WebSearch | `[待确认]`；只保留"2024-07 被 Canva 收购"这一多源一致事实 |
| 15 | **Microsoft 365 Personal 价格口径** | 二级来源分别记 $6.99/月、$9.99/月、$99.99/年 | WebSearch | `[待确认]`；保留 Designer 免费 15 积分/月与 M365 60 积分/月（引自 Microsoft Support） |

---

### 附：本轮检索覆盖度自检

- 已覆盖（16 个）：Midjourney、Stable Diffusion/Stability AI、ComfyUI、Adobe Firefly（含 Photoshop Generative Fill）、OpenAI GPT Image 2、Google Nano Banana/Imagen、Ideogram、Leonardo.Ai、Runway、Recraft、Flux/BFL、Canva Magic Studio、Microsoft Designer、DeviantArt DreamUp、NightCafe、SeaArt。
- **增补建议（未在本次范围内展开）**：Krea、Playground AI、Freepik AI、Picsart、OpenArt、Higgsfield、Lightricks —— 若需要补齐"长尾聚合器"层，建议下一轮单独检索。
