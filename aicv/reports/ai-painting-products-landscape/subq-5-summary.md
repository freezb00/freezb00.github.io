# SQ5｜AI 绘画产品的用户分层、JTBD 与付费意愿证据

> 子问题归属：AI 绘画产品调研全景 · 深度「决策级」 · 使用人：产品经理（求职/面试）
> 检索完成日：2026-10-12 ｜ 优先采用 2025-2026 信息，每条标注 timepoint
> 引用格式：正文用【S#】指向文末来源清单；来源清单含 `source_url` + 直接引文 `quote` + `source_grade`
> 来源等级：A＝官方/学术/财报原文；B＝头部媒体·机构报告·券商/第三方数据机构；C＝自媒体/UGC/聚合站/厂商营销页
> 厂商自报数据一律标注 `(self-reported)`；本文自行计算的派生值一律标注 `【本文推算】`；查不到的一律写 `[待确认]`

---

## 0. 一句话结论（先看这个）

AI 绘画的**付费率天花板被"泛娱乐用户"拉低、被"生产力场景"抬高**：美图官方财报显示，生活/娱乐场景订阅渗透率 5.9%，而电商设计等生产力场景达 9.0%（2025-12-31，付费用户 216 万 / MAU 2400 万）【S1】。学术侧对 394 名数字媒体设计师的 CB-SEM 研究显示，**感知易用性（β=0.310）对订阅意愿的影响大于价格价值（β=0.197）**，而"个人创新性"不显著（p=0.097）【S8】——即专业层付费不是被"价格便宜"驱动的，是被**可控与稳定**驱动的。

---

## 1. 用户分层大表

### 1.1 分层总表（8 层）

| # | 层级 | 典型 JTBD（用户要完成的任务） | 画质 | 一致性 | 可控性 | 批量 | 付费能力 | 代表产品 | 核心证据 |
|---|---|---|---|---|---|---|---|---|---|
| L1 | 泛 C 端娱乐（头像/壁纸/表情包/社交分享） | "把我/我的宠物变成某风格的一张图，发出去" | 屏幕级即可，重"好看/好玩" | 无要求（单张即交付） | 低（抽卡式可接受） | 低（单次 1-10 张） | 弱：免费额度即够，付费为去水印/提速 | 美图秀秀/美颜相机/Wink、Meta AI、豆包/即梦 | 美图生活场景付费率 5.9%【S1】；AI 原生 App 月人均时长 143.2 分钟（2025-12）【S10】 |
| L2 | 专业/半专业画师·插画师 | "在交稿周期内产出可用底稿/灵感变体，保留我的个人风格" | 高（可放大、可印） | 高（同一角色跨页一致） | 高（局部重绘/参考图/LoRA） | 中（几十至数百张/项目） | 中：愿为"角色一致性+私有风格"付 $20-60/月 | Midjourney（Pro/Mega 才有 Stealth）、Leonardo（自定义模型）、SD+ComfyUI | Midjourney Pro/Mega 才给 Stealth 与 12 并发【S7】；Leonardo 付费档才给私有生成与商用权【S36】 |
| L3 | 设计师（平面/UI/包装/建筑可视化） | "在既有设计软件里改一版、出几个方向给客户看" | 高，且要可编辑/矢量 | 中-高（品牌调性一致） | 高（与 PSD/AI/CDR 工作流打通） | 中 | 中-高：已在付 CC 订阅，AI 作为加购 | Adobe Firefly（85% 用量在 PS/AI/PR/Express 内）、Canva | Firefly 生成资产 240 亿（2025-06）【S44】；85% 用量在四款 CC 应用内【S44】 |
| L4 | 电商商家与运营 | "把一件衣服/一个 SKU 变成一整套可上架的图，提升点击率" | 中（平台主图规格够用） | 高（同一商品多角度、同模特跨 SKU） | 中（按模板出图，不调 prompt） | **极高**（数千 SKU） | 高：ROI 直接可算，愿按"出图量"付费 | 美图设计室、淘宝生意管家·智图/智影、阿里妈妈万相营造、天猫"家作" | 淘宝 AI 美工月均生成 2 亿张图/500 万个视频，商品点击率 +10%【S11】；生意管家累计生成 8.7 亿张图，月活商家近 200 万【S13】 |
| L5 | 游戏与影视 | "缩短前期：概念图、分镜、贴图、NPC/场景资产" | 高（概念图要能说服立项） | 高（角色/场景跨镜头一致） | 高（要接入引擎与 DCC） | 高（上万资产） | 高：省的是人天，按项目/席位付费 | Midjourney/Leonardo/SD、Unity 生态、ComfyUI 管线 | 51% 日本游戏公司在用生成式 AI，视觉资产居首（CESA，54 家，2025-06/07）【S18】；Unity 2026 报告：概念艺术与游戏资产 35%【S19】；Steam 2025 约 1/5 新游披露用生成式 AI，视觉资产约占用途 60%【S20】 |
| L6 | 企业营销与办公 | "把 PPT/报告/海报里的配图补齐，且版权安全" | 中（演示级） | 中（品牌模板一致） | 低（要"一句话出图"） | 中 | 中-高：走企业采购，看重**版权可赔付** | Adobe Firefly（CC Pro/团队版）、Canva、Microsoft 系、Gamma | Adobe CC 出现在 22.6 万+ 企业技术栈【S44】；Canva B2B（25+ 席位）ARR $5 亿、同比翻倍【S4】 |
| L7 | 教育与出版 | "按教材/绘本的文字稿配图，过审校、能印刷、版权可追溯" | **印前级（300dpi+，CMYK 不塌）** | **极高（跨册跨页同一人物）** | **高（要能按知识点改细节）** | 中-高（一本 200-400 张） | 中（受教材定价"保本微利"约束）→ 强价格敏感 | 童趣等出版社自研流程、通用工具+人工修 | 《小步日诵》384 张图：AI 出图时间成本 -60%、费用 -68%【S15】；教材须"插图质量高、图文配合得当"且国家审定【S16】 |
| L8 | 开发者 / 工作流编排 | "把出图能力 API 化，接进我自己的产品/管线" | 取决于下游 | 靠参考图 + 种子 + 后处理 | **最高（参数全暴露）** | 极高 | 按量付费，单价敏感，追求 batch 折扣 | Gemini API、OpenAI Images、Leonardo API、Replicate/ComfyUI | Gemini 3 Pro Image 官方输出 $0.134/张（1K/2K）、$0.24/张（4K），Batch 半价 $0.067/$0.12【S32】 |

> **口径说明**：上表"画质/一致性/可控性/批量"四列的具体档位是**本文基于引用证据的 PM 推断**（非引用事实），用于产品设计输入；付费能力与代表产品列均有引用支撑。

### 1.2 分层结构的第三方口径（用于交叉验证）

- **按应用**：Meticulous Research 估算 2025 年 AI 图像生成器市场中 **professional/enterprises 占 >74%**，personal 占其余但 CAGR 更高（2025-2032 预测）【注：该机构为付费报告摘要页，等级 C，仅作方向参考】。
- **按终端行业**：Meticulous 估算 2025 年 marketing & advertising 占比 >36%（最大单一终端）【同上，C 级】；Dataintelo 估算 media & entertainment 34.2%、advertising 26.8%、design 18.4%、education 10.9%【C 级机构，与前者口径冲突，均为 [SINGLE_SOURCE] 且互不一致，建议面试中不用具体数字，只说"广告营销与文娱是最大两块"】。
- **可靠结论**：不同第三方对"谁最大"说法不一致（marketing vs media&entertainment），**不要引用单一第三方市场份额数字**。可信度更高的是**上市公司自披露的分场景付费率**（美图）与**行业协会调研**（CESA、AOI）。

---

## 2. 付费意愿与漏斗数据表

### 2.1 已披露的付费率 / 订阅渗透率（最硬的一批）

| 指标 | 数值 | unit | timepoint | scope | 来源等级 | 备注 |
|---|---|---|---|---|---|---|
| 美图整体订阅渗透率 | **6.1%**（2024: 4.7%，+1.4p.p.） | 付费订阅用户/MAU | 2025-12-31 | 全球，MAU 2.76 亿、付费 1691 万 | **A（HKEX 年报原文）** | 官方披露口径【S1】 |
| 美图·生活/娱乐场景渗透率 | **5.9%**（2024: 4.6%） | 同上 | 2025-12-31 | 付费 1475 万 / MAU 2.52 亿 | **A** | 对应 L1 泛娱乐层【S1】 |
| 美图·生产力工具渗透率 | **9.0%**（2024: 5.9%，+3.1p.p.） | 同上 | 2025-12-31 | 付费 216 万 / MAU 2400 万 | **A** | 对应 L4 电商/口播层【S1】 |
| 生产力付费用户同比 | **+67.4%** | YoY | FY2025 | 216 万 vs 129 万 | **A** | 增速远高于生活场景 +30.3%【S1】 |
| Canva 付费率 | **≈11.7%**【本文推算】 | 付费用户/MAU | 2025 年末 | 付费 >3100 万 / MAU >2.65 亿 | B（TechCrunch 引 COO，self-reported） | 口径不一致（付费含团队席位），仅作量级参考【S4】 |
| 中国生成式 AI 用户规模 | **5.15 亿人**，普及率 **36.5%**，半年 +2.66 亿 | 人 / % | 2025-06 | 中国大陆 | **A（CNNIC，新华社/中国政府网发布）** | 未单独披露"图像生成"付费率【S9】 |
| 中国移动端 AI 应用 MAU | **7.22 亿**（PC 端 2.05 亿） | MAU | 2025-12 | 中国大陆 | B（QuestMobile） | AI 原生 App 月人均时长 143.2 分钟 vs 工具类 90.3、拍摄美化 52.1【S10】 |
| Midjourney 付费用户数 | **≈139 万**【估算，非官方】 | 人 | 2025 | 全球 | **C（分析师推算）** | 由 $500M 收入 ÷ $30/月混合价推算，**不可作为事实引用**【S40】 |
| Midjourney 付费率 | **[待确认]** | — | — | — | — | 官方从未披露注册/付费结构；网传 21.5% 转付费与官方"无免费层"自相矛盾，不可用 |

### 2.2 ARPU / 客单价

| 指标 | 数值 | unit | timepoint | scope | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 美图 ARPU（上界估计） | **≈174.7 元/年 ≈ 14.6 元/月**【本文推算】 | 元/付费用户/年 | FY2025 | 影像与设计收入 29.54 亿元 ÷ 付费 1691 万 | A（分子分母均来自 A 级财报） | 分子含非订阅收入，故为**上界**；美图 CFO 明确"ARPU 提升将成为未来主要增长引擎"【S1】【S2】 |
| Canva ARR | **40 亿美元**；B2B（25+ 席位）ARR **5 亿美元**、同比 +100% | USD ARR | 2025 年末 | 全球 | B（self-reported，COO 对 TechCrunch 口述） | 推算 ARPU ≈ $129/年【本文推算：$4B ÷ 31M】；口径含团队合同【S4】 |
| Midjourney 定价 | Basic $10 / Standard $30 / Pro $60 / Mega $120 每月；年付 8 折（$96/$288/$576/$1152 每年）；额外 Fast GPU $4/小时 | USD/月 | 官方页面当前价 | 全球 | **A（Midjourney 官方文档）** | 买的是 **Fast GPU 小时**（3.3/15/30/60 小时/月），不是张数；**无免费层**【S7】 |
| Midjourney 2025 收入 | **≈5 亿美元** | USD | FY2025 | 全球 | **C（第三方估算 PitchBook/Sacra 系）** | 2022 $50M→2023 $200M→2024 $300M→2025 ~$500M；**非官方披露，面试中须说明是估算**【S40】 |
| Adobe Firefly 官方定价 | Free（每日免费生成）/ Standard **$9.99**（2000 credits）/ Pro **$19.99**（4000 credits）/ Pro Plus **$49.99**（10000 credits）每月 | USD/月 | 官方页面当前价 | 全球 | **A（Adobe 官网）** | 标准图像功能 unlimited，credits 只花在 premium（视频/第三方模型）【S5】 |
| Adobe 整体 | FY2025 收入 **$237.7 亿**（+11% YoY）；总 ending ARR **$252 亿**；AI-influenced ARR **>$50 亿**（占整体 >1/3） | USD | FY2025（截至 2025-11-28） | 全球 | B（财报电话会转述） | 【S23】 |
| Adobe AI-first ARR | **>$2.5 亿**（Firefly 应用+Credit pack+企业版，Q1 FY26） | USD ARR | 2026-03 | 全球 | B（招银国际引 Adobe 财报） | **Firefly 收入仅占 Adobe 总收入约 1%**；Firefly 订阅+Credit pack ARR 环比 +75%，Generative credit 消费环比 +45%【S25】 |
| Adobe Firefly 累计生成量 | **220 亿**（2025-04）→ **240 亿**（2025-06） | 个资产 | 2025 | 全球 | B（Adobe 官方里程碑转述） | 85% 用量发生在 Photoshop/Illustrator/Premiere/Express 内【S44】 |
| Google Gemini 3 Pro Image | **$0.134/张（1K/2K）、$0.24/张（4K）**；Batch **$0.067 / $0.12** | USD/张 | 2026（官方定价页） | API | B（多个二级源一致的官方定价转述） | Nano Banana 2（Gemini 3.1 Flash Image）：$0.067/1K、$0.101/2K、$0.151/4K【S32】 |

### 2.3 学术侧：专业用户"为什么付费"（唯一可得的 A 级因果研究）

来源：Hu, Chen & Ding, *Scientific Reports* 15 (2025), DOI 10.1038/s41598-025-99924-7 / PMC12062495【S8】。方法：30 人访谈扎根编码 + N=394 数字媒体设计师 CB-SEM（已订阅并活跃使用者）。

| 路径 → 订阅意愿(PUI) | 标准化 β | p | 结论 |
|---|---|---|---|
| 感知易用性 PEU | **0.310** | <0.001 | 最强直接效应 |
| 输出质量 OQ | **0.279** | <0.001 | 次强 |
| 社会影响 SI | 0.226 | <0.001 | 显著 |
| 价格价值 PV | 0.197 | 0.003 | 显著但弱于易用性/质量 |
| 感知有用性 PU | 0.172 | 0.017 | 显著 |
| 感知信任 PT | 0.171 | 0.014 | 显著（对应版权/隐私顾虑） |
| 个人创新性 PI | 0.096 | 0.097 | **不显著（假设被拒）** |
| 中介：PEU→PU→PUI | 间接效应 0.1166，95%CI [0.0703, 0.1626] | — | 部分中介 |
| 中介：OQ→PT→PUI | 间接效应 0.0943，95%CI [0.0567, 0.1381] | — | **画质通过建立"信任"间接促付费** |

PM 解读（推断）：**在专业层，"好不好用、稳不稳"比"便不便宜"更决定付费**；而画质→信任→付费这条链，正是版权可追溯、可商用承诺的产品价值所在。

### 2.4 免费额度的商业作用（问题 3）

**为什么几乎所有产品都给免费额度——四条可核验的机制，均有官方/行业依据：**

1. **Credits 是算力配额，也是计价单位。** Adobe 官方帮助页直述："Generative credits provide a way to reflect the additional cost and value of our generative features and give you a way to keep track of how you use them. Additionally, they help to ensure smooth and consistent performance"（更新于 2026-07-15）【S6，A 级】。即：免费额度 = 有意设计的**算力漏斗口**。
2. **免费额度是"用量习惯养成器"，随后用额度收紧逼升级。** Adobe 2025-07-01 将 Single App 月度生成积分从 500 降到 25（**-95%**）【S44，C 级，需二次核实】；同期 Adobe 披露 Q4 FY2025 Generative Credit 消费量同比 **三倍增长**【S24，B】，Q1 FY26 credit 消费环比 **+45%**、Firefly 订阅+credit pack ARR 环比 **+75%**【S25，B】。用量先起来、再收口，是完整闭环。
3. **免费额度用来把"泛用户"转成"日活"，但不必转成付费。** a16z 2025 榜单观察到：AI 视频/图片编辑类占 MAU 榜与收入榜均 >20%，但**两榜重叠率仅 40%**——"大众化应用用户多，专业化应用更易激发付费意愿"【S27，B】。免费层的真实产出是**分发与数据**，不是直接收入。
4. **反例证明边界。** Midjourney **明确无免费层**，最低 $10/月（官方文档）【S7，A】，且规定年毛收入 >$100 万的公司必须买 Pro($60) 或 Mega($120)【S7，A】——说明**当产品定位是"专业生产力"而非"大众分发"时，可以完全不做免费额度**，代价是放弃漏斗顶部。

**免费额度的具体形态（2025-2026 快照）**

| 产品 | 免费额度 | 付费起步 | 等级 |
|---|---|---|---|
| Adobe Firefly | Free 档："Get free daily generations"（每日免费生成，限部分模型） | Standard $9.99/月（2000 credits） | A【S5】 |
| Midjourney | **无**（最低 $10/月） | Basic $10/月 | A【S7】 |
| Leonardo.AI | 150 tokens/天（约 30-75 张/天）；免费档**含水印、生成公开、无商用权** | Apprentice $12/月（8500 tokens/月） | C【S36】 |
| Ideogram | 免费档每天约 10 张慢速图（另一来源称 25 张/天，口径分歧） | Basic $7-8/月 | C【S36】 |
| 即梦 | 免费版每日赠送积分（第三方记录：每日约 88 积分，视频 5 积分起） | 基础会员 79 元/月（725 积分） | B【S37】+C |
| 可灵 | 免费版签到得"灵感值"；全球版约 66 积分/天 | 黄金会员 66 元/月（660 灵感值） | B【S37】+C |

**免费转付费漏斗（问题 3 的第二半）**

- 通用 SaaS freemium 免费→付费转化率行业区间 **2%–5%**（引 Statista/Paddle 系二手汇总）【S38，**C 级**】。
- **AI 绘画产品的免费→付费转化率：无任一厂商或第三方公开披露 → `[待确认]`。** 唯一可得的替代口径是美图"付费订阅/MAU"的 5.9%–9.0%【S1】，但那是"存量渗透率"而非"漏斗转化率"，**不可直接等同**。
- Midjourney 因无免费层，不存在免费→付费漏斗；其"转化"逻辑是 Basic($10) → Standard($30) 的**升档**，官方未披露升档率 → `[待确认]`。

### 2.5 用户流失 / 弃用原因（问题 5）

证据等级整体偏弱（多为 UGC/评测），**面试中应表述为"公开可观察到的抱怨主题"，而非"调研结论"**。

| 弃用原因 | 可核验证据 | 等级 |
|---|---|---|
| 手部/文字/解剖畸形、质量不稳定 | Trustpilot 一名付费超 2 年用户："Their new model (V7) is terrible. It can't draw hands, can't render basic text, and often produces deformed results."（2025）【S39】 | C（UGC） |
| 内容审核过严 / 账号封禁不可预期 | 同篇："You can now get banned not just for what you generate on the platform, but for comments you make off-platform"；Midjourney 官方回复称封禁系"repeated Terms of Service violations after multiple warnings"【S39】 | C（UGC，含官方回应） |
| 无 API、无法接入自动化 | 开发者评测："the bigger blocker is the lack of a public API... makes it hard to integrate Midjourney into pipelines"（2025）【S39】 | C |
| 无免费层 + 隐私功能（Stealth）被高价位锁定 | "Stealth Mode—hiding generations from public view—locked behind the $60 Pro tier... feels like table stakes rather than a luxury feature"（2025）【S39】 | C |
| 竞品替代（多模态打包更划算） | "OpenAI released its latest image generator, and it performs far better... if you cancel your subscription, your remaining credits disappear"（Trustpilot，2025-05）【S39】 | C（UGC） |
| 登录/计费等基础体验 | "The company cannot even provide a basic email-and-password login system... forced to log in through Discord or Google"（Trustpilot 年度续费取消案例）【S39】 | C（UGC） |
| 风格同质化 / 版权顾虑 | 插画师群体：32.4% 插画师报告因生成式 AI 丢失委托（AOI 2025，>1 万名创意工作者）【S21，B】；AOP 2026-01 调研：58% 专业摄影师因生成式 AI 失去工作、95% 意识到自己风格可被复制【S21，B】 | B |
| 开发者/美术群体情绪反弹 | GDC 2026 报告：视觉与技术美术中 64% 认为生成式 AI 是负面力量，仅 7% 正面（2025 为 13%）【S45，**C 级单一来源，谨慎**】 | C |

> **证据薄弱提示**：以上**没有任何一条来自厂商官方流失调研或第三方留存面板**（Sensor Tower/Similarweb 的 AI 绘画 App D30 留存数据未公开可得）。NPS 数据：`[待确认]`，未检索到任一 AI 绘画产品的公开 NPS。

---

## 3. 替代关系价格对比表（问题 4）

> **口径统一说明**：下表三项价格来源等级不一致（图库 C 级抓取、外包插画 C 级自媒体、AI 官方定价 A/B 级），**币种、timepoint、是否含授权费各不相同**，只可用于量级比较，不可用于精确 TCO 模型。

### 3.1 一张图库图多少钱

| 渠道 | 单价 | 币种 | timepoint | 口径 | 等级 |
|---|---|---|---|---|---|
| Shutterstock 订阅（350 张/月） | **$0.57/张**（$199/月） | USD | 2025 | 订阅摊薄价 | C（优惠券聚合站抓取）【S28】 |
| Shutterstock 订阅（750 张/月） | **$0.33/张**（$249/月） | USD | 2025 | 订阅摊薄价 | C【S28】 |
| Shutterstock 按需包（25 张） | **$9.16/张**（$229） | USD | 2025 | 一次性 | C【S28】 |
| Shutterstock 入门订阅（10 张/月） | **约 $2.90/张**（$29/月） | USD | 2025 | 多处二级源一致的转述 | C |
| Adobe Stock（10 张/月） | 约 **$2.99/张**（$29.99/月） | USD | 2025 | 转述 | C |
| Getty Images | **$50–$500+/张**（独家/编辑内容更高） | USD | 2025 | 转述，区间宽 | C【聚合站，多家口径不一】 |

### 3.2 一张外包插画多少钱（以儿童绘本为可比锚点，因与教育出版落点直接相关）

| 供给方分层 | 单张报价 | 整本（24–32 页） | 币种 | timepoint | 等级 |
|---|---|---|---|---|---|
| 新手/新兴插画师 | **$50–$150/张** | — | USD | 2025 年末 | C（插画师自营站）【S30】 |
| 中坚职业插画师 | **$150–$350/张** | **$2,500–$6,000** | USD | 2025 年末 | C【S30】 |
| 资深/出版社级 | **$400–$1,000+/张** | **$3,000–$15,000+** | USD | 2025 | C【S30】【S31】 |
| 低成本外包工作室口径 | **$10–$50/张**（2D 平涂 $10–15/页，写实 $30–50/页） | **$300–$1,500**（32 页） | USD | 2025–2026 | C（外包服务商自营站）【S29】 |

> **严重分歧提示**：同为"儿童绘本插画"，两家 C 级来源给出的单张价差达 **10 倍**（$10–50 vs $50–1000）。原因是层级口径（自由职业个人 vs 外包工厂）不同。**面试中不要给单一数字，给区间 + 说明层级差异。**

**替代侧的行业冲击证据（B 级，比价格本身更可靠）**：
- 英国 AOI 2025 年对 **1 万余名创意工作者**的调研：**32.4% 的插画师报告因生成式 AI 丢失委托**，丢失的主要是封面、概念图、营销图等"饭碗活"【S21，B】。
- 英国 AOP 2026-01 会员调研：**58% 专业摄影师正在因生成式 AI 失去工作**；95% 意识到自己的风格可被复制【S21，B】。
- 英国 ONS：使用"视觉内容 AI"的企业中，**超过一半报告对创意与设计岗位产生影响**（2026-06，16% 企业使用视觉内容 AI）【S21，B】。注意：ONS 口径为企业雇员，**不含自由职业外包**，故真实影响被低估。
- 个案（UGC，C）：英国插画师 Neil Stevens："There was a time I would be earning £80-90k plus. This year I'll barely make £10k."（12 年资历，2025）【S22】；Daniel Fishel："In 2020, I invoiced 77 assignments... So far this year, I've invoiced 22."【S22】
- 中国侧个案（C）：插画师自述头图类单张报价"从 300 元压到 80 元上下"（2025）【C 级自媒体】——**仅作趋势 anecdote，不作为数据引用**。

### 3.3 一张 AI 生成图多少钱

| 路径 | 单价 | 币种 | timepoint | 等级 |
|---|---|---|---|---|
| **Gemini 3 Pro Image API 官方输出价** | **$0.134/张（1K/2K）、$0.24/张（4K）** | USD | 2026 官方定价页 | B（Google 官方定价，经多二级源一致转述）【S32】 |
| 同上，Batch 模式 | **$0.067 / $0.12**（半价） | USD | 2026 | B【S32】 |
| Nano Banana 2（Gemini 3.1 Flash Image） | **$0.067（1K）/ $0.101（2K）/ $0.151（4K）** | USD | 2026 | B【S32】 |
| Midjourney Standard 摊薄（第三方估算 ~900 张/15 GPU 小时） | **约 $0.033/张**（$30 ÷ 900）【本文推算】 | USD | 2026 | 分子 A（官方定价）／分母 C（第三方估算张数）→ **整体 C，谨慎** |
| 国内视频向（可灵 API） | 约 **¥1.36/次**（3.0 Turbo） | CNY | 2025 | C【S37 周边转述】 |

### 3.4 电商摄影：替代关系最彻底的一段（有厂商自报的成本对比）

| 项目 | 传统实拍 | AI 生成 | 币种 | timepoint | 等级 |
|---|---|---|---|---|---|
| 一套服装图（4 套服装+3 场景，含化妆/场地/后期） | **¥1,500–2,800** | **¥80–300**（1920×2560 高清） | CNY | 2025 | C【S33】 |
| 单张产品图 | **¥300–3,000+** | 订阅摊薄后"几分到几毛钱" | CNY | 2025 | C（AI 厂商营销页，self-interested）【S34】 |
| 模特日费 | **¥1,000–10,000+/天** | 内置虚拟模特 | CNY | 2025 | C【S34】 |
| 单 SKU（国际口径） | **$20–150/SKU**；拍摄日 $2,500–10,000+ | **$0.75–2/张** | USD | 2025 | C（AI 厂商营销页）【S35】 |
| **中国官方口径（更可信）** | 某户外鞋类旗舰店："以前制作一套图需要拍图、切图、P图、修图，成本大概需要 **1500 元**。用了生意管家'智图'里的'鞋靴替换'工具，**1 个小时**就能做好一套图，都是低成本，甚至免费的" | — | CNY | 2025-09 | B（淘天官方口径，媒体报道）【S13，self-reported by 商家】 |
| 童装商家（年拍摄预算 200 万元） | — | "可以省掉 **50% 以上**的拍摄成本" | CNY | 2025-09 | B【S13】 |
| 天猫"家作"（家居家装） | 传统搭景+找模特+实拍 **2–3 天** | **几分钟**完成 | 时长 | 2025-03 | B【S14】 |
| 慕思（品牌侧） | — | 近一年采纳 AI 场景图近 2000 张（含模特 900+），相比传统模式"省了 **140 多万元**设计成本" | CNY | 2025-03 | B（品牌方口述）【S14】 |
| 平台侧总账 | — | 生意管家 AI 素材截至 2025-08 底"已为商家节省了 **140 亿元**的直接成本"；累计生成 8.7 亿张图、月活商家近 200 万 | CNY | 2025-08 | B（淘天 self-reported）【S13】 |
| 阿里妈妈万相营造 | — | "已助力百万商家生成营销素材超 1 亿条，累计节省制作成本突破 **100 亿元**" | CNY | 2025-09 | B（阿里 self-reported）【S12】 |

> **注意**：140 亿 / 100 亿这类"累计节省额"是**平台自报的替代额**（把"如果不是 AI 就要花钱拍"折算成钱），方法论未披露，只可用于说明方向，不可用于 ROI 论证。

### 3.5 替代关系结论（可核验部分）

1. **图库是被替代最直接的一层**：订阅摊薄价 $0.33–2.90/张【C】 vs AI 官方 API $0.067–0.24/张【B】——量级上 **AI 单张成本已进入图库订阅价区间内或更低**，且 AI 图不撞图。
2. **外包插画是被替代最痛苦的一层**：32.4% 插画师报告丢单（AOI 2025，B 级）【S21】；但**高端署名作品价格反向走高**（个案 anecdote，C 级，不作为结论）。
3. **电商摄影是被替代最彻底的一层**：有中国平台与品牌双方可核验的成本/时长对比【S13】【S14】。
4. **尚未被替代的**：需要"谁画的"构成价值的部分（署名风格、定稿判断）、需要物理真实性的高端品类（珠宝镜面折射等，C 级厂商自述承认）。

---

## 4. 教育出版落点专节（用户熟悉的垂直场景）

### 4.1 用户到底是谁（4 类决策/执行角色）

| 角色 | 真正要完成的任务（JTBD） | 关键约束 |
|---|---|---|
| **出版社美术编辑 / 插画编辑** | 按文字稿配图，控制**整本书风格统一**，在**出版周期**内交付，**过审** | 印前分辨率、CMYK 转换不塌、图文配合 |
| **教辅策划 / 选题策划** | 在预算内把一册/一套的配图量做出来，压缩**时间与费用**双成本 | 教材定价"保本微利"，单价敏感 |
| **插画工作室 / 美术团队** | 用 AI 出底稿+变体，人工做**风格统一、细节修正、印前处理** | 版权合规、细节准确性、不能整包交给 AI |
| **学校老师 / 教研员** | 为课件、习题、校本材料找**能说清知识点**的图 | 事实准确性、价值观/意识形态安全、本地化 |

### 4.2 可核验的场景数据（这是本垂直场景最硬的一条）

来源：全国少儿社长会公开内容，童趣出版案例（B 级，百道网/网易双源一致）【S15】：

> "比如，童趣的分级诵读绘本《小步日诵》，如采用手工绘制插画，全书共需要 **384 张图**，以一人一天一张图计算，最短需要 **4 位插画师用时 4 个多月**完成。而采用生成式人工智能技术绘图，**时间成本节省 60%，费用节约了 68%**，极大地降低了出版成本。"

同一来源明确写出**人工必须主导**的三件事：

> "使用生成式人工智能绘制插画仍需要人工介入与主导，保障插画**风格的统一性、版权合规性和细节准确性**。"

> "美术团队和编辑团队需要储备关于少儿读物插画的专业知识，提升**提示词输出能力**，并在已生成的基础插画上发挥个人优势，有所创新。"

以及审校环节的机制结论：

> "智能审校作为基础辅助工具效果显著但存在算法盲区，少儿读物内容的安全合规仍离不开人工审校，'**三审三校+智能预审**'的混合机制在保证审校效率与质量之间找到了关键平衡点。"

**推断出的量化口径（PM 可用，需注明来源）**：384 张图的绘本，手绘基线 ≈ 4 人 × 4 个多月；AI 后费用 -68%。若按中坚插画师 $150–350/张【S30，C 级】估算，384 张手绘基线约 40 万–94 万元人民币，AI 后约 13 万–30 万元——**此换算为本文推算，跨来源拼接（B×C），不可作为对外数据**。

### 4.3 与通用 AI 绘画产品的需求差异（4 条硬差异，每条有出处）

| 差异点 | 通用 AI 绘画产品的默认 | 教育出版的硬要求 | 依据 |
|---|---|---|---|
| **角色一致性** | 单张即交付；跨图一致性是"加分项" | **跨页、跨册、跨学段同一人物/形象必须一致**（一套教材/一个 IP 角色要用几年） | 插画环节"保障插画风格的统一性"为人工必须介入项【S15，B】 |
| **印前分辨率** | 屏幕级（1K/2K）为主；API 官方定价到 4K 才 $0.24/张【S32】 | **印刷级**（300dpi 以上、CMYK 不塌）；AI 常见鲜艳渐变在 CMYK 下会崩 | 教材须"插图质量高，图文配合得当"（教育部《中小学教材管理办法》第九条）【S16，A】；印刷塌陷为 C 级实务提示【S43】 |
| **版权可追溯** | 商用条款各产品不一；Leonardo 免费档**无商用权**、生成公开【S36】；Midjourney 年营收 >$100 万公司须 Pro/Mega【S7】 | 必须**可证明训练数据合规、可出具授权链**，因为教材要进国家审定、要重印多年 | 教材"符合知识产权保护等国家法律、行政法规"【S16，A】；送审须提交政治审核情况报告【S17，A】 |
| **审校合规** | 无审核环节 | **三审三校 + 智能预审**，AI 无法替代意识形态与价值观判断 | 【S15，B】【S16，A】；教育部 2025 年提出"制定数字教材建设和管理指导意见"【S48，B】 |

### 4.4 政策侧的硬边界（做这个场景必须记住的两条 A 级事实）

- **《中小学教材管理办法》**（教育部，教材〔2019〕3 号）："国家实行中小学教材**审定制度**，未经审定的教材，不得出版、选用"；编写修订要求包含"**插图质量高，图文配合得当**，可读性强"；"教材定价应严格遵守'**保本微利**'原则"【S16，A】。
  → PM 含义：教材插图不是"买图"决策，是"过审"决策；且**支付方预算被"保本微利"锁死**，AI 的价值必须落在**降本**而非提价。
- **《广东省中小学地方课程教材管理实施细则》**（粤教基〔2025〕6 号，2025-06-13 施行）：送审必须提交"政治审核情况报告"、教材清样须"文图全部定稿"；审核分初审/复审，复审未通过"必须立即停止试验"【S17，A】。
  → PM 含义：地方教材/教辅的配图一旦定稿即冻结，**返工成本极高**，所以"一次做对"比"快速出图"更值钱。

### 4.5 该场景的产品机会（推断，非引用事实）

基于 4.2–4.4 推出的三条产品判断，标注为 PM 推断：
1. **角色/风格锁定的资产库**（一次训练，全册复用，导出可印前的分层文件）比"更好的出图模型"更接近真实付费点——依据：风格统一是人工必须介入项【S15】。
2. **印前规格前置到生成环节**（分辨率、CMYK 预览、出血位）——依据：教材插图质量要求为 A 级硬约束【S16】。
3. **可审计的生成日志**（prompt/模型版本/时间戳/参考图来源）作为交付物的一部分——依据：送审要政治审核报告【S17】+ 知识产权合规【S16】；且这与【S8】发现的"输出质量→感知信任→付费"链路同构。
4. **教辅（非教材）比教材更快落地**：教材受国家审定约束（A 级硬约束）【S16】，而教辅/绘本/课件属市场化品种，童趣案例正是**绘本**而非教材【S15】。

---

## 5. 3–5 条可下注判断（每条挂引用）

### 判断 1：AI 绘画的付费率天花板约在 6%–9%（存量渗透口径），生产力场景是唯一能把它推到 9% 以上的杠杆。
证据：美图官方财报，2025-12-31 整体订阅渗透率 6.1%，生活/娱乐 5.9%，生产力工具 9.0%（且 +3.1p.p.，是三层中提升最快的）【S1，A】。生产力付费用户同比 +67.4%，远高于生活场景 +30.3%【S1，A】。
→ **可下注**：做 AI 绘画产品，把用户从"娱乐"推向"某个能算清 ROI 的具体工作流"，付费率有 1.5 倍空间（9.0/5.9 = 1.53【本文推算】）。
→ **风险**：单一公司样本 `[SINGLE_SOURCE]`；美图是移动端影像工具，与桌面/专业工具的可比性有限。

### 判断 2：专业层付费由"可控与稳定"驱动，不由"便宜"驱动；价格战打不动这一层。
证据：N=394 数字媒体设计师 CB-SEM，感知易用性 β=0.310、输出质量 β=0.279，**均高于**价格价值 β=0.197；且存在"输出质量→感知信任(β=0.392)→订阅意愿"的显著中介（间接效应 0.0943，95%CI [0.0567,0.1381]）【S8，A】。
→ **可下注**：面向专业层的产品，**把预算花在一致性/可控性/可追溯（即"信任"）上，边际收益高于降价**。
→ **反证风险**：样本全为"已订阅活跃用户"（100%），结论只解释**续费与升档意愿**，不解释"从 0 到 1 的付费转化"。

### 判断 3：免费额度是"算力闸门 + 习惯养成器"，不是获客赠品；收口时点就是变现时点。
证据：Adobe 官方直述 credits 用于反映"additional cost and value"并保证性能平稳【S6，A】；Adobe 将 Single App 月生成积分从 500 降至 25（-95%，2025-07-01）【S44，C，需核实】；同期 Generative Credit 消费量 Q4 FY25 同比三倍【S24，B】、Q1 FY26 环比 +45%，Firefly 订阅+credit pack ARR 环比 +75%【S25，B】。
→ **可下注**：额度设计应当"先用 unlimited 标准档养习惯 → 把 premium（高清/视频/第三方模型）设成付费闸门"，这与 Adobe 现行结构一致【S5，A】。
→ **反证**：Midjourney 完全无免费层仍做到约 5 亿美元年收入（C 级估算）【S40】【S7】——说明**强品牌 + 强社区可以跳过免费层**，但不可复制为通用策略。

### 判断 4：被替代最深的是"标准件"图片（图库配图、电商主图、营销素材），不是"署名作品"。
证据：图库订阅摊薄 $0.33–2.90/张【S28，C】 vs Gemini API 官方 $0.067–0.24/张【S32，B】；淘天商家"一套图 1500 元 → 智图 1 小时"【S13，B】；慕思省 140 万元设计成本【S14，B】；另一侧 AOI 2025：32.4% 插画师因生成式 AI 丢单，丢的是封面/概念图/营销图【S21，B】；AOP：58% 摄影师丢单【S21，B】。
→ **可下注**：产品定位应瞄准"标准件工业化生产"（批量、一致、可上架），而非"帮艺术家画画"。
→ **边界**：需要"谁画的"构成价值的部分未被替代（个案 anecdote，C 级，**不足以支撑结论**）。

### 判断 5：教育出版是"高确定性需求 + 强制度约束"的场景，落点应在绘本/教辅/课件，而非国家审定教材；产品护城河是"一致性 + 印前 + 可审计"，不是模型能力。
证据：童趣《小步日诵》384 张图，AI 后时间成本 -60%、费用 -68%，但仍须人工保障"风格统一性、版权合规性、细节准确性"【S15，B】；教材须国家审定、插图质量高、定价保本微利【S16，A】；地方教材送审须提交政治审核情况报告且文图定稿后返工成本极高【S17，A】；教育部 2025 年推进"制定数字教材建设和管理指导意见"【S48，B】。
→ **可下注**：若做教育出版方向，**从教辅/绘本/课件切入**（市场化定价、无国家审定硬门槛），把"角色一致性资产库 + 印前规格 + 生成日志可审计"做成产品三件套。
→ **风险**：该场景的付费能力受"保本微利"压制【S16】，**客单价可能低于通用生产力场景**；且除【S15】外缺乏第二个独立来源，`[SINGLE_SOURCE]`。

---

## 6. 来源清单

| # | 来源 | 类型 | 等级 | URL | 直接引文（quote） |
|---|---|---|---|---|---|
| S1 | 美图公司《截至2025年12月31日止年度业绩公告》（港交所披露易） | 上市公司财报 | **A** | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032700842.pdf | "Paying subscribers exceeded 16.91 million, including 2.16 million from Productivity tools. Paying Subscribers 16.91 / 12.61 (+34.1%)… Subscription Rate 6.1% (2024: 4.7%)… Products for leisure 5.9%… Productivity tools 9.0%" |
| S2 | 美图公司官网 2025 年度业绩稿 | 公司新闻稿（self-reported） | A（财务数据源） | https://www.meitu.com/zh/media/436?from=media | "截至2025年12月31日，美图公司付费订阅用户数达1691万创历史新高，同比增长34.1%；订阅渗透率为6.1%" |
| S3 | 新华网客户端《美图公司2025年度业绩》解读 | 官方媒体 | B | https://app.xinhuanet.com/news/article.html?articleId=20260331afd2b98440584bbdb22cbe522eea38c6 | "在'美图设计室'产品中…该产品Web端电商代理平均每生成2张内容，即可产出1张用户满意并保存的成品"（公司 CPO 口述，self-reported） |
| S4 | TechCrunch《Canva gets to $4B in revenue as LLM referral traffic rises》 | 头部科技媒体 | B（数据为 COO 口述，self-reported） | https://techcrunch.com/?p=3090294 | "Canva had more than 265 million monthly active users and over 31 million paid users in 2025, according to the company… annual recurring revenue to $4 billion… its B2B business, which accounts for companies with more than 25 seats, grow by 100% with $500 million in ARR." |
| S5 | Adobe 官方 Firefly 产品定价页 | 厂商官方 | **A** | https://www.adobe.com/products/firefly.html | "Firefly Free — Get free daily generations to quickly create video, audio, and images. Free / Firefly Standard — Get 2,000 credits… US$9.99/mo / Firefly Pro — 4,000 credits… US$19.99/mo / Firefly Pro Plus — 10,000 credits… US$49.99/mo" |
| S6 | Adobe 官方《Generative credits FAQ》（更新 2026-07-15） | 厂商官方 | **A** | https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html | "Generative credits provide a way to reflect the additional cost and value of our generative features and give you a way to keep track of how you use them. Additionally, they help to ensure smooth and consistent performance of our products and features across all users" |
| S7 | Midjourney 官方文档《Comparing Midjourney Plans》 | 厂商官方 | **A** | https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans | "Monthly Price: $10 / $30 / $60 / $120… Fast GPU Time: 3.3 hr/month / 15 hr/month / 30 hr/month / 60 hr/month… You must purchase the Pro or Mega plan if you are a company making more than $1,000,000 USD in gross revenue per year." |
| S8 | Hu L., Chen M., Ding N.《Factors influencing digital media designers' subscription to premium versions of AI drawing tools》*Scientific Reports* 15 (2025) | 同行评议学术论文 | **A** | https://www.nature.com/articles/s41598-025-99924-7 （PMC12062495） | "perceived ease of use indirectly influences subscription intention through perceived usefulness, while output quality affects it through the mediating role of perceived trust. Social influence, price value, and perceived trust all exhibit significant positive effects on subscription intention, whereas personal innovativeness does not demonstrate a statistically significant impact."（β 值见正文 2.3） |
| S9 | CNNIC《生成式人工智能应用发展报告(2025)》（中国政府网/新华社） | 国家机构统计 | **A** | https://www.gov.cn/yaowen/liebiao/202510/content_7044952.htm | "截至2025年6月，我国生成式人工智能用户规模达5.15亿人，较2024年12月增长2.66亿人，用户规模半年翻番；普及率为36.5%" |
| S10 | QuestMobile《2025年中国移动互联网年度大报告》（中国高新技术产业导报报道） | 第三方数据机构 | B | http://www.chinahightech.com/yaowen/2026-03/23/content_490800.html | "截至2025年12月，移动端AI应用、手机厂商AI助手、PC端AI应用的月活跃用户规模，分别达到7.22亿、5.59亿、2.05亿…AI原生类APP月人均使用时长达到143.2分钟，已远超工具类、拍摄美化类APP" |
| S11 | 新华社《淘宝天猫搜推智能总裁凯夫：做好用的AI…》 | 国家通讯社（数据为平台 self-reported） | B | https://www.news.cn/tech/20251016/70618f80c7f5414b9f83765f3a2d4be8/c.html | "淘宝还为商家组建AI经营团队…数据显示：AI美工月均生成2亿张图片/500万个视频，商品点击率提升10%" |
| S12 | 中国经济新闻网《阿里妈妈万相营造入选2025服贸会示范案例》 | 行业媒体（数据为阿里 self-reported） | B | https://www.cet.com.cn/itpd/itxw/10257298.shtml | "已助力百万商家生成营销素材超1亿条，累计节省制作成本突破100亿元" |
| S13 | 腾讯网转载《AI重塑经营体验：淘天为商家按下"减负键"》 | 媒体（数据为淘天/商家 self-reported） | B | https://new.qq.com/rain/a/20250928A05W4M00 | "该AI套件目前已累计生成8.7亿张图片，月均活跃商家近200万，覆盖平台超2亿商品。截至8月底，仅生意管家AI素材一项，已为商家节省了140亿元的直接成本"；"以前制作一套图需要拍图、切图、P图、修图，成本大概需要1500元。用了生意管家'智图'…1个小时就能做好一套图" |
| S14 | 封面新闻《平台为商家配备AI助手 可一键生成媲美实拍场景图 还带模特》 | 媒体（品牌方口述，self-reported） | B | https://www.thecover.cn/news/rIwZw13d4yiH90qSdq8Jkw== | "通过家作AI采纳的场景图有近2000张，其中带模特的有900多张，相比用传统模式，省了140多万元的设计成本"；"'家作'上线运营一年，有超13万商家使用" |
| S15 | 百道网/网易《AI如何重构少儿出版生产流程——全国少儿社长会》 | 行业媒体（双源一致） | B | https://m.bookdao.com/Article.aspx?id=441080 ； https://www.163.com/dy/article/K1AIQBI00512DFEN.html | "童趣的分级诵读绘本《小步日诵》，如采用手工绘制插画，全书共需要384张图…最短需要4位插画师用时4个多月完成。而采用生成式人工智能技术绘图，时间成本节省60%，费用节约了68%"；"使用生成式人工智能绘制插画仍需要人工介入与主导，保障插画风格的统一性、版权合规性和细节准确性" |
| S16 | 教育部《中小学教材管理办法》（教材〔2019〕3号） | 政府规章 | **A** | https://baike.baidu.com/item/%E4%B8%AD%E5%B0%8F%E5%AD%A6%E6%95%99%E6%9D%90%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95/24254340 | "国家实行中小学教材审定制度，未经审定的教材，不得出版、选用"；"语言文字规范，插图质量高，图文配合得当，可读性强"；"教材定价应严格遵守'保本微利'原则" |
| S17 | 《广东省中小学地方课程教材管理实施细则》（粤教基〔2025〕6号，2025-06-13 施行） | 地方政府规章 | **A** | https://edu.gd.gov.cn/zwgknew/jyzcfg/gfxwj/content/post_4719442.html | "教材清样必须是全套教材，文图全部定稿且完整、清楚、整齐"；送审材料须含"政治审核情况报告"；"复审未通过的教材，必须立即停止试验" |
| S18 | CESA（日本计算机娱乐供应商协会）2025 行业报告（经 The Nikkei / 二级转述） | 行业协会调研 | B | https://completeaitraining.com/news/51-of-japanese-game-companies-use-ai-in-development-tokyo/ | "51% of surveyed domestic game companies are using generative AI in development. The survey covered 54 Japanese studios from June-July 2025… The top use is visual asset generation (characters, props, backgrounds)" |
| S19 | Unity《2026 年游戏开发报告》（Cint 调研，300 位开发者） | 厂商/机构调研 | **A**（厂商官方报告） | https://www.unity.com/resources/gaming-report | 受访者使用 AI 工具的用途分布："编码辅助62%、写作与叙事设计44%、NPC行为40%、市场研究37%、自动化游戏测试35%、概念艺术和游戏资产35%" |
| S20 | Totally Human Media Steam 生成式 AI 报告（经 PCGuide、eloutput 转述） | 第三方数据机构 | B | https://www.pcguide.com/news/new-report-claims-nearly-1-in-5-games-released-on-steam-in-2025-use-ai-generated-content/ | "nearly 1 in 5 games released on Steam in 2025 used generative AI… that number has exploded to over 7,800 games, a nearly 700% increase"；"The most common use is for visual assets… This alone makes up about 60% of the AI use in games on Steam" |
| S21 | Creators' Rights Alliance 汇总 ONS / AOI(2025) / AOP(2026-01) 数据 | 行业组织 | B | https://www.creatorsrightsalliance.org/latest-news/new-ons-data-finds-ai-affecting-creative-roles | "over half of businesses using 'visual content AI' report an impact on creative and design roles"；"32.4% of illustrators in a large-scale survey reported losing work commissions to generative AI (Association of Illustrators 2025)"；"58% of professional photographers are losing work to generative AI… 95% of AOP members said they were aware their photographic style can be replicated" |
| S22 | designs-now《…things are really tough for illustrators right now》 | 行业媒体（从业者口述） | C | http://www.designs-now.com/article/120570/no-youre-not-imagining-it-things-are-really-tough-for-illustrators-right-now | "There was a time I would be earning £80-90k plus. This year I'll barely make £10k. It's fallen off a cliff."（Neil Stevens, 12 年资历插画师，2025） |
| S23 | SiliconANGLE《Adobe beats earnings expectations as AI tools drive double-digit revenue growth》 | 科技媒体（财报转述） | B | https://siliconangle.com/?p=724670 | "For the full fiscal year 2025, Adobe reported… revenue of $23.77 billion, up 11% year-over-year"；"Total Adobe ending ARR: $25.2 billion, growing 11.5% year-over-year"（Investing.com 电话会转述） |
| S24 | PetaPixel《Adobe's Revenue Breaks Yet More Records as It Closes Out 2025》 | 行业媒体（财报转述） | B | https://petapixel.com/2025/12/10/adobes-revenue-breaks-yet-more-records-as-it-closes-out-2025/ | "what it calls 'AI-influenced Annual Recurring Revenue (ARR)' is now over one third of its overall business… it saw Generative Credit consumption… tripled in Q4 2025" |
| S25 | 招银国际《A股传媒行业研究》引 Adobe 1QFY26 财报 | 券商研报 | B | https://ima.qq.com/wiki/?shareId=0602522abd18fa3d1e94b4d7158fbe8d45b2975c68ad8401f1b597e4ab6fdd37 | "据Adobe1QFY26财报披露，Firefly相关产品(含Firefly应用、Credit pack及FireflyEnterprise) ARR已突破2.5亿美元。其中，Firefly订阅及Credit pack ARR环比增长75%，Generative credit消费量环比增长超45%…目前，Firefly收入占公司总收入比例约1%" |
| S26 | 高盛预测（经中国证券网转述） | 投行预测 | B | https://m.cnstock.com/commonDetail/658807 | "高盛预计，2025年-2030年全球AI图像/视频工具市场将以44%的年复合增长率增长，从2025年的60亿美元增至2030年的390亿美元" |
| S27 | a16z《Top 100 Gen AI Consumer Apps》（经光明网、智源社区转述） | 头部 VC 榜单 | B | https://tech.gmw.cn/2025-08/28/content_38249616.htm ； https://hub.baai.ac.cn/view/43999 | "美图公司有5款产品入选全球移动应用Top 50榜单"；"50大活跃应用与50大收入应用的榜单重叠率仅40%…大众化应用用户多，专业化应用更易激发付费意愿" |
| S28 | Shutterstock 价格抓取（sanely.cc） | 聚合站 | C | https://sanely.cc/na-en/shop/shutterstock/coupons | "Subscribe for 50 Images at Just $125/Month… $2.50 per image"；"Access 350 Images for Just $199/Month… you pay only $0.57 for each image"；"On-demand Pack - 25 Images for $229… just $9.16 per image" |
| S29 | Kidillus《Children's Book Illustration Cost: 2026 Pricing Guide》 | 外包服务商自营内容 | C | https://kidillus.com/blog/childrens-book-illustration-cost-2026 | "Most professional illustrators price per illustration… $10–$50 per illustration / $300–$1,500 total for a standard 32-page children's book" |
| S30 | AnantaArt《How Much Does a Children's Book Illustrator Actually Cost in 2025?》 | 插画师自营内容 | C | https://www.anantaart.com/childrens-book-illustrator-actually-cost/ | "New or emerging illustrators: $50–$150 per illustration / Established mid-level professionals: $150–$350 per illustration / Highly experienced specialists: $400–$1,000+ per illustration… between $2,500 and $6,000 for a full 24–32 page picture book" |
| S31 | Craft2Publish《Children's Illustrator Cost…2025》 | 外包服务商自营内容 | C | https://craft2publish.com/childrens-illustrator-cost-best-illustrators-3d-animation-services-2025/ | "Professional illustrators: $200 – $500 per page / Top illustrators: $1000+ per page… For an entire book, costs often range between $3,000 and $15,000+" |
| S32 | Google Gemini API 图像定价（经 aifreeapi / uxmagic / pixmind 多源一致转述） | 二级源转述官方定价 | B | https://uxmagic.ai/blog/nano-banana-pro-vs-nano-banana-2 ； https://www.pixmind.io/posts/nano-banana-pro-pricing-guide-2026 | "Nano Banana Pro works out to about $0.134 per 1K or 2K image and $0.24 per 4K image. Nano Banana 2 is about $0.045 at 512px, $0.067 at 1K, $0.101 at 2K and $0.151 at 4K. Batch mode roughly halves both." |
| S33 | 大数跨境《AI电商模特图片高清》 | 跨境行业百科 | C | https://www.10100.com/encyclopedia/6/55918054 | "传统摄影棚拍摄一套4套服装+3场景的模特图，成本约为¥1,500–2,800元…而AI生成同等数量高清图(1920×2560分辨率)，成本可压缩至¥80–300元" |
| S34 | Photta《AI 还是传统实拍？电商产品摄影的成本、效率与 ROI 全方位对比》 | AI 厂商营销内容（self-interested） | C | https://www.photta.app/zh/blog/ai-vs-traditional-product-photography-comparison | "单价：每张图约 ¥300 - ¥3000+"（传统实拍）；"模特拍摄：需雇佣模特（¥1000 - ¥10000+/天）" |
| S35 | Veeton《AI Photoshoots vs Traditional Methods》 | AI 厂商营销内容（self-interested） | C | https://veeton.com/blog/ai-photoshoots-vs-traditional-methods-for-e-commerce-product-photography | "A shoot day runs $2,500 to over $10,000, roughly $20 to $150 per SKU… An AI photoshoot generates studio-quality product images… for roughly $1 to $2 each" |
| S36 | AI Free Forever《Ideogram vs Leonardo AI Review, Pricing and Free Features》/ BestAICompared | 聚合测评 | C | https://aifreeforever.com/blog/ideogram-vs-leonardo-ai-review-pricing-and-free-features ； https://bestaicompared.com/?p=247/ | "Free Plan: 150 tokens daily (refreshes every 24 hours)… Public generations only / No commercial rights"（Leonardo）；"Free Plan: 10 slow images daily"（Ideogram） |
| S37 | 中国银河证券研究院《2026年Token…报告》（表格，经转载） | 券商研报 | B | https://ima.qq.com/wiki/?shareId=6c106937365703608a288f7260d2a247b9348ea7406b6675fd91383b3664e91a | "即梦｜免费 & 订阅｜免费版每天赠送积分 基础会员：79元/月，725积分；标准会员：239元/月，2210积分；高级会员：649元/月，6160积分"；"可灵｜免费 & 订阅｜免费版通过签到可获得一定'灵感值'。黄金会员：66元/月，660灵感值" |
| S38 | AppScaleLab《Freemium Models: 2025's 2-5% Conversion Reality》（引 Statista/Paddle 系二手汇总） | 聚合站 | C | https://appscalelab.com/freemium-models-2025-s-2-5-conversion-reality/ | "A recent report by Statista, based on a 2025 analysis of over 500 SaaS companies, pegged the average freemium conversion rate between a meager 2% and 5%." |
| S39 | Midjourney 用户弃用反馈合集（Trustpilot / AI Forum X / 开发者评测） | UGC | C | https://www.trustpilot.com/users/684b13394e662dff323d43e2 ； https://www.kuroneko-cmd.dev/posts/2025/is-midjourney-worth-30-per-month | "Their new model (V7) is terrible. It can't draw hands, can't render basic text, and often produces deformed results."（Trustpilot，2025）；"the bigger blocker is the lack of a public API… makes it hard to integrate Midjourney into pipelines"（开发者评测，2025） |
| S40 | Midjourney 收入估算（Axis Intelligence / Morphed 聚合） | 聚合站（分析师估算） | C | https://axis-intelligence.com/midjourney-statistics/ ； https://morphed.app/stats/midjourney-statistics | "Midjourney generated an estimated $500 million in revenue during 2025… with approximately 21 million registered users… Axis Intelligence Research estimates approximately 1.39 million paying subscribers" |
| S41 | 《AI四类模型详解：文生视频工具怎么选》（2026-09） | 自媒体 | C | https://ima.qq.com/wiki/?shareId=4be6382efcd9e1d2057b56b2fa65afcf1125fceef3a2bdbda80789667a6f527c | "即梦：每日约88积分，视频5积分起，约17条/日"；"可灵：国内登录送灵感值；全球版免费66积分/天" |
| S42 | Neolemon《Hire an Illustrator or Use AI? Children's Book Guide》 | AI 工具厂商内容 | C | https://www.neolemon.com/blog/hire-an-illustrator-or-use-ai-childrens-book-guide | "The U.S. Copyright Office's January 2025 report says copyright can exist where a human author determined sufficient expressive elements… but not through mere prompting alone." |
| S43 | Text2Img.pro《AI Image Generation for Textbooks & Education (2026)》 | AI 工具厂商内容 | C | https://www.text2img.pro/ai-image-generation-textbooks-education-2026-8/ | "Teams that follow this loop typically cut illustration turnaround by 60–70% while keeping quality control intact."；"Test print conversions — vivid generated gradients often collapse in CMYK" |
| S44 | SQ Magazine《Adobe Creative Cloud Statistics 2026》（聚合 Adobe 官方披露） | 聚合站 | C | https://sqmagazine.co.uk/adobe-creative-cloud-statistics/ | "Adobe Firefly users have generated more than 22 billion assets since the model's March 2023 launch, with 85% of Firefly use occurring inside Photoshop, Illustrator, Premiere Pro, and Express"；"The Single App generative-credit cap dropped from 500 to 25 monthly credits on July 1, 2025" |
| S45 | Best-Games.io《The AI Asset Debate》(引 GDC 2026 报告) | 聚合站 | C | https://best-games.io/articles/2026-03-05-ai-assets-game-development-debate-2026 | "Among visual and technical artists, 64% view generative AI as a negative force… Only 7% of respondents hold a positive view of AI's impact on the industry—down from 13% just one year prior." |
| S46 | 教育部等九部门《关于加快推进教育数字化的意见》（2025-04，经科学网/中新网） | 政府文件转述 | B | https://news.sciencenet.cn/htmlnews/2025/4/542260.shtm | "推动课程、教材、教学数字化变革…制定数字教材建设和管理指导意见"；"加强对智能教育产品、工具、服务监管，规范人工智能应用进校园管理" |
| S47 | Meticulous Research《AI Image Generator Market》摘要页 | 付费报告摘要 | C | https://www.meticulousresearch.com/product/ai-image-generator-market-6009 | "In 2025, the professional/enterprises segment is expected to account for a larger share of over 74.0% of the AI image generator market"；"the marketing and advertising segment is expected to account for the largest share of over 36.0%" |
| S48 | Dataintelo《AI Art Generators Market》摘要页 | 付费报告摘要 | C | https://dataintelo.com/report/global-ai-art-generators-market | "the Media and Entertainment sector dominated the AI art generators market in 2025 with approximately 34.2% revenue share… The Education end-user segment held approximately 10.9% in 2025" |

---

## 7. 查不到 / 证据薄弱清单

| # | 缺口 | 状态 | 说明与后续动作 |
|---|---|---|---|
| 1 | **AI 绘画产品的免费→付费转化率** | `[待确认]` | 无任一厂商或第三方公开披露。可用的最接近替代是美图"付费/MAU"存量渗透率 5.9%–9.0%（A 级）【S1】，但**不是漏斗转化率**，不可混用。通用 SaaS 2–5% 是 C 级二手汇总【S38】，不能替代。 |
| 2 | **Midjourney 付费率、付费用户数、留存率** | `[待确认]` | 官方从未披露。网络流传的"139 万付费用户""21.5% 转付费"均为 C 级推算或与官方"无免费层"自相矛盾，**禁止在面试中当事实引用**。2025 收入 ~$5 亿亦为第三方估算【S40，C】。 |
| 3 | **AI 绘画产品的 NPS** | `[待确认]` | 检索未发现任一产品的公开 NPS。 |
| 4 | **AI 绘画 App 的 D1/D7/D30 留存** | `[待确认]` | Sensor Tower / Similarweb 的留存数据未公开可得；a16z 只公布 MAU 榜与收入榜【S27】。 |
| 5 | **分层市场份额（谁最大）** | 证据冲突 | Meticulous 称 marketing & advertising >36% 最大【S47，C】，Dataintelo 称 media & entertainment 34.2% 最大【S48，C】。两者口径与样本均不透明 → **只用定性结论"广告营销与文娱是最大两块"**。 |
| 6 | **Adobe Firefly ARR 的准确值** | 数据打架 | 三个数字并存：$125M（Mordor 转述，2025）、>$250M（Q1 FY26，招银国际引 Adobe）【S25，B】、≈$300M（Q2 FY26 转述，C）。**建议只引用 B 级的"Firefly 收入占 Adobe 总收入约 1%"【S25】**，这是最稳健的表述。 |
| 7 | **教育出版场景的量化付费意愿** | 证据薄弱 `[SINGLE_SOURCE]` | 只有童趣《小步日诵》一个可核验案例（-60% 时间 / -68% 费用）【S15，B】。缺少：出版社 AI 插画的采购预算规模、单张 AI 插图结算价、教辅 vs 教材的付费差异。**建议下一步**：找出版行业协会（中国出版协会、中国书刊发行业协会）或上市出版公司年报中的"数字出版/AI"披露。 |
| 8 | **图库图片的官方定价** | 未取到一级源 | Shutterstock/Getty 官方价格页未能直接抓取，现有价格为聚合站抓取【S28，C】。**建议下一步**：直接访问 shutterstock.com/pricing 与 gettyimages.com 官方价格页核对。 |
| 9 | **儿童绘本插画报价的跨源分歧** | 严重分歧 | 单张从 $10 到 $1000+（相差 10 倍），源于"外包工厂 vs 自由职业署名插画师"层级差异【S29】【S30】【S31】，全部 C 级。**建议下一步**：查 AOI（Association of Illustrators）或国内插画师协会的费率指南。 |
| 10 | **用户流失原因的权威调研** | 证据薄弱 | 现有全部为 Trustpilot/论坛/评测的 UGC（C 级）【S39】+ 行业组织的从业影响调研（B 级，但测的是"丢单"不是"弃用产品"）【S21】。**建议下一步**：查 G2/Capterra 的 AI 图像工具评论分布，或 Sensor Tower 的卸载/流失面板。 |
| 11 | **中国 AI 绘画（纯图像生成）用户规模与付费率** | `[待确认]` | CNNIC 只给"生成式 AI 用户 5.15 亿"的总口径，未拆分图像生成【S9】；QuestMobile 有"AI 图像处理"赛道但未给绝对值【S10】。**建议下一步**：查 QuestMobile《AI 应用层发展核心报告》原文或艾瑞/易观的 AIGC 专项报告。 |
| 12 | **开发者层（L8）的付费证据** | 薄弱 | 只有 Google 官方 API 单价【S32，B】；缺 Replicate/Leonardo API/ComfyUI 生态的实际调用量与收入。 |
| 13 | 各第三方市场规模数字 | 不可互证 | pmarketresearch / dataintelo / zvzo / yuezhineng 等给出的市场规模与份额互相矛盾，均为 C 级付费报告摘要页 → **本次未采信任何单一市场规模数字**，仅保留 Goldman Sachs 的预测作为 B 级参考【S26】。 |
