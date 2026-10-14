# SQ4：AI 绘画产品的商业模式拆解与单位经济（unit economics）

> 调研日期（timepoint 基准）：**2026-10-12**
> 所有数字均标注 unit / timepoint / scope。`[estimate]` = 本人按公式推导，附完整假设链；`[待确认]` = 未找到可核验来源；`[SINGLE_SOURCE]` = 仅单一来源支撑。

---

## 0. 先给结论用的三句话

1. **这门生意的成本曲线在过去 24 个月被压平了两个数量级**：裸算力边际成本已降到 **$0.0002–0.005 / 张（1024², 20 steps）**，而 C 端订阅折算单张仍在 **$0.03–0.07**，云端 API 零售价 **$0.003–0.08**。价差不是技术问题，是「排队/并发/确定性/版权兜底」的定价权问题。
2. **订阅制不是被 credits 取代，而是被「订阅 + credits 双层」取代**：Adobe 把标准图做成 Unlimited、只让视频/音频/第三方模型吃积分；即梦把积分额度砍掉 33%/45%/59% 却不动月费名义价——两者都是**名义价不动、实际单价上移**。
3. **2026 年最大的塌陷不是需求侧，是供给侧 Model ID 的寿命**：OpenAI 在 14 个月内下线了 dall-e-2/3、gpt-image-1、gpt-image-1.5/mini、chatgpt-image-latest 共 6 个图像端点；Google 关停 gemini-2.5-flash-image（Nano Banana）。任何把定价锚在某个 model ID 上的产品，UE 都在裸奔。

---

## 1. 商业模式分类表

> 说明：同一产品常同时踩多个格子（如 Adobe = 订阅 + credits + 套件捆绑 + 企业私有化）。下表按**主要变现机制**归类，交叉处另注。

| # | 模式 | 机制（钱怎么进来） | 代表产品（≥2 个） | 适用用户 | 优势 | 劣势 |
|---|---|---|---|---|---|---|
| 1 | **C 端订阅（月/年）** | 固定月费换固定算力额度；年付打折 20% | Midjourney Basic/Standard/Pro/Mega（$10/$30/$60/$120 月付；$96/$288/$576/$1,152 年付，2026 官方）<br>Leonardo.Ai Apprentice/Artisan/Maestro（$12/$30/$60 月付，$10/$24/$48 年付，2026-09-25 官网）<br>美图 VIP 订阅（2026H1 VIP 订阅占总收入 79.9%） | 高频个人创作者、自由职业者 | 现金流可预测；ARPPU 可分层； churn 可见 | 重度用户吃掉毛利（「鲸鱼问题」，见 §5）；额度用尽即流失 |
| 2 | **算力积分 credits** | 订阅给基础额度 + 积分包加购；不同功能不同积分消耗 | Adobe Firefly（Standard $9.99/月 2,000 credits；Pro $19.99 4,000；Pro Plus $49.99 10,000；Premium $199.99 50,000；加购 2,000 起）<br>即梦 AI（基础/标准/高级/超级 = 725 / 2,210 / 12,320 / 54,600 积分每月；¥10 = 221–333 积分，2026 官网）<br>可灵 AI（黄金 66 元/月 660 灵感值；铂金 268；钻石 666）<br>美图「AI 算力点」（2026 Q1/Q2 消费总额环比各 +46%，半年累计 +113%） | 用量波动大、需要「按实际消耗付费」的重度用户 | 让高频用户多付钱（ARPPU 上探）；可对冲算力涨价 | 用户心智负担重；易被解读为「变相涨价」（即梦已因此被研报点名） |
| 3 | **免费 + 增值（freemium）** | 免费额度获客 → 靠去水印/商用授权/并发/加速转化 | Bing Image Creator / Microsoft Copilot Designer（免费 + 15–25 boosts，M365 Personal $9.99/月 给 100 boosts/天）<br>Leonardo.Ai（150 Fast Tokens/天，约 30–50 张/天）<br>LiblibAI 哩布哩布（免费版 50 积分/天；基础 ¥29/月 300/天）<br>Adobe Firefly Free（限量每日生成；创意类 freemium MAU 2026Q3 破 1 亿，YoY +70%） | 泛用户、低频尝鲜者 | 获客成本最低；MAU 是融资/故事指标 | 免费额度 = 纯现金流出（见 §3.4）；转化低时直接拖垮 UE |
| 4 | **API 按量售卖** | per-image / per-megapixel / per-token / per-GPU-second | fal.ai（FLUX.1 schnell $0.003/MP、dev $0.025/MP、FLUX.2 pro $0.03 首 MP、Kontext pro $0.04/张）<br>Replicate（L40S $0.000975/s、A100-80G $0.0014/s = $5.04/h、H100 $0.001525/s = $5.49/h；读于 2026-09-23）<br>OpenAI Images API（gpt-image-2 medium 1024² $0.053 / high $0.211；gpt-image-1.5 low $0.009）<br>火山引擎即梦 AI 图像生成（3.0 系列 ¥0.2/张，4.0/4.6 系列 ¥0.22/张，智能超清 ¥0.4/张） | 开发者、把生图当 feature 的 App、批量生产 | 无库存、无闲置风险；用量即收入 | 价格战最惨烈（$0.003 vs $0.08 差 26 倍）；上游模型下线即断供 |
| 5 | **企业 / 团队席位** | per-seat 定价 + 治理（SSO / 权限 / 审计）+ 商用条款 | Midjourney（年毛收入 >$1M 的公司必须买 Pro 或 Mega，官方条款）<br>Ideogram Team（$30/user/月，年付 $20/user；≥2 seats）<br>Leonardo Team Starter（$24/seat/月起，≥3 seats，75,000 共享 tokens）<br>Adobe Firefly Premium（US$199.99/月/license，50,000 credits + 无限 Firefly Video Model） | 工作室、品牌方、 agency | ARPU 高、churn 低、可叠加合规溢价 | 销售周期长；需要私有化/审计能力才卖得动 |
| 6 | **模型授权 & 私有化部署** | License 费 / 部署费 / 定制模型训练 | Stability AI：Self-Hosted License（Community License 下年营收 <$1M 免费，超阈值需 Enterprise license）；Brand Studio Enterprise（无限席位、Brand ID Models、SSO、定制报价）<br>Adobe Firefly Custom Models + IP indemnification（限企业方案）<br>通义万相（企业支持私有化 API 部署） | 金融/医疗/品牌方、数据不出域场景 | 单价最高、粘性最强、可卖「版权兜底」 | 交付重、复制性差、需要实施团队 |
| 7 | **与办公 / 设计套件捆绑** | AI 能力不作为独立 SKU，而是抬高整包价格或做留存 | Adobe Creative Cloud Pro（US$69.99/月，含 4,000 credits + 无限标准图/矢量 + 20+ App；Creative Cloud 总 ARR $27.5B）<br>Microsoft 365 Personal/Family/Premium（$9.99/$12.99/$19.99 月，100 boosts/天 + 优先队列）<br>Canva（Pro US$144/年；重度用户加购 AI Pass US$100/人/月） | 已有工作流的用户 | 获客成本≈0；AI 是涨价理由不是成本中心 | AI 成本吃掉整包毛利（Adobe 承认推迟了 CC 定价优化以换 MAU） |
| 8 | **硬件 / 云算力** | 卖 GPU 小时或整机，而非卖图 | Replicate 按秒计费（L40S $3.51/h；A100 $5.04/h；H100 $5.49/h）<br>国内算力租赁（2026-07：RTX 4090 容器时租 ¥1.96/时、裸金属月租 ¥1,500–2,500；A100 80G ¥2.8–3.5/时；H100 80G ¥5.5–6.8/时）<br>本地自建（RTX 4090 工作站一次性 $1,500–$4,000+） | 高频批量、合规不出网、技术型用户 | 边际成本趋 0；无供应商锁定 | 闲置即亏损；运维/驱动/模型转换成本自担 |
| 9 | **内容平台广告 & 流量分成** | 免费生图换流量 → 广告/电商/增值变现 | 美图（2026H1 广告收入 4.15 亿元，YoY **-4.4%**，是三大板块中唯一下降的）<br>Canva（180M+ MAU、接近 $20 亿年收入，AI 作为留存漏斗）<br>`[待确认]` 国内独立 AI 绘画平台的广告分成具体机制与抽成比例 | 大众用户 | 不受「单张成本」约束 | 生图工具天然低停留时长；美图广告已负增长，说明这条路在收缩 |
| 10 | **创作者经济（模型/作品分成）** | 平台把生成收入的一部分分给模型/LoRA 作者，或让创作者自定授权费 | **Civitai**：旧制 = 每次用你的模型生成，你拿该次 buzz 的 25%；2026-07-29 改为**创作者自定 per-generation licensing fee**（建议：base model ~1 buzz/张，LoRA ~0.1 buzz/张；区间 1 buzz/100张 ~ 100 buzz/张），旧制 2026-08-31 退役；**费用可堆叠**（微调费叠加在 base 之上）；Creator Shop 装扮销售 **创作者 70% / 平台 30%**<br>**LiblibAI**：对模型创作者有 revenue sharing<br>**Canva**：承诺数年投入 $2 亿向同意授权内容训练模型的创作者付费 | 模型训练者、LoRA 作者、风格作者 | 供给侧自增长；平台抽「基础设施税」 | 定价权下放 → 创作者间价格战（地板 1 buzz/100 张可被用来砸价）；分成池不透明，Civitai 未公开池子规模 |
| 11 | **模型/技术授权给大厂（一次性/年度）** | 不卖产品卖技术 | `Midjourney × Meta 2025 年技术授权协议（ reportedly for image/video model technology）` `[SINGLE_SOURCE]` `[待确认]`<br>Stability AI（2026-08-25 $76M B 轮，投资方含 UMG/Warner/Sony/EA；此前与 UMG 2025-10、Warner 2025-11 建立战略联盟） | 大厂补齐能力 | 单笔金额大、零边际成本 | 极难复制；依赖谈判地位 |

---

## 2. 定价带分布表

### 2.1 海外（USD，月付名义价，除非注明）

| 价格带 | 区间 | 产品 / 套餐 | Timepoint | 额度 / Scope | 来源等级 |
|---|---|---|---|---|---|
| **免费** | $0 | Bing Image Creator / Copilot Designer（15–25 boosts，口径见注 1） | 2026-04～2026-07 | 免费账号，标准速度不限量 | C（多源冲突） |
| | $0 | Leonardo.Ai Free | 2026-09-25 | 150 Fast Tokens/天（≈30–50 张/天） | B/C |
| | $0 | Adobe Firefly Free | 2026-09-20 | 限量每日生成；付费后标准图无限 | A |
| | $0 | Recraft Free（含矢量生成，SVG） | 2026 | 有限额度 | C |
| **低端** | **$8–12 / 月** | Midjourney Basic **$10**（≈3.3 fast GPU 小时） | 2026 官方文档 | 200 分钟 fast GPU/月 | **A** |
| | | Adobe Firefly Standard **$9.99** | 2026-09-20 | 2,000 credits + 无限标准图/矢量 | **A** |
| | | Leonardo.Ai Apprentice **$12**（年付 $10） | 2026-09-25 | 8,500 tokens | B/C |
| | | Recraft Basic **$12**（年付 $10） | 2026 | 1,000 credits | C |
| | | Krea Basic **$9**（年付 $5） | 2026 | 5,000 compute units | C |
| **中端** | **$19–30 / 月** | Midjourney Standard **$30**（15 fast GPU 小时 + Relax 无限图） | 2026 官方文档 | — | **A** |
| | | Adobe Firefly Pro **$19.99** | 2026-09-20 | 4,000 credits + Photoshop web/mobile | **A** |
| | | ChatGPT Plus **$20**（含图像生成，与 GPT-4o/其他用量共享配额） | 2026 | 共享配额 | B/C |
| | | Google AI Pro **$19.99**（Nano Banana 图像 + 1,000 Flow credits） | 2026 | 4× 免费额度 | C |
| | | Leonardo.Ai Artisan **$30**（年付 $24） | 2026-09-25 | — | B/C |
| | | Microsoft 365 Personal **$9.99**（100 boosts/天） | 2026-06 | 含 Office 套件 | C |
| **高端（个人/Prosumer）** | **$50–120 / 月** | Midjourney Pro **$60**（30 小时 + Stealth）、Mega **$120**（60 小时） | 2026 官方文档 | — | **A** |
| | | Adobe Firefly Pro Plus **$49.99**（10,000 credits） | 2026-09-20 | — | **A** |
| | | Ideogram Pro **$60**（年付 $42，3,500 priority credits） | 2026-07-30 | — | C |
| | | Leonardo.Ai Maestro **$60**（年付 $48） | 2026-09-25 | — | B/C |
| **团队 / 企业** | **$22–200 / seat / 月** | Adobe Firefly Premium **US$199.99/license/月** | 2026-09-20 | 50,000 credits + 无限 Firefly Video Model | **A** |
| | | Ideogram Team **$30/user/月**（年付 $20） | 2026-07-30 | ≥2 seats | C |
| | | Leonardo Team Starter **$24/seat/月**（≥3 seats，75,000 共享 tokens） | 2026-09-25 | — | C |
| | | Recraft Teams **$22/seat 起**（≥2 seats） | 2026 | — | C |
| | | Canva AI Pass **US$100/人/月**（叠加在 Pro 之上） | 2026 | 重度用户 | C |

> 注 1：Bing Image Creator 免费额度口径**多源冲突**：vantaige（2026-04）称 **15 boosts/天**；morphed（2026-04）称 **15 boosts/周**；costbench（2026-07）称 **25 boosts/周**。官方 bing.com/images/create/help 未在可抓取内容中给出明确数字 → **该数字标 `[待确认]`，不要用于任何测算。**

### 2.2 国内（CNY）

| 价格带 | 产品 / 套餐 | 价格 | 额度 | Timepoint | 来源等级 |
|---|---|---|---|---|---|
| 免费 | LiblibAI 免费版 | ¥0 | 50 积分/天 | 2026-06 | C |
| | 即梦 AI | ¥0 | 每日登录赠送积分（视频 10 秒≈60 积分、15 秒≈90 积分） | 2026 | B |
| | 可灵 AI | ¥0 | 每日 66 灵感值（≈6 条 720P） | 2026-08 | C |
| | 通义万相 | ¥0 | 网页版每日多次生成；阿里云百炼新用户约 50 张文生图 + 50 秒视频（90 天内领用） | 2026-07 | C |
| 低端 | LiblibAI 基础会员 | **¥29/月** | 300 积分/天 | 2026-06 | C |
| | 可灵 AI 黄金会员 | **¥66/月** | 660 灵感值 | 2026 | B/C（另有一源称 ¥58/月） |
| | 即梦 AI 基础会员 | 连续包月 **¥69**（年付首年 ¥393，次年 ¥659） | 725 积分/月（¥10=221 积分） | 2026 官网 / 2026-04 研报 | **A**（官网）+ B |
| 中端 | LiblibAI 专业会员 | **¥59/月** | 600 积分/天 | 2026-06 | C |
| | 即梦 AI 标准会员 | 连续包月 **¥199**（年付首年 ¥1,099/¥949，次年 ¥1,899） | 2,210 积分/月（¥10=241 积分） | 2026 官网 | **A** |
| | 通义万相标准 | **¥47/月** | 300 灵感值 | 2026-08 | C |
| | 美图 VIP（整体推算） | 月 ARPPU ≈ **¥16/月** `[estimate]` | 见 §3.5 推导 | 2026H1 | 推导自 A 财报 |
| 高端 | 即梦 AI 高级会员 | 连续包月 **¥499**（年付首年 ¥5,199，次年 ¥10,398） | 12,320 积分/月（¥10=284 积分） | 2026 官网 | **A** |
| | 即梦 AI 超级会员 | 年付首年 **¥19,656**（次年 ¥43,680） | 54,600 积分/月（¥10=333 积分） | 2026 官网 | **A** |
| | 可灵 AI 钻石会员 | **¥666/月** | 8,000 灵感值 | 2026 | B/C |
| | LiblibAI 旗舰会员 | **¥99/月** | 1,200 积分/天 | 2026-06 | C |

### 2.3 国内 API（CNY/张，按量）

| 服务 | 单价 | Timepoint | 来源等级 |
|---|---|---|---|
| 火山引擎 豆包图像创作模型 5.0（文生图/图生图） | **¥0.22/张** | 2026（官网首页） | **A** |
| 火山引擎 即梦 AI 图像生成 3.0 系列 | **¥0.20/张**（次数包 10万次 ¥18,000；50万次 ¥80,000） | 官方文档 | **A** |
| 火山引擎 即梦 AI 图片生成 4.0 / 4.6 | **¥0.22/张** | 官方文档 | **A** |
| 火山引擎 即梦 AI 智能超清 | **¥0.40/张** | 官方文档 | **A** |
| 阿里云百炼 通义万相 wan2.6-t2i / wan2.5 / wan2.2-t2i-plus | **¥0.20/张**；轻量的 wan2.2-t2i-flash **¥0.14/张** | 2026-07 | C（转述官方计费文档） |
| 硅基流动 Z-Image-Turbo | **¥0.10/张**（SDXL/Flux 部分低至 ¥0.05–0.08） | 2026 | C |
| LiblibAI API（SDXL） | **≈¥0.06/张起** | 2026 | C |

> 关键对比：国内官方图 API ¥0.14–0.22/张 ≈ **$0.020–0.031/张**（按 1 USD ≈ 7.1 CNY），与 fal.ai / Replicate 的 FLUX dev $0.025/张**基本在同一水位**——**国内并不比海外便宜**，这与「国内价格战」的直觉相反。

---

## 3. 成本与 UE 拆解（含公式）

### 3.1 GPU 云端单价（可核验报价）

| GPU | 单价（USD） | 单价（CNY） | Timepoint / 地区 | 来源等级 |
|---|---|---|---|---|
| Replicate **Nvidia T4** | $0.000225/s = **$0.81/h** | — | 2026-09-23，官方 pricing 页 | **A** |
| Replicate **Nvidia L40S** | $0.000975/s = **$3.51/h** | — | 2026-09-23 | **A** |
| Replicate **Nvidia A100 80GB** | $0.0014/s = **$5.04/h** | — | 2026-09-23 | **A** |
| Replicate **Nvidia H100** | $0.001525/s = **$5.49/h** | — | 2026-09-23 | **A** |
| Replicate **8×H100** | $0.0122/s = **$43.92/h** | — | 2026-09-23 | **A** |
| RTX 4090（Vast.ai 最低） | **$0.27/h** | — | 2026 | C |
| RTX 4090（RunPod） | $0.34–0.60/h | — | 2026 | C |
| A100 80GB（Lambda） | $1.29–2.80/h | — | 2025–2026 | C |
| H100 80GB（RunPod / Vast.ai spot） | $1.99–3.50/h | — | 2025–2026 | C |
| 国内 **RTX 4090 24GB** 容器 | — | **¥1.96/时**；裸金属 ¥1,500–2,500/月 | 2026-07，国内 | C |
| 国内 **A100 80G** | — | **¥2.8–3.5/时**；裸金属 ¥6,000–9,000/月 | 2026-07，国内 | C |
| 国内 **H100 80G** | — | **¥5.5–6.8/时**；裸金属 ¥12,000–15,000/月 | 2026-07，国内 | C |
| 国内 **H20 96G** | — | ¥6.20/时 | 2026-07 | C |
| 国内 **昇腾 910B** | — | ¥3.58/时 | 2026-07 | C |

> ⚠️ 两个口径差异极大：Replicate 官方牌价（A100 $5.04/h）是**托管 Serverless**价格；Vast.ai/RunPod spot（$0.27–2.8/h）是**裸租**价格。相差 2–10 倍。做 UE 时必须声明口径。
> 趋势：`[SINGLE_SOURCE]` 有国内来源称 2026 年以来算力租赁价格整体上涨约 30–40%，高端卡（H100/H200）供给偏紧价格微涨，中低端卡（4090/A10）走低。**方向性可信，具体幅度未获第二来源。**

### 3.2 单张图推理成本 —— `[estimate]`，三套独立公式

#### 公式 A：裸算力边际成本（最乐观，只算 GPU）

```
cost_per_image = (GPU_hourly_rate / 3600) × seconds_per_image / utilization
```

假设链：
- SDXL 1024×1024，20 steps，DPM++ 2M Karras，batch size 1
- RTX 4090 = **2.1 秒/张 → 1,714 张/小时**；A100 80GB = **1.8 秒/张 → 2,000 张/小时**；H100 = **1.5 秒/张 → 2,400 张/小时**（来源：gpucloudlist 自测基准，`[SINGLE_SOURCE]`，等级 C）
- RTX 4090 时租 $0.27/h（Vast.ai，C）；A100 $5.04/h（Replicate 官方，A）

| 场景 | 计算 | 结果 |
|---|---|---|
| RTX 4090 @100% 利用率 | $0.27 / 1714 | **$0.000158/张** |
| RTX 4090 @50% 利用率 | $0.000158 / 0.5 | **$0.00032/张** |
| RTX 4090 @25% 利用率 | $0.000158 / 0.25 | **$0.00063/张** |
| A100（Replicate 牌价）@100% | ($5.04/3600) × 1.8 | **$0.00252/张** |
| A100（Replicate 牌价）@50% | — | **$0.00504/张** |
| H100（Replicate 牌价）@100% | ($5.49/3600) × 1.5 | **$0.00229/张** |

**结论区间：裸算力边际成本 ≈ $0.0002 – $0.005 / 张（1024², 20 steps）。**
该区间跨度 25 倍，主要来自「GPU 型号 + 利用率」两个假设，二者都必须显式声明。

#### 公式 B：云端 API 采购价（若你是「套壳方」，这是你的真实 COGS）

```
COGS_per_image = 上游 API 报价（按分辨率/质量档位）
```

| 服务 / 模型 | 1024² 单价 | Timepoint | 来源等级 |
|---|---|---|---|
| fal.ai FLUX.1 [schnell] | **$0.003/MP** | 2026 | **A**（fal 官方） |
| fal.ai FLUX.2 [klein] 4B | **$0.009/MP**（输入+输出） | 2026 | **A** |
| fal.ai FLUX.2 [dev] | **$0.012/MP** | 2026 | **A** |
| fal.ai FLUX.2 [pro] | **$0.03 首 MP + $0.015/附加 MP** | 2026 | **A** |
| fal.ai FLUX.1 [dev] | **$0.025/MP**（1024²=$0.025；2048²=$0.10） | 2026 | **A** |
| fal.ai FLUX 1.1 [pro] Ultra | **$0.06/张**（原生最高 4MP） | 2026 | **A** |
| fal.ai FLUX Kontext [pro] / [max] | **$0.04 / $0.08 每张** | 2026 | **A** |
| Stability SD 3.5 Large / Ultra / Core | ≈**$0.065 / $0.08 / $0.03 每张**（1 credit = $0.01） | 2026 | C |
| BFL FLUX.2 [klein] 4B（直连） | **$0.014/张** | 2026-05-20 | C |
| OpenAI gpt-image-2 low / medium / high（1024²） | **$0.006 / $0.053 / $0.211** | 2026 官方文档 | **A** |
| OpenAI gpt-image-1.5 low / medium / high（1024²） | **$0.009 / $0.034 / $0.133** | 2026（2026-12-01 下线） | **A** |
| Nano Banana 2 Lite（Gemini 3.1 Flash Lite Image） | **$0.0336 / 1K 图** | 2026 | C |
| Nano Banana（gemini-2.5-flash-image） | **$0.039/张**（Batch $0.0195） | 2026-10-02 下线 | C |
| 火山引擎 即梦 4.0 | **¥0.22/张 ≈ $0.031** | 2026 | **A** |
| 阿里云 通义万相 wan2.6-t2i | **¥0.20/张 ≈ $0.028** | 2026-07 | C |

**结论区间：云端 API 采购价 ≈ $0.003 – $0.21 / 张**，主流区间 **$0.02–0.06**。
与公式 A 对比：**零售 API 价是裸算力成本的 10–300 倍**。这中间的差额 = 排队/弹性/利用率风险/工程/存储/失败重试/毛利。

#### 公式 C：C 端订阅折算单张（Midjourney，`[estimate]` 但输入全部来自官方）

```
implied_price_per_GPU_hour = 月费 / 套餐 fast GPU 小时
images_per_GPU_hour        = 官方 fast GPU 分钟数 / 第三方张数估计
cost_per_image             = implied_price_per_GPU_hour / images_per_GPU_hour
```

| 项 | 值 | 来源 |
|---|---|---|
| Basic 月费 | $10 | Midjourney 官方文档（A） |
| Basic fast GPU 时间 | 3.3 小时 = 200 分钟 | Midjourney 官方文档（A） |
| Basic 对应张数 | ≈200 张 | 第三方普遍口径（C），**非官方** |
| **隐含 GPU 小时捆绑售价** | $10 / 3.3 = **$3.03/GPU-小时** | 推导 |
| **加购 fast GPU 时间官方价** | **$4/小时**（全档位同价） | Midjourney 官方文档（A） |
| 单张 fast 图 GPU 消耗 | 200 分钟 / 200 张 = **1 GPU-分钟/张** = 0.0167 GPU-小时 | 推导 |
| **折算单张（捆绑价）** | $3.03 × 0.0167 = **$0.0506/张** | 推导 |
| **折算单张（加购价）** | $4 × 0.0167 = **$0.0667/张** | 推导 |

⚠️ 注意：Midjourney 的「1 GPU-分钟」是它自己的 A100/H100 级服务器的分钟，不等于 Replicate 的 $0.0014/s。Holz 公开说过 Midjourney 跑在「$20,000–$40,000 一台的 GPU 服务器」上（The Verge / PC Gamer 访谈，2022，等级 B）。所以 **$0.05/张 是 Midjourney 的收入侧折算，不是它的成本侧。**

#### 公式 D：Midjourney 的 GPU 小时收入 vs 市场 GPU 小时租金（关键 UE 判据）

```
Midjourney 每 GPU-小时的收入：$3.03（捆绑）/ $4.00（加购）      [A]
市场 A100/H100 裸租：$1.29 – 5.49 /小时                        [A: Replicate $5.04；C: Vast/RunPod $1.99–3.50]
→ 若 Midjourney 按 Replicate 牌价级别采购算力（$5.04/h），它在 Fast 通道上是**负毛利**的；
→ 只有靠 (a) 自有/长约算力、(b) Relax 模式填充闲置、(c) 全球 8 区域跨时区负载均衡（Holz 访谈，B），才能把实际单位成本压到 $3–4/h 以下。
```

**这是本报告最重要的一条可验证推论**：Midjourney 之所以必须做 Relax Mode（官方：Standard 及以上无限 Relax 图，使用共享 GPU 空闲容量），不是产品体验设计，**是 UE 强制约束**——把不可售卖的闲置 GPU 时间以「无限但慢」的形式变现。

### 3.3 免费额度的成本敞口 `[estimate]`

```
月成本敞口 = 每日免费张数 × 30 × 单张采购价（公式 B）
```

| 产品 | 免费额度 | 折算张数/天 | 单张采购价假设 | 月敞口 | 来源等级 |
|---|---|---|---|---|---|
| Leonardo.Ai Free | 150 Fast Tokens/天 | 30–50 张 | $0.025（fal FLUX.1 dev，A） | **$22.5 – $37.5 / 用户 / 月** | 额度 B/C + 单价 A |
| LiblibAI Free | 50 积分/天 | 15–25 张 | ¥0.06（Liblib SDXL API，C） | **¥27 – ¥45 / 用户 / 月** | C |
| Adobe Firefly Free | 限量每日生成；**付费后标准图无限** | 未知 | — | `[待确认]` | A（存在性）/ 量 `[待确认]` |
| Bing Image Creator | 见 §2.1 注 1，口径冲突 | `[待确认]` | — | `[待确认]` | C + 冲突 |

> **PM 含义**：免费额度的成本敞口（$20–40/用户/月）**高于多数产品的入门订阅价**（$8–12/月）。这意味着：免费额度只有在其转化贡献 > 直接售卖时才成立；一旦转化率低于阈值，免费额度本身就是最大的成本项。这解释了为什么 2023–2026 年间所有玩家都在**收缩**免费额度（见 §6）。

### 3.4 训练 vs 推理的成本结构

**唯一可核验的公开口径**（David Holz，2023 年访谈，等级 B）：
> 「我们云成本的 10% 用于训练，90% 用于用户制作图像的推理。几乎所有的成本都在制作图像上。」（CSDN 转载的 The Verge/Stratechery 系访谈中文版）

Holz 同时给出训练成本量级（2022，等级 B）：
> 「Training image models is probably around $50,000 every time you do it right now. And you never get it right in one try, so you have to use three tries or 10 tries or 20 tries.」

⚠️ 这是 **2022 年 timepoint** 的口径，不能直接用于 2026 的前沿模型训练成本。2026 年单次前沿图像模型训练成本 → `[待确认]`。

### 3.5 毛利 / 单位经济 —— 公开数字

| 主体 | 指标 | 数值 | Unit / Timepoint / Scope | 来源等级 |
|---|---|---|---|---|
| **Midjourney** | 收入 | **2023 年 >$200M；2024 年 $300M** | USD / 日历年 / 公司整体（**原告在起诉状中的主张**） | **A**（法院文件，经 UPI / Media Play News / Entrepreneur / Legal500 报道） |
| Midjourney | 收入 | 2022 年 $50M | USD / 2022 / 公司整体 | B/C（Entrepreneur 转述起诉状） |
| Midjourney | 用户 | 约 2,100 万 users（**非付费订阅数**） | 截至 2024-09 | A（起诉状，经 Legal500） |
| Midjourney | 是否盈利 | Holz 称 2022-08 已盈利；**利润率/毛利数字从未公开** | — | B（访谈）/ 幅度 `[待确认]` |
| Midjourney | 2025–2026 收入 | 流传的 **$500M–600M ARR** | 2026 年中 | ⚠️ **第三方建模值，非申报值**。provenstartups 明确批评：「Sites take the 2024 figure, apply an invented growth rate, and publish a 2025 or 2026 run rate with no new evidence behind it.」→ **面试中引用必须声明为 estimate，不得当事实** |
| Midjourney | 融资 | **$0 外部融资**（自筹） | 截至 2026-06 | B（多源） |
| **Adobe** | AI-first ARR | **>$650M，YoY +150%** | USD / FY2026Q3 期末（截至 2026-08-28） | **A**（Adobe 财报电话会） |
| Adobe | 总 ARR | **$27.50B**，YoY +11.2% | USD / FY2026Q3 期末 | **A**（SEC 8-K） |
| Adobe | **Firefly ARR** | Q2 FY26「**approaching $300 million**」（含 Firefly App + credit packs + Enterprise Firefly）；Q3 FY26 **环比 +40%** | USD / 2026-05-29 与 2026-08-28 | **A**（Adobe 官方 earnings script + transcript） |
| Adobe | AI-first ARR 占总 ARR | **≈2.4%** `[estimate]` = $650M / $27.5B | 2026-08-28 | 推导自 A |
| Adobe | AI 影响型 ARR | >$50 亿（占总 ARR 约 21%） | FY25Q3 | B（国信证券转述） |
| Adobe | Creative freemium MAU | **破 1 亿，YoY +70%**（Firefly + Express + PS/LR/Premiere web&mobile） | 2026-08-28 | **A** |
| Adobe | 推迟 CC 定价优化 | FY26 总 ARR 增长目标 10.2%，「约一半来自推迟创意产品线价格优化，另一半来自全力投入免费增值体验」 | FY2026 指引 | **A**（电话会）+ B（国信证券解读） |
| Adobe | Non-GAAP 经营利润率 | **≈45%**（FY26 指引） | FY2026 指引 | **A** |
| **Stability AI** | 收入 vs 亏损 | **2024Q1 收入 <$5M，亏损 >$30M，欠云厂商近 $100M 未付** | USD / 2024Q1 | **A/B**（Reuters 报道，经二级源转述） |
| Stability AI | 融资 vs 云支出 | 「仅筹得约 $80M 新融资，而公司一年云基础设施费用超过 $99M」 | USD / 2024–2025 | B |
| Stability AI | B 轮 | **$76M**（UMG / Warner / Sony / EA / AMD Ventures / Coatue 等）；Akkaraju 任内累计融资 $232M | USD / 2026-08-25 | B（Variety 转述） |
| Stability AI | 收入估计 | ~$190M ARR（2025–2026）⚠️ 与 2024Q1 <$5M 口径**严重冲突** | USD / 2025–2026 | C（fueler.io，低可信）→ **不建议引用** |
| Stability AI | 商业模式转向 | 2025-08-05 发布企业产品 **Stability AI Solutions**；2026-04-08 上线 **Brand Studio**（Trial 1,000 credits 免费 / Creator $19 月 2,000 / Core $50 月 5,000 / Enterprise 定制） | 2025–2026 | B + C |
| **美图（1357.HK）** | 总收入 | **22.13 亿元**，YoY +22.1% | CNY / 2026H1 / 持续经营业务 | **A**（财报） |
| 美图 | 影像与设计产品收入 | **17.69 亿元**，YoY +30.9%，占总收入 79.9% | CNY / 2026H1 | **A** |
| 美图 | 经调整归母净利 | **6.52 亿元**，YoY +39.5% | CNY / 2026H1 | **A** |
| 美图 | 付费订阅用户 | **1,844 万**，YoY +19.7%；渗透率 **6.5%**（+1pp YoY） | 截至 2026-06-30 | **A** |
| 美图 | VIP 订阅占总收入 | **79.9%**（上年同期 74.5%） | 2026H1 | **A** |
| 美图 | 广告收入 | **4.15 亿元，YoY −4.4%**（三大板块唯一下降） | CNY / 2026H1 | **A** |
| 美图 | AI 生产力 ARR | **约 6.2 亿元**，YoY +47.8%；生产力 MAU 3,300 万（YoY +43.5%） | 截至 2026-06 | **A** |
| 美图 | AI 算力点消费 | 2026 Q1/Q2 **环比各 +46%**，半年累计 **+113%**；Q2 付费用户 AI 渗透率 **>46%** | 2026H1 | **A** |
| 美图 | **推算月 ARPPU** | 17.69 亿 ÷ 1,844 万 ÷ 6 ≈ **¥16/月** `[estimate]` | CNY / 2026H1 均值 | 推导自 A（注：分母含生活场景 1,609 万 + 生产力 235 万，混合口径） |
| 美图 | 生产力 vs 生活场景 ARPPU | 生产力高约 **50%**；美图设计室已有数千名用户年化消费达综合 ARPPU 的 **约 10 倍** | 2026H1 | **A**（CFO 表态） |
| **Canva** | 收入 / MAU | 接近 **$20 亿年收入**；**180M+ MAU**；估值 $260 亿（最近一轮） | 2024（收购 Leonardo 时） | B |
| **Leonardo.Ai** | 被收购前 | 1,900 万+ 注册用户，累计生成 10 亿+ 张图；此前融资 $38.8M+ | 2024-07 收购时 | B（TechCrunch） |

### 3.6 自建 vs 云的盈亏平衡 `[estimate]`

```
breakeven_images = 硬件投入 / (云端单张成本 − 本地单张成本)
```
- 假设：云端 $0.04/张；本地仅电费 ≈ $0.002/张；硬件 $2,000
- → breakeven ≈ **52,600 张**
- 另一来源（creativeainews，C）：$3,500 本地配置 vs $150–240/月订阅组合 → **回本 15–24 个月**

⚠️ 该公式**不含**运维人力、模型更新、失败重试、机会成本。text2img.pro 自述：「If debugging a CUDA conflict costs you four billable hours, you've just spent more than a year of cloud subscription fees.」等级 C，但方向性成立。

---

## 4. 可下注判断（5 条）

### 判断 1：订阅制没有被 credits 取代，但**名义价格锚已被 credits 接管**——未来 12 个月看「月费不动、额度动」

- **论据 A（Adobe，官方）**：2025-06-17 起，CC 团队版单应用计划**新订阅者**每月 generative credits 从 500 降至 **25**；个人版单应用/摄影计划新订阅者同样降至 25。老用户保留原额度。（Adobe 官方 Learn 页 + Ars Technica）
- **论据 B（即梦，头部券商）**：连续包月 69/199/499 元的积分额度从 1,080/4,000/15,000 **削减到 725/2,210/6,160，降幅 33%/45%/59%**；同时增设 VIP 极速通道，2.0 / 2.0 fast VIP 较普通版**涨价 75% / 120%**；综合测算 Seedance 1.5pro / 2.0 普通版涨价 **49% / 99%**。（东方证券研报，2026-04）
- **结论**：C 端 AI 生成产品的**价格弹性在「额度」而非「月费」**。PM 设计定价时应把 credits 表当作真正的价格表，月费只是分层壳。

### 判断 2：**「无限标准图 + 积分只用于视频/音频/第三方模型」成为行业默认结构**，图片生成正在被降级为留存工具而非收入工具

- **论据（Adobe，官方）**：所有**付费** Firefly 计划「include unlimited access to standard generative AI features like Generate Image, Generative Fill, Generative Expand, and Text to Vector Graphics」；credits 只用于 video/audio/partner models。同时 Firefly ARR 在 Q2 FY26「approaching $300M」，Creative freemium MAU 破 1 亿。
- **推论**：Adobe 把图像生成做成 CC 的获客/留存漏斗，真正的钱在 video credits 和 CC 整包涨价。这与 Midjourney「图像即收入」是两种截然不同的 UE 结构。
- **下注**：任何仍然对「单张图」单独收费的 C 端产品，会在 12 个月内被迫转向「无限图 + 高价视频/编辑」。

### 判断 3：**单张裸算力成本已不是竞争壁垒，壁垒转移到「排队确定性」**

- **论据**：裸算力边际成本 $0.0002–0.005/张（§3.2 公式 A），而 API 零售价 $0.003–0.21/张。价差 10–300 倍全部由**弹性、并发、失败重试、SLA**构成。
- **论据（即梦，B）**：东方证券指出即梦增设 VIP 极速通道的核心卖点是「用户排队等待时间大幅减少」，并带来 75%/120% 的溢价。同时媒体实测「即便涨价，用户仍需排队数小时」（南方+/科创板日报）。
- **下注**：**「不排队」是可单独定价的 SKU，且溢价可达 75–120%**。这是 2026 年 AI 生成产品最容易变现、且最不需要技术优势的一个维度。

### 判断 4：**供给侧 model ID 寿命 < 18 个月，把定价锚在某个 model ID 上是结构性风险**

- **论据（OpenAI 官方 deprecations 页，A）**：
  - 2025-11-14 通知 → **`dall-e-2` / `dall-e-3` 于 2026-05-12 下线**
  - 2026-04-22 通知 → **`gpt-image-1` 于 2026-10-23 下线**
  - 2026-06-02 通知 → **`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` 于 2026-12-01 下线**
- **论据（Google，C）**：`gemini-2.5-flash-image`（Nano Banana）于 **2026-10-02** 下线，官方建议迁到 Gemini 3.1 Flash Image；Nano Banana 2 Lite 反而更便宜（$0.039 → $0.0336，−14%）。
- **下注**：14 个月内 OpenAI 下线 6 个图像端点。**任何以「单模型价格」做三年 UE 模型的商业计划都是错的。** 产品架构必须做 model-agnostic 抽象层。

### 判断 5：**国内 C 端 AI 绘画的 ARPPU 天花板显著低于海外，「订阅为主 + 广告为辅」的旧模型正在切换为「订阅 + 算力点」**

- **论据 A（美图，A）**：2026H1 影像与设计收入 17.69 亿元 ÷ 1,844 万付费用户 ÷ 6 月 = **月 ARPPU ≈ ¥16**；而 Midjourney Standard 是 **$30/月**（≈¥213）。**差 13 倍。**
- **论据 B（美图，A）**：广告收入 **−4.4%**（唯一下降板块）；VIP 订阅占比从 74.5% **升到 79.9%**；同时 CFO 明确说「商业模式从订阅制向 AI 算力点消费延伸」，且「高频用户的 ARPPU 也随之提升」，生产力应用 ARPPU 比生活场景高 **约 50%**。
- **下注**：国内不能用纯粹的固定月费吃到重度用户价值；**「低月费保底 + 算力点按量加购」是唯一能同时覆盖轻度和重度用户的结构**，美图已验证（算力点消费半年累计 +113%）。

---

## 5. 定价 vs 价值锚：为什么有的按张卖、有的按月卖、有的免费送？（可验证论据）

| 定价形态 | 真实驱动 | 可验证论据 |
|---|---|---|
| **免费送** | ① 大厂有非 AI 收入兜底，AI 是流量入口；② 边际成本已低到可忽略 | **Adobe**：Creative freemium MAU 破 1 亿（YoY +70%），CFO 明确说为此**推迟了 CC 定价优化**（FY26 ARR 增长 10.2% 中「约一半来自推迟创意产品线价格优化」）—— 免费是有对价的，代价是 ARR 增速。<br>**Microsoft 365**：$9.99/月 的 M365 Personal 里塞 100 boosts/天，AI 图像不是独立 SKU，**没有独立盈亏约束**。<br>**裸成本**：$0.0002–0.005/张（公式 A）让「免费 50 张/天」的账面成本只有 $0.01–0.25/天。 |
| **按月卖（订阅）** | ① 用户使用频次高且不可预测 → 按张卖会产生「预算焦虑」；② 需要可预测现金流 | **Midjourney**：卖的不是图，是 **GPU 小时**（Basic 3.3h / Standard 15h / Pro 30h / Mega 60h）。Holz 明确说第一年亏钱的原因是「高级用户、鲸鱼用户，他们抹去了我们所有的利润，然后把我们带到了负值」——**无限量订阅在重度用户身上是负毛利的**，后来才加「safeties」。<br>**Relax Mode 的存在**（Standard 及以上无限 Relax 图）本质是**把不可售卖的闲置 GPU 时间免费送出去**，而不是卖出去。 |
| **按张 / 按积分卖** | ① 用量方差极大（批量 vs 偶发）；② 成本随分辨率/步数/模型剧烈变化（$0.003 vs $0.08）；③ 上游涨价需要向下传导 | **fal.ai 的定价单位是 megapixel 不是「张」**：1024²=$0.025，2048²=$0.10，3840×2160=$0.225 —— 因为**成本随像素数线性增长**，按张卖会在高分辨率上亏死。<br>**OpenAI 从 per-image 转向 per-token**：gpt-image-2「priced by token rather than by a fixed image price: image output $30/1M tokens, image input $8/1M, text input $5/1M」—— 因为图生图的输入 token 不可控。<br>**Adobe 的积分只覆盖 video/audio/partner models**，标准图无限 —— 因为标准图成本已被压到可忽略，而视频/第三方模型成本仍高且方差大。 |
| **按席位卖（企业）** | 卖的不是算力，是**治理 + 版权兜底 + 审计** | **Midjourney 官方条款**：年毛收入 >$1M 的公司**必须**买 Pro 或 Mega —— 用合规条款而非功能差异做分层。<br>**Adobe**：IP indemnification 只给 eligible enterprise customers；Firefly Custom Models 也只在企业方案里。<br>**Leonardo Team Starter**：$24/seat/月，≥3 seats，卖点是 75,000 共享 tokens + 共享 Bank。 |
| **免费额度收缩** | 免费额度的成本敞口（$20–40/用户/月，§3.3）**高于入门订阅价**（$8–12/月） | **Midjourney 2023-03**：Holz 对 Gizmodo 说「We stopped trials because of massive amounts of people making throwaway accounts to get free images…This happened at the same time as a temporary gpu shortage. The two things came together and it was bringing down the service for paid users.」<br>**Adobe 2025-06-17**：新订阅者 credits 500 → 25（官方）。<br>**即梦 2026**：积分额度削减 33%/45%/59%（东方证券）。 |

---

## 6. 失败与塌陷案例（时间 + 原因）

| 时间 | 主体 | 事件 | 原因 / 机制 | 来源等级 |
|---|---|---|---|---|
| **2023-03 / 2023-04** | Midjourney | **永久取消免费试用**（不再恢复） | Holz：大量 throwaway accounts 刷免费图 + 同期 GPU 短缺，拖垮付费用户体验。（注：Washington Post 最初归因于深假；Holz 本人否认，Gizmodo 直引） | **B**（Gizmodo / Futurism / Greek Reporter 直引 Holz） |
| **2024-10-01** | Midjourney | 加购的 fast GPU 小时引入 **60 天过期**（此前永久有效） | 防止用户「买 Pro 再跳过一个月」套利，把囤积的算力负债清掉 | C |
| **2024 全年** | Stability AI | **2024Q1 收入 <$5M，亏损 >$30M，欠云厂商近 $100M 未付**；Coatue 要求创始人 Mostaque 辞职 | 开源模型被大规模复制/滥用，DreamStudio + API + 订阅收入均不及预期；云账单失控 | **A/B**（Reuters，经二级源转述） |
| **2024-03 / 2024-06** | Stability AI | 创始人 Emad Mostaque 辞任 CEO；$80M 重组融资（Sean Parker / Greycroft / Coatue / Lightspeed），Prem Akkaraju 接任 | 治理 + 现金流危机 | B |
| **2024-07 / 2025-05** | Leonardo.Ai | **被 Canva 收购**（现金+股票，金额未披露），120 人全员加入；此前仅融资 $38.8M+ | 独立变现跑不通；Canva 需要自研模型能力降低对第三方模型供应商的依赖 | **B**（TechCrunch，Cameron Adams 直引） |
| **2024（时间未精确）** | Canva | AI 能力上线导致**部分企业客户涨价 300%**，用户反弹后 2024-10 部分让步（teams 用户可免费加至 4 人） | AI 成本转嫁过猛 | B（Ars Technica） |
| **2025-06-17** | Adobe | CC 单应用计划**新订阅者**每月 generative credits **500 → 25**；CC All Apps 自动升级为 CC Pro，$60 → $70/月 | AI 成本转嫁 + 推动用户上更高档位 | **A**（Adobe 官方 Learn 页）+ **B**（Ars Technica） |
| **2025-08-05** | Stability AI | 发布企业级产品 **Stability AI Solutions**，从开源社区转向企业服务 | 承认「开源运动的核心悖论」：用两年证明开源可行，又用两年揭示其局限 | B |
| **2025-07-03 ⚠️日期冲突** | **Vega AI**（北京右脑科技 / RightBrain AI） | 发布停运公告，付费入口关闭、服务器关闭、用户数据清除；对 6/3–6/18 购买 30 天权益的用户按剩余时间退款 | ① 低价/免费获客→订阅回款→高额算力成本→亏损→融资的死循环；② API 封装（Wrapper）无护城河；③ 内容合规成本 | C（aitop100 公告转载 + tsight 分析）⚠️ 但百度百科显示该公司 2025-08 仍在更新产品、2025-12 商标仍在注册 → **停运具体日期 `[待确认]`，存在 2025 vs 2026 冲突** |
| **2025-12** | OpenAI | DALL·E 3 从 ChatGPT 移除，图像生成并入 GPT-5.x 原生多模态（GPT Image） | 产品线收敛 | C |
| **2026-04 / 2026-05** | 字节 即梦 AI | 连续包月 69/199/499 元档位积分额度削减 **33%/45%/59%**（1,080/4,000/15,000 → 725/2,210/6,160）；新增 VIP 极速通道溢价 75%/120%；综合涨价 49%/99% | 火山引擎日均 Token 调用量破 100 万亿，日均算力成本估约 400 万–1,200 万元；算力供给刚性瓶颈 | **B**（东方证券研报；晚点 LatePost 转述，等级 B） |
| **2026 上半年** | 字节 豆包 | 语音通话 / 图片生成 / 专家模式**限额**，用户感知「降智」 | 成本收缩，算力向有付费能力的产品倾斜 | C（用户反馈 + 自媒体分析） |
| **2026-05-12** | OpenAI | **`dall-e-2` 与 `dall-e-3` API 正式下线** | 产品代际替换（2025-11-14 已通知） | **A**（OpenAI Deprecations 官方页） |
| **2026-08-25** | Stability AI | $76M B 轮（UMG / Warner / Sony / EA / AMD Ventures 等），Akkaraju 任内累计 $232M | 版权诉讼压力下转向「授权数据训练」路线，让权利人进董事会 | B（Variety 转述，recodex 整理） |
| **2026-08-30** | OpenAI | **官方 DALL·E GPT 从 ChatGPT 下架** | 产品清理 | C |
| **2026-07-29 → 2026-08-31** | **Civitai** | 废除运行多年的「**每次生成分给模型作者 25%**」机制，改为创作者自定 per-generation licensing fee；旧制 2026-08-31 19:59 退役；**未设费的模型此后不再从生成中获得任何收入** | 平台承认 25% 计算口径错误（把 add-on fees 也算进基数）；改为把定价权下放给供给侧，平台改收「基础设施 + 商店 30% 抽成」 | **A**（Civitai 官方公告） |
| **2026-10-02** | Google | `gemini-2.5-flash-image`（Nano Banana）下线，迁往 Gemini 3.1 Flash Image | 常规代际替换；替代型号反而便宜 14% | C（转述 Google API pricing 页） |
| **2026-10-23** | OpenAI | **`gpt-image-1` 下线** | 代际替换（2026-04-22 通知） | **A** |
| **2026-12-01** | OpenAI | **`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` 下线** | 代际替换（2026-06-02 通知） | **A** |

> **未被证伪但需存疑的一条**：有来源称「Sora 已于 2026 年 3 月关闭」（aiproducthub，等级 C）。**未找到第二来源 → `[待确认]`，不要引用。**

---

## 7. 来源清单表

| # | 来源 | 类型 | 等级 | URL | 直接引文 |
|---|---|---|---|---|---|
| S1 | Midjourney Docs「Comparing Midjourney Plans」 | 官方文档 | **A** | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans | "Midjourney offers four subscription tiers: Basic, Standard, Pro, and Mega… Monthly Price $10 $30 $60 $120… Fast GPU Time 3.3 hr/month (200 minutes) 15 hr/month 30 hr/month 60 hr/month… Purchase Extra GPU Time $4/hr… You must purchase the Pro or Mega plan if you are a company making more than $1,000,000 USD in gross revenue per year." |
| S2 | Adobe「How much does Adobe Firefly cost?」 | 官方文档 | **A** | https://creativecloud.adobe.com/cc-shared/fragments/products/firefly/plans/faq | "Adobe Firefly Standard: US$9.99/mo — 2,000 generative credits… Pro: US$19.99/mo — 4,000… Pro Plus: US$49.99/mo — 10,000… Premium: US$199.99/mo — 50,000… All paid plans include unlimited standard image and vector generations." |
| S3 | Adobe Firefly plans 页 | 官方文档 | **A** | https://www.adobe.com/products/firefly/plans.html | "Firefly Standard US$9.99/mo… Firefly Pro US$19.99/mo… Firefly Premium US$199.99/mo… Creative Cloud Pro Regularly at US$69.99/mo" |
| S4 | Adobe SEC 8-K（FY2026 Q3 财报） | 财报/SEC | **A** | https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm | "Adobe AI-first ARR grew more than 150% year over year… Total Adobe Annualized Recurring Revenue ("ARR") exiting the quarter was $27.50 billion." |
| S5 | Adobe FY2026 Q3 Earnings Call Transcript | 官方电话会 | **A** | https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/adbe-q3fy26-transcript.pdf | "Firefly ending ARR across Firefly Apps and Firefly credit packs grew 40% quarter over quarter… AI-first ending ARR now exceeding $650 million and growing more than 150% year over year… creative freemium MAU crossed 100M and growing greater than 70% year over year" |
| S6 | Adobe FY2026 Q2 Earnings Script | 官方电话会 | **A** | https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/11606202/c5y6yteraf.pdf | "Firefly ending ARR, including Firefly apps and credit plans and Enterprise Firefly offerings, approaching $300 million" |
| S7 | Adobe Learn「更改 Creative Cloud 团队版计划」 | 官方文档 | **A** | https://learn.adobe.com/cn/creative-cloud/policy-pricing/changes-to-teams-plan.html | "自 2025 年 6 月 17 日起…以下 Creative Cloud 团队版单软件计划的所有新订阅者，其每月生成式积分额度将下调至 25 个" |
| S8 | Adobe HelpX「Generative credits FAQ」 | 官方文档 | **A** | https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html | "Creative Cloud Single App for teams… Standard 500 25"（2025-06-17 前后对比列） |
| S9 | OpenAI Platform「Image generation」定价 | 官方文档 | **A** | https://platform.openai.com/docs/guides/image-generation/ | "GPT Image 2… Low $0.006 / Medium $0.053 / High $0.211（1024×1024）… GPT Image 1.5 Low $0.009 / Medium $0.034 / High $0.133" |
| S10 | OpenAI Developers「Deprecations」 | 官方文档 | **A** | https://developers.openai.com/api/docs/deprecations | "On November 14th, 2025, we notified developers using DALL·E model snapshots of their deprecation and removal from the API on May 12, 2026." / "\| October 23, 2026 \| `gpt-image-1` \|" / "On June 2, 2026, we notified developers using older GPT Image models of their deprecation and removal from the API on December 1, 2026." |
| S11 | fal.ai「How to Use FLUX AI」 | 官方文档 | **A** | https://fal.ai/learn/tools/how-to-use-flux | "On fal, it costs $0.003 per megapixel [schnell]… [dev] runs at $0.025 per megapixel… FLUX 1.1 [pro] Ultra… $0.06 per image on fal… FLUX.2 [pro]… $0.03 for the first megapixel, $0.015 per additional megapixel" |
| S12 | fal.ai model page「FLUX.1 [dev]」 | 官方文档 | **A** | https://fal.ai/models/fal-ai/flux-1/dev | "1024×1024 image = 1 megapixel = $0.025; 2048×2048 image = 4 megapixels = $0.10; 3840×2160 image = 8.29 megapixels (rounds to 9) = $0.225" |
| S13 | Replicate Pricing | 官方定价页 | **A** | https://replicate.com/pricing | "Nvidia A100 (80GB)… $0.001400/sec $5.04/hr… Nvidia H100… $0.001525/sec $5.49/hr… Nvidia L40S… $0.000975/sec $3.51/hr… Nvidia T4… $0.000225/sec $0.81/hr" |
| S14 | 火山引擎「即梦AI-图像生成计费说明」 | 官方文档 | **A** | https://docs.volcengine.com/docs/JimengAI/JimengAI-imagegenerationbillinginstructions | "即梦AI-文生图3.0 / 3.1… 按调用次数扣费（单次出图1张）0.2 [元/图]… 即梦AI-图片生成4.0… 按生成张数扣费 0.22… 即梦AI-智能超清… 0.4" |
| S15 | 火山引擎首页（豆包图像创作模型 5.0） | 官方 | **A** | https://www.volcengine.com/ | "豆包图像创作模型 5.0… 文生图0.22元/张 图生图0.22元/张" |
| S16 | 即梦 AI 官网会员页 | 官方定价页 | **A** | https://jimeng.jianying.com/ai-tool | "基础会员… 725 积分每月 换算¥10=221积分… 标准会员… 2210 积分每月 ¥10=241积分… 高级会员… 12320 积分每月 ¥10=284积分… 超级会员… 54600 积分每月 ¥10=333积分" |
| S17 | Civitai「Creator Economy Update 2026」 | 官方公告 | **A** | https://civitai.com/articles/32087/creator-economy-update-2026-you-set-the-price-now | "Together these replace the old flat 25% generation compensation - a number we set, that you couldn't see or change… Base models: we suggest around 1 buzz per image. LoRAs: we suggest around 1 buzz per 10 images… Fees can go as low as 1 buzz per 100 images and as high as 100 buzz per image." |
| S18 | Civitai「Proposal: Fixing Creator Compensation」 | 官方公告 | **A** | https://civitai.com/articles/33749/proposal-fixing-creator-compensation-and-leveling-up-licensing-fees | "It's meant to be 25% of what a generation costs, but it's been coming off our add-on fees too… Take a plain SDXL generation. Base cost is 4 buzz per image" |
| S19 | 美图公司 2026 中期业绩（官网） | 官方财报 | **A** | https://www.meitu.com/zh/media/439 | "来自持续经营业务的总收入22.1亿元，同比增长22.1%… 影像与设计产品…收入同比增长30.9%至17.7亿元，占总收入的80%… 付费订阅用户数超1844万，同比增长19.7%。订阅渗透率为6.5%… 生产力应用的ARR约6.2亿元" |
| S20 | 证券时报（美图 2026H1 明细） | 头部财经媒体 | **B** | https://www.stcn.com/article/detail/4132099.html | "影像与设计产品为第一大收入来源，期内收入17.69亿元，同比增长30.9%，占总营收比重79.9%；广告业务收入4.15亿元，同比小幅下滑4.4%" |
| S21 | 央广网（美图业绩预告） | 头部媒体 | **B** | https://xm.cnr.cn/gqlb/hjxgq/20260731/t20260731_527738501.shtml | "2026第一、二季度，用户AI算力点消费总额均实现超过46%的环比增长… 第二季度增速进一步加快" |
| S22 | ifnews（美图 CFO 表态） | 财经媒体 | **B** | https://www.ifnews.com/news.html?aid=864095 | "随着美图的商业模式从订阅制向AI算力点消费延伸…目前美图生产力应用的ARPPU约比生活场景应用高出50%" |
| S23 | UPI / Centre Daily（Disney+ NBCU 诉 Midjourney） | 头部媒体转述法院文件 | **B** | https://www.centredaily.com/news/business/article308430690.html | "In 2023, Midjourney reported more than $200 million in revenue and in 2024 took in an additional $100 million on top of it… 'Midjourney, which has attracted millions of subscribers and made $300 million last year alone'" |
| S24 | Legal 500（Disney & Universal v Midjourney 分析） | 法律专业机构 | **B** | https://www.legal500.com/intelligence/hong-kong/technology/the-empire-strikes-back-%E2%80%93-disney-&-universal-v-midjourney | "reportedly over 21 million subscribers worldwide and ostensibly generating US$200 million in 2023 and US$300 million in 2024" |
| S25 | Entrepreneur（同案报道） | 头部商业媒体 | **B** | https://www.entrepreneur.com/business-news/disney-universal-sue-ai-startup-midjourney-plagiarism/493100 | "The startup was founded in 2021 and has since generated $50 million in revenue in 2022 and $300 million in revenue in 2024." |
| S26 | provenstartups「Midjourney Revenue: a bootstrapped number, graded」 | 数据审计型自媒体 | **C** | https://provenstartups.com/blog/revenue-reality/midjourney-revenue | "The best-supported figure is $300 million for calendar 2024… No margin or profit figure exists for any year… Sites take the 2024 figure, apply an invented growth rate, and publish a 2025 or 2026 run rate with no new evidence behind it." |
| S27 | Gizmodo（Holz 谈取消免费试用） | 头部科技媒体 | **B** | https://gizmodo.com/midjourney-deep-fake-ai-trump-arrested-pope-1850283812 | "We stopped trials because of massive amounts of people making throwaway accounts to get free images…This happened at the same time as a temporary gpu shortage. The two things came together and it was bringing down the service for paid users." |
| S28 | CSDN 转载 David Holz 访谈（中文） | 访谈转载 | **B/C** | https://blog.csdn.net/cf2SudS8x8F0v/article/details/129760918 | "我们云成本的10%用于培训，90%用于用户制作图像的推断。几乎所有的成本都在制作图像上。" / "第一个月我们是赔钱的，因为高级用户，鲸鱼用户，他们抹去了我们所有的利润" |
| S29 | The Verge / ae.headtopics（Holz 谈训练成本） | 头部媒体 | **B** | https://ae.headtopics.com/news/an-interview-with-david-holz-ceo-of-ai-image-generator-58170886 | "Training image models is probably around $50,000 every time you do it right now. And you never get it right in one try" |
| S30 | Ars Technica（Adobe 涨价 + credits 削减） | 头部科技媒体 | **B** | https://arstechnica.com/gadgets/2025/05/adobe-hikes-subscription-prices-to-support-generative-ai-features | "as of June 17, Adobe will give new single-app subscribers just 25 generative AI credits instead of the current 500." / "Creative Cloud All Apps subscribers into the Creative Cloud Pro subscription, which will be $70 per month… up from $60" |
| S31 | 东方证券研报（即梦涨价）via 智通财经/腾讯自选股 | 券商研报转载 | **B** | https://gu.qq.com/resources/shy/news/detail-v2/index.html?id=SN20260414092520a44ac11d | "一是基于Seedance2.0和fast版本另外增设VIP通道…2.0和2.0fastVIP模式较普通版本分别涨价75%和120%；二是削减会员订阅的积分额度权益，如在连续包月下，69/199/499元的积分额度，从此前的1080/4000/15000分削减到725/2210/6160分，减少幅度分别为33%/45%/59%。综合测算下，Seedance1.5pro/2.0普通版本涨价幅度分别为49%/99%。" |
| S32 | 南方+ / 南都（即梦会员与积分实测） | 头部媒体 | **B** | https://www.nfnews.com/content/ry5OdZzb6Z.html | "生成一条10秒左右的视频需要约60积分，15秒左右的视频需要90积分… 从即梦的收费来看，基础会员年费659元，标准会员年费1899元，高级会员年费5199元" |
| S33 | 科创板日报（即梦会员倒卖与续费） | 头部财经媒体 | **B** | https://chinastarmarket.cn/detail/2296174 | "以标准会员为例，每月含4000积分，连续包月首月119元，次月起恢复至199元/月；连续包年首年949元，次年则为1899元/年" |
| S34 | 搜狐（字节 AI 成本压力，引晚点 LatePost） | 门户转载 | **B/C** | https://www.sohu.com/a/1010867358_100223577 | "据《晚点 LatePost》独家消息，自2026年春节以来，字节跳动云计算业务火山引擎的日均云端大模型调用量已超过100万亿Tokens…这一规模的Token日均成本约在400万-1200万元人民币之间" |
| S35 | TechCrunch（Canva 收购 Leonardo.Ai，经 CSDN/CSDN Agent 转载） | 头部科技媒体 | **B** | https://agent.csdn.net/6a4f6d8110ee7a33f28b813c.html | "这笔交易的具体金额并未对外披露，但Canva联合创始人兼首席产品官Cameron Adams表示，此次收购采用现金和股票混合的方式。Leonardo.ai全部120名员工将加入Canva" / "Leonardo.ai拥有超过1900万注册用户，其工具已被用于创建超过10亿张图像" |
| S36 | besthub（Stability AI 企业转型，转述 Reuters） | 二级源转述 Reuters | **B/C** | https://www.besthub.dev/articles/stability-ai-s-enterprise-pivot-can-open-source-ai-survive-the-profit-crisis-64a943e5f19e | "Reuters reported Q1 2024 revenue under $5 million against losses exceeding $30 million and nearly $100 million in unpaid cloud fees." / "After raising roughly $80 million in new funding last year, the company spent over $99 million on cloud infrastructure in a single year" |
| S37 | SegmentFault（Stability AI 商业化转型） | 技术媒体 | **C** | https://segmentfault.com/a/1190000047392185 | "2025 年 8 月 5 日，Stability AI 发布面向企业的产品「Stability AI Solutions」… 去年，在创始人离职背景下，Stability AI 仅筹得约 8,000 万美元的新融资，而公司仅一年预计用于云基础设施的费用就超过了 9,900 万美元。" |
| S38 | recodex（Stability AI $76M B 轮，引 Variety） | 二级源转述 Variety | **B/C** | https://recodex.pro/stability-ai-raises-76m-series-b-music-giants-bet-big-can-generative-ai-tools-escape-copyright | "On August 25, 2026, the company… announced the close of a $76 million Series B round… According to Variety, the round brings Stability AI's total funding under CEO Prem Akkaraju to $232 million." |
| S39 | gpucloudlist（SDXL GPU 基准与每千张成本） | 自媒体基准站 | **C** | https://www.gpucloudlist.com/en/blog/best-gpu-cloud-stable-diffusion | "We benchmarked SDXL 1024x1024 generation (20 steps, DPM++ 2M Karras, batch size 1)… RTX 4090 24GB 2.1 seconds ~1,714 [img/hr] $0.27/hr (Vast.ai)… RTX 3090 — Vast.ai $0.07/hr 857 $0.08 [per 1,000 images]" |
| S40 | jarvislabs（SDXL GPU 成本对比） | 服务商基准 | **C** | https://jarvislabs.ai/ai-faqs/best-gpu-for-stable-diffusion | "H100 80GB ~1.5-2s/image $2.69 ~$1.50-2.00 [cost per 1000 images]… RTX 3090… $0.29 ~$0.60-0.90" |
| S41 | 极智算 JYGPU（2026-07 国内 GPU 租赁价格，经 ima.qq.com 转载） | 服务商/自媒体 | **C** | https://ima.qq.com/wiki/?shareId=514ddea87d37ee6890616e3411e61ad4de70fd929e275f91568a3540699cfed2 | "GPU型号 显存 容器时租(元) 裸金属月租(元/卡)… H100 80G 80GB HBM3 5.5-6.8 12,000-15,000… A100 80G 2.8-3.5 6,000-9,000… RTX 4090 24GB 1.96 1,500-2,500" |
| S42 | aitop100（Vega AI 停运公告转载） | 自媒体转载公告 | **C** | https://www.aitop100.cn/infomation/details/27832.html | "Vega AI 正式停止运营的日期定在了2025年7月3日… 到了2025年7月3日这一天，产品服务将全面终止，服务器也会随之关闭" |
| S43 | tsight（Vega AI 停运分析） | 自媒体分析 | **C** | https://tsight.io/articles/18100545 | "绝大多数AI绘画平台（包括Vega AI）陷入了同一个逻辑陷阱：以低价或免费策略获取用户 → 依赖订阅制回款 → 支付高额算力成本 → 亏损 → 寻求融资。" |
| S44 | aisotools（Nano Banana / gpt-image-1 下线迁移成本） | 自媒体 | **C** | https://aisotools.com/blog/image-generation-api-alternatives-2026 | "gemini-2.5-flash-image is deprecated and will be shut down on October 2, 2026… Nano Banana 2 Lite — $0.0336 per 1K image, 14% cheaper than the $0.039 you pay now." |
| S45 | pikes.ai（DALL·E 关停与替代价格） | 自媒体（有利益相关披露） | **C** | https://pikes.ai/blog/grok-imagine-vs-midjourney-vs-dalle-product-photography | "On November 14th, 2025, we notified developers using DALL·E model snapshots of their deprecation and removal from the API on May 12, 2026." |
| S46 | promoclock（Ideogram / Leonardo / Recraft / Canva 定价） | 聚合站 | **C** | https://promoclock.co/en/blog/best-ai-image-generators | "Ideogram gives free accounts 30 credits a week; Plus costs $20/month for 2,400 credits, Pro $60/month for 7,500 and Team $30 per user… Leonardo.ai's free plan refreshes 150 fast tokens a day… Essential costs $12/month, Premium $30 and Ultimate $60" |
| S47 | ampm-aiops（Ideogram / Leonardo 官方定价核验） | 聚合站 | **C** | https://ampm-aiops.com/en/compare/ideogram-vs-leonardo | "Read directly from leonardo.ai/pricing on 2026-09-25: from US$72/month (US$24 per seat per month, minimum 3 seats), 75,000 shared tokens" |
| S48 | toolchew（2026-05-20 各图像 API 价格核验） | 聚合站 | **C** | https://toolchew.com/en/best-ai-image-api | "FLUX.1 [schnell] fal.ai $0.003… FLUX.2 [pro] BFL direct / fal.ai $0.030… Stable Image Core Stability AI $0.030… SD3.5 Large Stability AI $0.065… Stable Image Ultra Stability AI $0.080" |
| S49 | hokai.io（Stability Brand Studio 定价） | 聚合站 | **C** | https://hokai.io/hub/tools/stability-ai | "Brand Studio's Creator tier is $19 a month for 2,000 credits and Core is $50 a month for 5,000… Open-source models remain free to self-host under the Stability AI Community License for organizations under $1 million in annual revenue." |
| S50 | biemoyu / feizhuke（LiblibAI 定价三层结构） | 导航站转载 | **C** | https://feizhuke.com/sites/liblibai-guanwang.html | "liblibai采用'免费额度+会员订阅+按需购买'的三层定价结构… 免费版 50积分/天；基础会员(¥29/月) 300积分/天；专业会员(¥59/月) 600积分/天；旗舰会员(¥99/月) 1200积分/天" |
| S51 | flowith（Liblib vs SeaArt 社区与创作者分成） | 自媒体 | **C** | https://flowith.io/blog/liblib-vs-seaart-which-better-model-quality-community-size | "Liblib Community 200,000 active creators sharing models, LoRAs, and workflows… Revenue sharing for model creators" |
| S52 | ai-bio（国内 14 款图生视频工具价格，2026-08-26 采集） | 聚合站 | **C** | https://ai-bio.cn/ai-video-from-image-tools/ | "即梦AI(字节) 每日60~100积分… 基础¥69/月·1080积分… 通义万相(阿里) 每日50灵感值·App不限次 标准¥47/月·300灵感值… 注：以上数据采集于2026年8月26日" |
| S53 | 华安/三个皮匠（即梦、可灵会员价格与积分） | 研报转载 | **B/C** | https://www.sgpjbg.com/info/ddd62166320260a2ee07e58738f1c2ca.html | "基础会员79元/月（1080积分），标准会员239元/月（4000积分），高级会员649元/月（15000积分）… 黄金会员66元/月（66个标准视频），铂金会员268元/月（300个标准视频），钻石会员666元/月（800个标准视频）" |
| S54 | 国信证券（Adobe FY26Q2 解读） | 券商研报转载 | **B** | https://ima.qq.com/wiki/?shareId=d548021a437cf2f7992008afcfebd3b361bece8d8d19985a0e0f5c4acc91de31 | "FY26Q2 Firefly ARR，包括Firefly App、Firefly点数包等已超过3亿美元（FY26Q1为2.5亿）… FY25Q3表示Adobe 受人工智能影响的ARR已超过50亿美元，测算占比总ARR21%" |
| S55 | valueaddvc（Midjourney ARR 建模） | 自媒体建模 | **C** | https://valueaddvc.com/blog/how-does-midjourney-make-money-500m-arr-zero-funding-and-the-ai-image-business-model-explained | "roughly $200 million in annualized revenue in early 2024, about $300 million by the end of 2025, and an estimated $500 million to $600 million by mid-2026… Midjourney's $10B figure is a research-firm estimate, not a priced funding round." |
| S56 | aitrendtool（图像 API 定价核验） | 聚合站 | **C** | http://aitrendtool.com/best/best-ai-image-generation-apis | "Seedream V4 at $0.03 per image, FLUX Kontext Pro at $0.04, Nano Banana at $0.0398, Qwen Image at $0.02 per megapixel… Serverless GPUs are also available from $1.89/hour for an H100" |
| S57 | aiwiki（Leonardo.Ai 被 Canva 收购后发展） | 百科站 | **C** | https://aiwiki.ai/wiki/leonardo_ai | "At the time of the acquisition, Leonardo.AI had more than 19 million users and had generated over 1 billion images." |
| S58 | text2img.pro（Cloud vs Local 成本对比） | 自媒体 | **C** | https://www.text2img.pro/cloud-vs-local-ai-image-generation-24 | "Marginal cost per image [cloud] $0.001–$0.05 [local] Electricity only… A $2,500 workstation amortized over three years costs about $70 per month, plus perhaps $15 in electricity" |
| S59 | morphed（Bing Image Creator 免费额度） | 聚合站 | **C** | https://morphed.app/blog/bing-image-creator-limits | "Bing Image Creator gives you 15 fast generations ("boosts") per week, then an uncapped but slow queue at 2-5 minutes per generation." ⚠️ 与 S60、S61 冲突 |
| S60 | vantaige（Bing Image Creator，2026-04） | 聚合站 | **C** | https://vantaige.io/ai-tool/bing-image-creator | "Free accounts receive 15 fast 'boosts' per day… Copilot Pro subscribers at $20 per month get 100 boosts daily" ⚠️ 与 S59 冲突 |
| S61 | costbench（Bing Image Creator Pricing 2026） | 聚合站 | **C** | https://www.costbench.com/software/ai-image-generators/bing-image-creator | "You get unlimited image generations at standard speed plus 25 fast-generation boosts per week at no charge." ⚠️ 与 S59、S60 冲突 |
| S62 | tech-insider（Bing Image Creator 2026-10 现状） | 自媒体 | **C** | https://tech-insider.org/bing-image-creator-setup-2026/ | "a model Microsoft's own Azure documentation confirms was retired for new deployments on March 4, 2026. Bing Image Creator's current help page no longer mentions DALL-E at all. Instead, it lists two selectable models: MAI-Image-2e… and MAI-Image-2.5-Flash" |
| S63 | 百度百科（Vega AI / 北京右脑科技） | 百科 | **C** | https://baike.baidu.com/item/北京右脑科技有限公司/63218904 | "2025年8月，公司旗下AI视频创作平台Video Studio（视频创作）功能开启内测… 2025年12月13日，'VEGA AI'商标注册成功" ⚠️ 与 S42 的 2025-07-03 停运日期冲突 |
| S64 | modelslab（Replicate 按秒 vs 按张） | 服务商 | **C** | https://modelslab.com/replicate-pricing | "Nvidia A100 (80GB) $0.001400 $5.04 $3,628.80 [30 days online]… Nvidia H100 $0.001525 $5.49 $3,952.80" |
| S65 | usagepricing（Midjourney 定价历史） | 聚合站 | **C** | https://usagepricing.com/blueprint/midjourney | "Free trial permanently suspended Apr 2023… Effective October 1, 2024, Midjourney introduced a 60-day expiration on top-up fast hours purchased at $4/hour." |
| S66 | yankucms（国内生图 API 价格选型） | 自媒体 | **C** | http://www.yankucms.cn/news/4.html | "Z‑Image‑Turbo:0.10 元/张… LiblibAI… SDXL:约0.06 元/张起… 阿里云通义万相 wanx‑v1:0.16 元/张… 火山即梦 4.0:0.22 元/张" |
| S67 | readaitime（通义万相免费额度与 API 价） | 聚合站 | **C** | https://www.readaitime.com/zh-hant/tools/tongyi-wanxiang | "阿里云百炼开通后，新使用者约有 50 张文生图 + 50 秒影片生成的免费额度（90 天内领用）… 文生图 wan2.6-t2i/wan2.5-t2i-preview/wan2.2-t2i-plus 均为 0.20 元/张、轻量档 wan2.2-t2i-flash 为 0.14 元/张" |
| S68 | gemlist（Civitai Buzz 分成机制） | 聚合站 | **C** | https://www.gemlist.io/blog/how-much-does-civitai-pay-creators | "Civitai doesn't publish the pool size or total Buzz banked, which makes earnings genuinely hard to predict" |
| S69 | creativeainews（2026-03 开源创意 AI 成本回收期） | 自媒体 | **C** | https://www.creativeainews.com/articles/open-source-creative-ai-march-2026-wave/ | "Total: $150 to $240 per month, or $1,800 to $2,880 per year. A $3,500 local setup pays for itself in 15 to 24 months" |
| S70 | 今日头条（AI 应用泡沫：C 端娱乐工具） | 自媒体 | **C** | https://www.toutiao.com/a7663679811411313202 | "市面上同类工具超过上万款，用户几乎全部习惯免费试用，付费会员转化率常年低于3%，单用户年付费金额不足30元" ⚠️ 未标注统计口径与来源，仅作方向性参考，不可作为定价依据 |

---

## 8. 查不到 / 证据薄弱清单

| # | 缺口 | 现状 | 为什么重要 |
|---|---|---|---|
| 1 | **任何 AI 绘画公司的公开毛利率 / 毛利额** | `[待确认]`。Midjourney 从未披露利润率（provenstartups 明确："No margin or profit figure exists for any year"）；Adobe 只披露公司整体 non-GAAP 经营利润率 ≈45%，**未拆分 Firefly**；美图未拆分 AI 算力点的毛利。 | 所有「AI 绘画毛利率 80%」的说法都不可核验。**面试中若被问，正确回答是「公开市场无任何一家披露过分部毛利率，只能用 ARR 与云端 API 价反推」。** |
| 2 | **Midjourney 2025 / 2026 收入** | 流传的 $500M–600M ARR 是**第三方按 2024 年 $300M 加假设增长率外推**，无新证据（S26 明确批评）。 | 极易在面试/汇报中被当成事实引用。**必须标 estimate。** |
| 3 | **Midjourney 的实际 GPU 采购成本** | `[待确认]`。只有 Holz 2022 年的定性描述（"$20,000–$40,000 GPU servers"、"超过 10,000 个 GPU"、"云成本 90% 是推理"），**无 2026 年数字**。 | 无法算出 Midjourney 的真实毛利。§3.2 公式 D 只能给出「收入侧 GPU 小时价 $3–4 vs 市场租金 $1.29–5.49」的相对判断。 |
| 4 | **Stability AI 的真实收入** | 严重冲突：Reuters 口径 2024Q1 收入 <$5M；另有来源（fueler.io，C）称 2025–2026 ARR ~$190M。**两者相差 40 倍，无法调和。** | 建议**只引用 Reuters 口径**，废弃 fueler 数字。 |
| 5 | **Vega AI 停运的确切日期** | 冲突：aitop100（C）称 2025-07-03；但百度百科显示该公司 2025-08 仍在发新功能、2025-12 仍在注册商标。 | 案例本身可信（多个独立源都提到停运公告），**日期不可引用**。 |
| 6 | **Bing Image Creator / Copilot Designer 的免费额度** | 三源冲突：15/周、15/天、25/周。官方帮助页未在可抓取内容中给出数字。 | 不要用这个数字做任何成本测算。 |
| 7 | **国内独立 AI 绘画平台（非大厂）的广告变现与流量分成机制** | `[待确认]`。只找到美图的广告收入（4.15 亿元，−4.4%），但那是美图整体广告，不专属于 AI 绘画。 | 「内容平台广告与流量分成」这一模式在国内独立 AI 绘画产品上**缺实证**。 |
| 8 | **国内平台的创作者分成比例** | `[待确认]`。LiblibAI 有 "revenue sharing for model creators"（C），但**比例、池子规模、结算方式均未公开**。 | 与 Civitai 的透明机制（A）对比时，国内侧无对等可核验数据。 |
| 9 | **2026 年前沿图像模型的单次训练成本** | `[待确认]`。Holz 的 $50,000/次是 **2022 年**口径，不能外推。 | 无法评估新玩家的自研门槛。 |
| 10 | **国内 AI 绘画产品的付费转化率** | 只有一个未标注口径的自媒体数字："付费会员转化率常年低于3%，单用户年付费金额不足30元"（S70，C）。 | 与美图的官方渗透率 6.5%（A）**口径不同**（后者是全公司 VIP 渗透率），不可混用。 |
| 11 | **Midjourney × Meta 技术授权协议的金额与范围** | `[SINGLE_SOURCE]` + `[待确认]`。仅 valueaddvc（C）提到 "a 2025 licensing deal with Meta (reportedly for image/video model technology)"。 | 若成立，是「模型授权给大厂」模式的唯一 AI 绘画实例，值得单独核实。 |
| 12 | **Adobe Firefly ARR 在 FY2026Q3 的绝对值** | 官方只给了「环比 +40%」和 Q2 的 "approaching $300M"。 → Q3 ≈ **$420M `[estimate]`**（$300M × 1.4）。**官方未直接披露绝对值。** | 引用时必须标 estimate 或用「环比 +40%」这个官方口径。 |
| 13 | **可灵 AI 会员价格** | 多源冲突：¥66/月（黄金，多源）vs ¥58/月（火山引擎开发者社区）；铂金 ¥266 vs ¥268 vs ¥234。 | 国内视频/图像产品调价频繁，任何单源价格都应标 timepoint 与来源等级。 |
| 14 | **Sora 是否已于 2026-03 关闭** | `[SINGLE_SOURCE]`（aiproducthub，C）。 | **不要引用。** |
| 15 | **2026 年国内算力租赁涨价 30–40% 的幅度** | `[SINGLE_SOURCE]`（ima.qq.com 转述 JYGPU）。方向性（高端卡涨、低端卡跌）有第二个源佐证（S41），但 **30–40% 这个具体幅度无第二来源**。 | 可做定性表述，不做定量引用。 |
| 16 | **单张图推理成本的一手权威测算** | 所有可用的都是**服务商/自媒体自测基准**（gpucloudlist、jarvislabs，C），无第三方权威机构（如 MLPerf、Epoch AI）的公开图像推理成本基准。 | §3.2 公式 A 的整个吞吐假设建立在 C 级来源上，**这是本报告证据链最薄弱的一环**。建议实操时用「直接跑自己的 workload 测」替代引用。 |

---

## 9. 给 PM 的三条直接可用结论

1. **定价表 = credits 表，不是月费表。** 参考 Adobe（无限标准图 + 积分只管视频/第三方模型）和即梦（月费不变、额度砍 33%–59%）。设计定价时先定 credits 消耗系数表，再倒推月费档位。
2. **把「不排队」做成 SKU。** 即梦 VIP 极速通道的直接溢价是 **75%–120%**（东方证券），这是当前 ROI 最高的变现维度，且不需要模型能力领先。
3. **UE 模型必须做 model-agnostic。** OpenAI 14 个月内下线 6 个图像端点（A）。任何把成本锁定在单一 model ID 上的三年财务模型，在 2026 年都是不可用的。
