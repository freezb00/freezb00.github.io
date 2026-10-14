# 发布前审计报告 · AI 绘画产品调研

> 审计角色：Citation Auditor + Numeric Auditor
> 审计时间：2026-10-12｜审计对象：report.md / decision-memo.md / deck.html / research-thesis.yaml / evidence-ledger.yaml
> 审计约束：只记录实际观测结果。打不开写「打不开」，取不到写「取不到」，不猜内容、不补数字。

---

## 1. 总体判定

**结论：需修正后发布（不可原样发布）。**

一句话理由：**证据链的 A 级硬事实（E01/E04/E05/E06/E08/E12/E13/E14 部分/E15/E20/E23/E24/E28/E29/E31/E32/E37）经真实抓取全部命中、且全文 0 处类比句、0 个编造 E 编号，主体可用；但存在 1 个最高级问题——即梦 AI 定价（官方页实测无任何价格数字）被以「搜索引擎渲染快照」填充并标为 A 级 hard_fact，且被 4 个承重结论、1 条证伪信号对照组、1 张面试话术卡引用；另有 9 条高严重级问题需在发布前修掉。**

| 项 | 结果 |
|---|---|
| 高严重级问题 | **10 条** |
| 中严重级问题 | 14 条 |
| 低严重级问题（可接受） | 11 条 |
| 类比句 | **0 处**（5 份文件全量扫描） |
| 编造/错误 E 编号 | **0 个**（三份产物共 37/35/36 个 E 编号，全部存在于账本） |
| URL 抽检 | 25 条：20 条完全打开、1 条重定向、1 条落到目录页、1 条 WebFetch 层失败、1 条 PDF 未抽取、1 条页面无价格 |
| quote 抽检 | 14 条：11 条完全一致、2 条部分匹配、1 条找不到 |

---

## 2. A 节 · URL 可打开性抽检（25 条）

抽样原则：优先 A 级官方来源、财报、法规原文、判决书、官方 LICENSE / model card。

| # | E 编号 | URL | HTTP / 打开状态 | quote 能否匹配 | 备注 |
|---|---|---|---|---|---|
| A1 | E01, E09 | docs.midjourney.com/hc/.../27870484040333-Comparing-Midjourney-Plans | 能打开 | **完全一致** | $10/$30/$60/$120、3.3/15/30/60 hr、Extra $4/hr、>$1M 强制 Pro/Mega 全部命中 |
| A2 | E02 | adobe.com/products/firefly/plans.html | 能打开，但只返回标题骨架，**无任何价格与条款文本**（JS 渲染） | **找不到** | "All paid plans include unlimited standard image and vector generations." 无法在该 URL 取证 |
| A3 | E03 | adobe.com/cc-shared/.../adbe-q3fy26-transcript.pdf | **WebFetch fetch failed**（未重试成功） | 未能核对 | 未取得 PDF 正文，本次不判定 quote |
| A4 | E04 | bfl.ai/pricing | 能打开 | **部分匹配** | 价格 $0.041/$0.048/$0.07/$0.10/$0.607 完全一致；"No subscriptions, no seat fees. Only pay for what you generate." **未找到**（页面只有 "Pay as you go"） |
| A5 | E05, E06 | cloud.tencent.com/document/product/1668/90896 | 能打开 | **完全一致** | 3.0 0.2元/张、极速版 0.099/0.094/0.088/0.066、资源包、并发叠加包全部命中。附带发现：页面顶部有「迁移至 TokenHub、原平台停止支持新购模型服务」公告，report 未记录 |
| A6 | E07, E08 | replicate.com/pricing | 能打开 | **完全一致** | A100 80GB $0.0014/s=$5.04/h；H100 $5.49/h；8×H100 $43.92/h；L40S $3.51/h |
| A7 | E10 | sacra.com/c/higgsfield/ | 能打开 | **完全一致（但发现 2 个未收录事实）** | $1B/$700M/$200M、32M+ 用户、近 1M 付费、$400M/$5.4B、>90%→60%+ 均命中。见下方 ⚠️ |
| A8 | E11 | platform.openai.com/docs/deprecations | **重定向** → developers.openai.com/api/docs/deprecations | 重定向后**完全一致** | "On November 14th, 2025 … removal from the API on May 12, 2026." 命中 |
| A9 | E12, E13 | www1.hkexnews.hk/.../2026082600321_c.pdf | curl 可下载（application/pdf，594,910 bytes）；WebFetch 不支持 PDF | **未做正文抽取** | 改用同源美图官网稿 + 中国证券报交叉核对，quote 全命中 |
| A10 | E13, E14 | meitu.com/zh/media/439 | 能打开 | **完全一致** | 1609万/235万/46%/113%/1844万/6.5%/3300万/6.2亿/2.82亿/MVLAND 220元 13 倍全部命中 |
| A11 | E14 | epaper.cs.com.cn/.../20260827_4-A06.htm | 能打开 | **完全一致** | MVLAND 220元 / 13 倍原句命中 |
| A12 | E14 | jimeng.jianying.com/ | 能打开，但会员区显示「**正在加载套餐**」，**全页无任何价格** | **找不到** | ⚠️ 见 G 节 |
| A13 | E14 | klingai.com/app/membership/membership-plan | 能打开 | **完全一致** | 58/234/586/1149 元，100 灵感值 6.97→3.52 全部命中 |
| A14 | E15 | doi.org/10.1038/s41598-025-99924-7 | 重定向 → nature.com/articles/s41598-025-99924-7（开放获取） | **完全一致（β 值）** | β=0.310/0.279/0.197 三句命中；间接效应 0.0943 位于 Table 8，正文段落未取到，未能直接核对 |
| A15 | E18 | moe.gov.cn/ | 能打开，但为**教育部首页** | **找不到** | ⚠️ 三条 A 级 quote（未经审定不得出版 / 插图质量高 / 保本微利）不在该 URL |
| A16 | E20 | ipc.court.gov.cn/zh-cn/news/view-6033.html | 能打开 | **完全一致** | 第十二条原句、法发〔2026〕10 号、2026-09-07 全部命中 |
| A17 | E23 | cac.gov.cn/2025-03/14/c_1743654684782215.htm | 能打开 | **完全一致** | 第四条（三）、第九条、第十四条（2025-09-01 施行）命中 |
| A18 | E23 | cac.gov.cn/2026-07/06/c_1785081384384987.htm | 能打开 | **完全一致** | 1.4 万余款 / 600 余万条 / 2.6 万余个 / 1,300 余个 / 9 个数据集命中 |
| A19 | E23 | cac.gov.cn/2026-09/02/c_1790099041364574.htm | 能打开 | **完全一致** | 561 万余条 / 4.9 万余个 / 2,400 余个命中 |
| A20 | E24 | eur-lex.europa.eu/eli/reg/2026/1744/oj | 打开但**落到 OJ 目录页**，未取到法规原文；追加 `/eng` 后取到 | **部分匹配（含新发现）** | Annex III→2027-12-02、Annex I→2028-08-02 命中。⚠️ 发现 Recital (38)：对 2026-08-02 前已投放市场的生成式系统，Art. 50(2) 标记义务给 **4 个月过渡期**；report「2026-08-02 如期适用」未写入该例外 |
| A21 | E32 | blog.comfy.org/p/comfyui-raises-30m-to-scale-open | 能打开 | **完全一致** | "$30 million financing at a $500 million valuation"、累计 $47M、4 million / 60,000+ / 150,000+ 命中。日期差异：页面 Apr 24, 2026 vs report 记 2026-04-25 |
| A22 | E28 | github.com/comfyanonymous/ComfyUI/blob/master/LICENSE | 能打开 | **完全一致** | "GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007" |
| A23 | E29 | huggingface.co/black-forest-labs/FLUX.1-dev | 能打开 | **完全一致** | `flux-1-dev-non-commercial-license`，gated 命中 |
| A24 | E37 | news.cn/tech/20260211/.../c.html | 能打开 | **完全一致** | 44.8 万家门店 / 226.2 万张 / 零成本 / 54.9 万商家 / 80% 命中 |
| A25 | E31 | liblib.art/viphome | 能打开 | **完全一致** | ¥429/2199/7399/14999/40999、700/4600/16300/32800/92000 积分、0.048→0.015、20 积分/日、3GB 全部命中 |

**⚠️ A7 的两个未收录事实（见 H2）**：Sacra 原文写明「The company calculates its run rate by **multiplying revenue from the latest four weeks by 13**」——即 $1B 是外推 run-rate 而非已实现年收入；且 Sacra 页面顶部「Revenue」卡显示 **$538.00M (2026)**，与正文 $1B 并列出现、关系未说明。report / memo / deck / 账本 E10 均未收录这两点。

---

## 3. B 节 · quote 匹配核查（14 条）

| # | 出处 | 引用的 quote | 原文核对结果 | 判定 |
|---|---|---|---|---|
| B1 | E01 | "Monthly Price $10 $30 $60 $120 … Fast GPU Time 3.3 hr/month (200 minutes) … Purchase Extra GPU Time $4/hr … You must purchase the Pro or Mega plan if you are a company making more than $1,000,000 USD…" | 逐项命中，含 3.3 hr/month (200 minutes) | **完全一致** |
| B2 | E04 | "Pay as you go … FLUX 3 Image $0.041/img … $0.607/img" | 价格与 "Pay as you go" 命中；"No subscriptions, no seat fees. Only pay for what you generate." 未找到 | **部分匹配（无歪曲）** |
| B3 | E05/E06 | "混元生图（3.0） 0.2元/张"；"混元生图（极速版）0.099/0.094/0.088/0.066 元/张" | 官方后付费阶梯表逐项命中 | **完全一致** |
| B4 | E08 | "Nvidia A100 80GB $0.0014/second"；"8x Nvidia H100 $0.0122/second" | 两项均命中（$0.001400/sec、$0.012200/sec） | **完全一致** |
| B5 | E10 | "Higgsfield hit $1B in annualized revenue in September 2026, up from $700M in August and about $200M at the end of 2025 … more than 32 million users and nearly 1 million paying subscribers" | 逐字命中 | **完全一致** |
| B6 | E11 | "On November 14th, 2025, we notified developers … removal from the API on May 12, 2026." | 逐字命中 | **完全一致** |
| B7 | E12/E13 | "用戶AI算力點消費總額於2026年第一季及第二季均實現超過46%的環比增長" | 大陆官网稿为「第一季度及第二季度的AI算力点消费总额环比增幅均超过46%，半年累计增幅约113%」 | **转述但意思一致**（繁→简换算，语义一致） |
| B8 | E13 | "生活场景应用的付费订阅用户1609万，同比增长18.8% …… 生产力应用的付费订阅用户235万，同比增长29.8%" | 逐字命中 | **完全一致** |
| B9 | E14 | "AI音乐视频创作平台MVLAND目前每付费订阅用户的月均消费水平约为220元，按年化计算，约为美图公司综合ARPPU的13倍" | 中证报原句逐字命中 | **完全一致** |
| B10 | E14 | "超级会员 … 下月续费金额¥4299" | jimeng.jianying.com 页面价格模块为「正在加载套餐」，**无 4299 字样** | **找不到**（⚠️ 见 G 节） |
| B11 | E14 | "黑金会员 后续每月1149元" | 可灵会员页命中「后续每月*1149元*」 | **完全一致** |
| B12 | E15 | "perceived ease of use (β=0.310) and output quality (β=0.279) exerted stronger effects on subscription intention than price value (β=0.197)" | 原文为三句独立表述 "PEU significantly influences PUI (β=0.310, p<0.001)" / "OQ notably affects PUI (β=0.279, p<0.001)" / "PV has a significant influence on PUI (β=0.197, p=0.003)"，并另有排序句 PEU 0.310 > OQ 0.279 > SI 0.226 > PV 0.197 | **拼接但无歪曲** |
| B13 | E20 | "第十二条 … 人工智能开发者提出不侵权抗辩的，应当责令其提供训练数据来源、训练过程记录、模型运行模式以及科学理论依据等予以佐证。法发〔2026〕10号" | 逐字命中 | **完全一致** |
| B14 | E23 | "第四条 …(三)在图片的适当位置添加显著的提示标识"；"第九条 …依法留存提供对象信息等相关日志不少于六个月"；"第一阶段累计处置违规网站、应用程序、智能体等AI产品1.4万余款" | 三处均逐字命中 | **完全一致** |

**判定汇总**：完全一致 11 / 部分匹配 2（B2、B12）/ 找不到 1（B10）。**0 条语义不符。**

---

## 4. C 节 · 关键结论双源核验（8 条承重结论）

| # | 承重结论 | 独立来源数 | ≥2 独立源？ | 单源是否已标 | 结果 |
|---|---|---|---|---|---|
| C1 | **B1 / NV1**：定价战场从月费转到计量单位 | 4（E01 Midjourney 官方、E02 Adobe、E04 BFL、E12 美图港交所） | ✅ | — | **通过** |
| C2 | **B2 / NV2**：国产 API 地板价 ¥0.2 → ¥0.066–0.18 被击穿 | 1 个 A 级官方（腾讯云）+ ≥2 个 C 级二级站（OrcaRouter / yankucms / aiapi-pro，存在同源风险） | ⚠️ 部分 | 未标 | **中**：A 级事实只有腾讯云一家，「地板价击穿」的 A 级支撑是单点 |
| C3 | **B3 / NV3**：价值迁移第三极（Higgsfield） | **1**（Sacra，公司自报） | ❌ | ⚠️ 仅写「C 级公司自报」，**三份产物均未打 `[SINGLE_SOURCE]` 标签** | **高**（见 H6） |
| C4 | **B4 / OC3**：合规是准入门槛不是溢价来源 | 4（E03 Adobe 财报、E25 Stability、E26 Getty 10-Q/CMA、E20 最高法） | ✅ | — | **通过** |
| C5 | **B5 / OC4**：国内是「中位数低、右尾极长」 | 3（E13 美图官方、E14 可灵官网 A、E31 LiblibAI 官网 A）+ MVLAND（A/B） | ✅ | — | **通过**（但右尾中「即梦 ¥4,299/月」一项落在不可核验源上，见 G/H1） |
| C6 | **B6 / NV5**：专业层付费驱动是「可控与稳定」而非价格 | 因果结论**仅 1 个 A 级源**（E15，N=394）；右尾分布部分有 E13/E14 | ❌（因果侧） | ⚠️ report 自述「唯一的 A 级因果研究」但**未打 `[SINGLE_SOURCE]`** | **高**（见 H6） |
| C7 | **B7 / OC5**：被挤死的是定位不是品类 | 退场名单 ≥4 个独立源（Imagen 官方 A、Sora 新华网 B、Reve C、6pen C）+ E10 + E38 | ✅ | — | **通过** |
| C8 | **B8**：教育出版当前只够做观察方向 | 制度侧 E18（A）；ROI 实证 **E19 单源 B** | ⚠️ 部分 | ✅ E19 已标 `[SINGLE_SOURCE]` | **中**：制度侧 A 级 URL 无法回溯（见 H4） |
| C9 | **FP2**：免费额度是否亏损 = 是否拥有自有算力的函数 | 2（E08 Replicate 牌价 A、E09 Midjourney 官方 A）+ E07 推导 | ✅ | — | **通过** |
| C10 | **FP4**：model ID 更替是可规划事件 | **1**（E11 OpenAI deprecations 官方页；E33 是另一现象，不构成同现象第二源） | ❌ | ❌ 未标 | **高**（见 H5/H6） |

**未标 `[SINGLE_SOURCE]` 的单源承重结论共 3 条：NV3（Higgsfield）、NV5 因果侧（E15）、FP4（E11）。** research-thesis.yaml 全文 `[SINGLE_SOURCE]` 出现 **0 次**、`[待确认]` 出现 **0 次**，是该文件中最明显的标注缺口。

---

## 5. D 节 · 数值口径审计

### D-1 裸数字（缺 unit / timepoint / scope）

| 位置 | 裸数字 | 缺失项 | 级别 |
|---|---|---|---|
| report §4.1.2 #4 | "SynthID 已标记 1,000 亿+ 图像/视频" | 无 timepoint；unit 是「张」还是「次标记」未定 | 中 |
| report §4.4 L6 | "Adobe CC 出现在 22.6 万+ 企业技术栈（C）" | 无 timepoint、无 scope（技术栈口径未定义） | 中 |
| report §9.2 用户份额行 | "Canva 2.65 亿 MAU（C）"、"美图整体 MAU 2.82 亿（A）" | 无 timepoint | 中 |
| report §4.1.2 #1 | "注册用户 2,000 万+（`estimate`）；员工 40–60 人" | 无 timepoint、无 scope | 低 |
| report §4.1.4 #11 | "超 400 万设计师/运营/电商等创作者（…未标时间点）" | 无 timepoint（report 已自认） | 低 |
| deck p.6 国内 | 同上「400 万创作者」 | 无 timepoint（deck 已自认但仍标 A/B） | 低 |

### D-2 混用口径（收入 / 用户 / 调用量互推）

| 位置 | 问题 | 级别 |
|---|---|---|
| report §4.7 护城河表「分发渠道」行 | 同一格内并列 Gemini App 9 亿 MAU（用户份额）、Nano Banana 累计生成 500 亿张（调用量）、Canva 月访问量 8.58 亿次（流量），并据此判「最强」 | 中 |
| report §9.2 用户份额行 | 「累计注册 6,500 万」与「MAU 2.65 亿 / 2.82 亿」与「付费订阅 1,844 万」并排列在同一张份额表，表内已写「不可互推」但仍并列 | 低 |
| report §4.2 分类学 #1 | "美图 VIP（2026H1 VIP 订阅占总收入 79.9%）" —— 79.9% 实际是**影像与设计产品收入占集团总收入**的比例（§4.3.7 同一数字写作「¥22.13 亿 / ¥17.69 亿（79.9%）」），被改标签为「VIP 订阅」 | **高**（见 H10） |
| report §4.1.4 #14 / §4.3.7 | 美图毛利率 71.5% 已注明是集团口径 ✅；海艺「毛利率 >40% / 续费率 >60%」已注明绝对收入未披露 ✅ | 通过 |

### D-3 预测值 / 计划值被写成已发生事实

| 位置 | 问题 | 级别 |
|---|---|---|
| report §3.2 FP4、§4.6.2 时间线（2026-10-23 / 2026-12-01 行）、§5.5 F6 对照组、memo 卡 7、deck p.5 FP4、deck p.10 时间线 | 截至审计日 2026-10-12，**只有 dall-e-2 / dall-e-3（2026-05-12）2 个端点已下线**；gpt-image-1（2026-10-23）与 gpt-image-1.5 / mini / chatgpt-image-latest（2026-12-01）为**已公告但尚未发生**的下线。六份产物统一写作「OpenAI 在 14 个月内下线 6 个图像端点」（完成时态） | **高**（见 H5） |
| report §5.1–5.3 三情景 | 已显式声明「描述的是结构状态与触发条件，不是市场规模预测」✅ | 通过 |
| report §5.7 / §8 #21 | 已拒绝给出 2027–2028 市场规模 ✅ | 通过 |

### D-4 estimate 未给 formula 或假设链

| 位置 | estimate | 缺失 | 级别 |
|---|---|---|---|
| report §4.1.4 #2 | "火山引擎日均算力成本估约 ¥400 万–1,200 万（B）" | 无 formula、无假设链、无 scope（是否只算生图） | 中 |
| report §9.1 | "Canva 付费率 ≈11.7%（付费用户/MAU 推算）" | 未给分子分母数值、无 timepoint；该数字在正文其他位置从未出现 | 中 |
| report §4.1.2 #1 | "Midjourney ARR $500–600M（2026，`estimate`，C）" | 无 formula（已声明为第三方建模值，非申报值） | 低 |
| report §4.8.4 | "384 张手绘基线约 ¥40 万–94 万元，AI 后约 ¥13 万–30 万元" | 有 formula（$150–350/张 × 384），但**未标汇率**（见 D-6） | 中 |
| report §4.3.2 / §4.3.5 | 公式 A、公式 D 均已显式列出 formula 与假设链 ✅ | — | 通过 |

### D-5 厂商自报（self-reported）未标注

| 位置 | 问题 | 级别 |
|---|---|---|
| report §4.7 分发渠道行 / §4.1.2 #4 | "Gemini App 9 亿 MAU（2026-05）"、"Nano Banana 累计生成超 500 亿张（2026-05）" 为 Google 自报，仅标 B/C，未标 self-reported | 低 |
| report §4.1.2 #12 | "Canva ARR 约 $40 亿（2026 年初，C）" —— §9.1 已说明是 COO 对 TechCrunch 口述，但 §4.1.2 未标 self-reported | 低 |
| report §4.4 L4 / L6、§4.1.4 #15 | 淘宝、阿里妈妈、Canva B2B、万兴均已标 self-reported ✅ | 通过 |

### D-6 币种混用 / 换算未标汇率与日期

| 位置 | 换算 | 隐含汇率 | 级别 |
|---|---|---|---|
| report §4.3.3 公式 B 表 | 火山 Seedream ¥0.12/张 ≈ **$0.018**；阿里云 ¥0.20/张 ≈ **$0.028** | 6.67 与 7.14 —— **同一张表内两个不一致的汇率**，均未标汇率与日期 | **高**（见 H8） |
| report §4.2 定价带结构事实 (a) | 即梦超级会员 ¥4,299/月 ≈ **$605/月**（对比 Midjourney Mega $120/月），仅写「按 2026 年汇率量级」 | 7.105，未标汇率值与取数日期 | **高**（见 H8） |
| report §4.8.4 / deck p.11 | 中坚插画师 $150–350/张 → ¥40 万–94 万元 | 7.0，未标 | **高**（见 H8） |
| report §4.1.2 #4 | Nano Banana Pro $0.134/张 与 $120/1M tokens 并列 | 未混用，但两个计价单位未说明换算前提 | 低 |

### D-7 跨时间点比较未说明

| 位置 | 问题 | 级别 |
|---|---|---|
| report §4.3.1 GPU 单价表 | 同一表内 timepoint 有 2026-09-23（Replicate）、2026-10（AutoDL）、2026-07（国内裸金属）三种，表内已分别标注 ✅ | 通过 |
| report §4.1.4 #7 | LiblibAI 2025-10「300 点/日」与 2026-10「20 积分/日」已显式声明「计量单位换名，不可直接比较」✅ | 通过 |
| report §9.2 | Gemini MAU @2026-05、ComfyUI 400 万用户 @2026-04-25、美图 MAU @2026H1 并列 | 部分无 timepoint（见 D-1） | 中 |
| report §4.6.2 时间线 | 2024-02-08 至 2026-12-01 跨 3 年，每行均带日期 ✅ | 通过 |

### D-8 数值内部冲突（三份产物之间 / 同一份内）

| 位置 | 冲突 | 级别 |
|---|---|---|
| report §4.1.2 #16 vs §4.7 | 海艺社区模型「**70 万+**」vs「**150 万+ 模型/LoRA（2025 年底）**」，两处均无 A 级源 | 中 |
| report §3.1 NV1 注 vs §4.1.4 #1 | 即梦降幅数据用「69/199/**499** 元档 → 725/2,210/**6,160** 积分」，而定价表为 69/199/**998**/4,299 元档 → 725/2,210/**12,320**/54,600 积分 | **高**（见 H9 / H10） |
| report §4.1.4 #14 / deck p.6 | 「AI 商拍 **8 美豆**/张（**≈¥0.8**/张）」与同格「折算 **¥0.032/美豆**」矛盾（8 × 0.032 = ¥0.256，非 ¥0.8）；实为混用了 ¥0.1/美豆（美图设计室充值档）与 ¥0.032/美豆（WHEE 赠送档）两个单位价 | **高**（见 H9） |
| report §4.1.2 #12 | Canva 官方中文站 Pro US$180/年 vs 第三方 $15/月，已显式标注冲突 ✅ | 通过 |
| report §4.2 定价带表 vs deck p.9 | 即梦「¥998/月」在 report 标 A/B，deck 标 A/B，账本 E14 标 A —— 三处等级不一致 | 中 |

---

## 6. E 节 · 引用 ID 完整性

### E-1 编号存在性

| 文件 | 使用的 E 编号数 | 账本中不存在的编号 |
|---|---|---|
| report.md | 37（E01–E34、E36–E38，缺 E35） | **0** |
| decision-memo.md | 35（E01–E15、E17–E34、E36–E38，缺 E16、E27、E35） | **0** |
| deck.html | 36（E01–E34、E37、E38，缺 E35、E36） | **0** |
| research-thesis.yaml | 38（E01–E38 全量） | **0** |

账本实际编号 E01–E38 共 38 条（含 E35）。**未发现任何编造或拼错的 E 编号。**

### E-2 语义一致性（张冠李戴检查）

| # | 问题 | 级别 |
|---|---|---|
| E-2.1 | report §6 第 33 行把 **E22** 挂到 `ipc.court.gov.cn/zh-cn/news/view-4513.html`（内容为「广州案与杭州案对比 + 张家港案」），但账本 E22 的 claim 是「美国不可登记 vs 中国北京案承认用户为作者」，source_url 为 DLA Piper + 中国法院网。同一 E 编号在两个文件挂了不同 URL 与不同内容侧 | 低 |
| E-2.2 | **E21 等级三处漂移**：账本 A/B → report §4.6.1 标 A/B → report §6 来源表标 **C** → FP3 与 memo 决策 4 按 **A** 级使用（"输出侧过滤标准写进判决主文（E21，A，广州互联网法院…）"）。同一证据在三份产物里出现 A / A/B / C 三个等级 | **高**（见 H7） |
| E-2.3 | **E16 URL 不一致**：账本 E16 source_url = `theaoi.com`；report §6 第 27 行 E16 挂 `creatorsrightsalliance.org`。两个不同 URL 挂同一 E | 低 |
| E-2.4 | **E19 账本无 URL**：账本 E19 source_url 写「童趣出版案例报道（B 级垂媒）」，无链接；report §6 第 30 行与 memo §9 补了 `m.bookdao.com/Article.aspx?id=441080`。账本缺 URL，正文补了，未构成编造 | 低 |
| E-2.5 | **E30 / E26 / E31 URL 粒度不一致**：账本给首页（`tusiart.com/`、`investors.gettyimages.com/`、`liblib.art/`），正文给具体页（`/about/model-policy`、`/node/16391/html`、`/viphome`）。方向正确但账本应回填具体页 | 低 |
| E-2.6 | **E38 账本 URL 不可回溯**：`tracxn.com/` 为数据库首页，无法定位到 NeuroPixel.AI 具体条目 | 低 |
| E-2.7 | **E14 账本标 A 与正文自述矛盾**：账本 E14 `source_grade: A` 且 source_url 含 `jimeng.jianying.com`；report §4.1.4 与 §8 #1 自承「两次直连 Fetch 失败，数字取自搜索引擎渲染快照」。账本等级被抬高 | **高**（归入 H1） |

---

## 7. F 节 · 类比句扫描

扫描句式：`这就像 / 类似于 / 相当于 / 好比 / 打个比方 / 可以想象成 / 就像是 / 好比说 / 宛如 / 犹如 / 就像 / 如同 / 仿佛 / 某种意义上说 / 打个不恰当的比方`

| 文件 | 命中数 |
|---|---|
| report.md | **0** |
| decision-memo.md | **0** |
| deck.html | **0** |
| research-thesis.yaml | **0** |
| evidence-ledger.yaml | **0** |

**结果：0 处。符合「应为 0 处」的要求。**

---

## 8. G 节 · 原文禁止承压检查

### G-1 `[待确认]` 项是否确属查不到（抽样复检）

| `[待确认]` 项 | 本次复检动作 | 是否确属查不到 |
|---|---|---|
| 即梦 AI 年费档位 | 打开 jimeng.jianying.com | ✅ 确属查不到（页面「正在加载套餐」），但**月费档位同样是查不到的**（见 G-2） |
| 即梦 AI 收入 | 未检索（report 已声明不引用） | ✅ 已正确禁用 |
| 腾讯智影 / 绘蛙 / 创客贴 / 蓝湖 MasterGo 定价 | 未逐项复检 | ⚠️ 未复检，按 report 声明接受 |
| ComfyUI 收入规模 | Comfy 官方博客确认只披露融资与体量 | ✅ 确属零披露 |
| 出版社 AI 插画采购预算与单张结算价 | 未检索 | ⚠️ 未复检 |
| 2026 年前沿图像模型单次训练成本 | 未检索 | ⚠️ 未复检 |

`[待确认]` 密度：report.md 55 处、deck.html 16 处、decision-memo.md 1 处、research-thesis.yaml **0 处**。memo 与 thesis 的标注密度明显低于 report，memo 读者更易误用。

### G-2 即梦 AI 定价专项检查（最高级问题）

**实测结果（2026-10-12）**：`https://jimeng.jianying.com/` 页面「选择适合你的创作计划」区块渲染结果为「**正在加载套餐**」，**全页无任何一个价格数字**。

**report.md 自承**（§4.1.4 #1 与 §8 #1）：「页面为 SPA 动态注入，两次直连 Fetch 失败，数字取自搜索引擎对该 URL 的渲染快照」。

**判定**：即梦的月费档位（¥69 / ¥199 / ¥998 / ¥4,299，积分 725 / 2,210 / 12,320 / 54,600）**不是来自可回溯的一级来源，而是二手渲染快照**。这属于「用不可核验来源填充本应 `[待确认]` 的位置」。虽然它不是「套用同类产品价格」的估算，但性质更严重：**它被标为 A 级 hard_fact，并进入了承重结论。**

**污染范围（实测）**：

| 位置 | 用法 | 标注的等级 |
|---|---|---|
| evidence-ledger.yaml E14 | `source_grade: A`，source_url 含 jimeng.jianying.com | **A**（❌ 应降级） |
| report §1 B5 | 「右尾样本同为 A 级：…即梦超级会员续费 ¥4,299/月」 | **A** |
| report §2.4 OC4 结论 | 「可比对象不是 ¥16/月，而是 … 即梦 ¥69–4,299/月」 | 未标等级 |
| report §3.1 NV5 表 | 「即梦 ¥4,299/月」 | A（挂 E14/E15） |
| report §4.1.4 #1 定价表 | ¥69 / ¥199 / ¥998 / ¥4,299 | A- |
| report §4.2 定价带表 | 低端 ¥69、中端 ¥199、高端 ¥998 / ¥4,299 | A / B |
| report §4.2 结构事实 (a) | ¥4,299/月 ≈ $605/月，作为「国内顶部 SKU 高于海外」的**唯一国内高值锚点** | 未标等级 |
| report §5.5 F5 | 对照组 ¥4,299/月（证伪信号的基线值） | 未标等级 |
| report §10 使用建议 2 | 列为「面试中最稳的三组数字」的对照项 | — |
| decision-memo §9 E14 行 | 「A · hard_fact」，无获取方式说明 | **A** |
| decision-memo 卡 3 | 「右尾同为 A 级：…即梦超级会员 ¥4,299/月」 | **A** |
| deck p.6 国内表 | ¥69/199/998/4,299，等级栏 **B**（与 report 的 A- 不一致） | B |
| deck p.9 定价带 | 高端 ¥998 / ¥4,299，等级 **A/B** | A/B |
| deck p.13 B5 | 「即梦超级会员续费 ¥4,299/月 … 2026 官网会员页 **A**」——**未标注 Fetch 失败与快照来源** | **A** |
| deck p.15 步骤 1 | 反推自检的对照项「即梦 ¥69–4,299/月（A）」 | **A** |

**另发现内部冲突**：report §3.1 引用东方证券的降幅数据使用「69/199/**499** 元档 → 725/2,210/**6,160** 积分（降幅 33%/45%/59%）」，与 §4.1.4 定价表的「69/199/**998** 元档 → …/**12,320** 积分」不一致。499 元档在定价表中不存在，6,160 恰为 12,320 的一半。同一产品在 report 内存在两套积分档位。

---

## 9. 必须修正的高严重级问题清单（10 条）

### H1 · 即梦 AI 定价被二手快照填充并标为 A 级 —— 最高级

- **文件/位置**：`evidence-ledger.yaml` E14（source_grade: A）；`report.md` §1 B5、§2.4 OC4 结论、§3.1 NV5、§4.1.4 #1、§4.2 定价带表与结构事实 (a)、§5.5 F5、§10 建议 2；`decision-memo.md` §9 E14 行、卡 3；`deck.html` p.6 / p.9 / p.13 / p.15
- **问题**：官方页实测无任何价格（「正在加载套餐」），数字来自搜索引擎渲染快照，非可回溯一级来源；却在所有产物中被标为 A 级 hard_fact，并支撑 B5「右尾极长」、OC4「天花板不低」、NV5、定价带结构事实 (a)、F5 对照组、面试卡 3。
- **怎么改**：① 把 jimeng.jianying.com 相关数字从 A 降为 **C（二手快照）**并在每个出现处补「来源为搜索引擎渲染快照，官方页两次直连失败，不可直接引用」；② 更稳妥的做法是把即梦月费档位移入 `[待确认]`，从 B5 / NV5 / 定价带表 / F5 对照组中撤下，改用可灵 ¥1,149/月（A，已实测）与 LiblibAI ¥40,999/年（A，已实测）作右尾锚点；③ 账本 E14 的 source_grade 改为 A（可灵 + MVLAND）/ C（即梦）分行；④ deck p.13 必须补上 Fetch 失败说明。

### H2 · E10 未披露 Sacra 自报的 run-rate 口径与同页冲突数

- **文件/位置**：`report.md` §2.1 反方证据①、§3.1 NV3、§5.6 max_assumption；`decision-memo.md` 排序第 1 条、卡 1；`deck.html` p.4 B3、p.15；`evidence-ledger.yaml` E10；`research-thesis.yaml` NV3
- **问题**：Sacra 原文明确写「The company calculates its run rate by multiplying revenue from the latest four weeks by 13」——$1B 是 4 周收入外推的 run rate，不是已实现年收入；且 Sacra 页面顶部「Revenue」卡显示 **$538.00M (2026)**，与正文 $1B 并列、关系未说明。全系统承重墙（NV3 / OC1 / DS2 / bear 0.25 / bull 阈值）建立在这个未标口径的数字上。
- **怎么改**：在 E10 的 claim 与 report §5.6 中补两行硬事实——「口径：最近 4 周收入 × 13 的公司自报 run rate（Sacra 原文）」与「Sacra 页面顶部另有 Revenue $538.00M (2026)，与 $1B 的关系未说明」；所有「年化收入约 $10 亿」改写为「公司自报年化 run rate 约 $10 亿（4 周×13 外推）」。

### H3 · Adobe Firefly 定价页 quote 不可核验（E02 / FP1 承重）

- **文件/位置**：`report.md` §6 第 2 行（A）、§2.3? 无、§3.2 FP1、§4.1.2 #2、§9.1；`decision-memo.md` 决策 6 ③；`deck.html` p.5 FP1；`research-thesis.yaml` FP1；`evidence-ledger.yaml` E02
- **问题**：`adobe.com/products/firefly/plans.html` 实测只返回标题骨架，quote「All paid plans include unlimited standard image and vector generations.」与四档价格均无法在该 URL 取证。FP1（四条第一性约束之一）的正面证据与 memo「不做无限免费方案」的依据都挂在这条 quote 上。
- **怎么改**：① 改挂可核验的 Adobe 官方来源（report §6 第 5 行的 generative credits FAQ 页，本次未抽检，需实际抓取验证后再替换）；② 若仍用 plans.html，必须标注「该页为 JS 渲染，本次未取得原文；条款表述来自 Adobe 官方 FAQ 页」；③ 在 E02 的 risk 栏写明「quote 未在 source_url 直取到，等级暂按 A，需人工复核」。

### H4 · E18 三条 A 级 quote 挂在教育部首页 URL，无法回溯

- **文件/位置**：`evidence-ledger.yaml` E18（source_url: `http://www.moe.gov.cn/`）；`report.md` §6 第 28 行、§4.8.3；`decision-memo.md` 决策 1、§9；`deck.html` p.11
- **问题**：实测 moe.gov.cn 为教育部首页，三条 quote（「未经审定的教材不得出版、选用」「插图质量高，图文配合得当」「保本微利」）均不在该 URL。B8 的制度侧 A 级边界、决策 1 的「落点不是国家审定教材」约束、deck p.11 的制度硬边界全部依赖它。
- **怎么改**：把 URL 换成《中小学教材管理办法》（教材〔2019〕3 号）的**文件级 URL**（需在 moe.gov.cn 站内检索后回填具体路径），并在回填前把 E18 的等级从 A 临时降为「A（URL 待回填）」。§4.8.3 引用的《广东省中小学地方课程教材管理实施细则》URL 为具体页，可保留。

### H5 · 4 个未发生的 scheduled deprecation 被写成已下线

- **文件/位置**：`report.md` §3.2 FP4、§4.6.2 时间线（2026-10-23 / 2026-12-01 行）；`decision-memo.md` 卡 7；`deck.html` p.5 FP4、p.10 时间线
- **问题**：截至 2026-10-12 只有 2 个端点（dall-e-2 / dall-e-3，2026-05-12）已下线；gpt-image-1（2026-10-23）与 gpt-image-1.5 / mini / chatgpt-image-latest（2026-12-01）为已公告未发生。六处均写作完成时「OpenAI 在 14 个月内下线 6 个图像端点」，违反报告自身「预测值不写成已发生事实」的纪律，且卡 7 是会被口播的面试话术。
- **怎么改**：统一改为「OpenAI 已公告在 14 个月窗口内下线 6 个图像端点（2026-05-12 已下线 2 个；2026-10-23、2026-12-01 计划下线 4 个）」，时间线表的这两行加「（已公告，尚未发生）」标注。

### H6 · 3 条单源承重结论未标 `[SINGLE_SOURCE]`

- **文件/位置**：`research-thesis.yaml` NV3、NV5、FP4（该文件全文 `[SINGLE_SOURCE]` 出现 0 次）；`report.md` §3.1 NV3 / NV5、§3.2 FP4、§1 B6；`decision-memo.md` 卡 6 / 卡 7；`deck.html` p.4 / p.5 / p.8
- **问题**：① NV3（Higgsfield 三极）仅 Sacra 一家来源，report 只写「C 级公司自报」未打标签；② NV5 / B6 的因果结论（PEU/OQ > PV）仅 E15 一项 A 级研究，report 自述「唯一的 A 级因果研究」但未打标签；③ FP4（更替可规划）仅 E11 一家（OpenAI），E33 属另一现象不构成第二源。
- **怎么改**：在这三条的结论行、thesis 的 `evidence_grade_warning` / `caveat` 栏统一补 `[SINGLE_SOURCE]`；FP4 补一句「跨供应商的 deprecation 通知期仅 OpenAI 一家有 A 级数据，Google Cloud / 火山方舟 / 阿里云尚无同口径公开记录」。

### H7 · E21 等级在 A / A/B / C 之间漂移，FP3 按 A 级使用

- **文件/位置**：`evidence-ledger.yaml` E21（A/B）；`report.md` §6 第 32 行（**C**）、§4.6.1（A/B）、§3.2 FP3（**A**）、§4.6.1 时间线（B/C）；`decision-memo.md` 决策 4（**A**）；`deck.html` p.10（A/B）
- **问题**：同一条证据（广州互联网法院 (2024) 粤0192民初113号）在五处标了三个不同等级；「输出侧过滤标准」被 FP3 与决策 4 当作 A 级工程标准写死进产品要求，而该过滤标准实际只出现在 B/C 级转述中（判决主文原文本次未直取）。
- **怎么改**：统一 E21 的等级为 **A/B（判决书事实 A，过滤标准表述 B）**；FP3 与 memo 决策 4 的「标准写死为判决主文表述」改为「标准表述来自对该案的 B/C 级转述，判决原文待 A 级核验」；report §6 第 32 行的等级从 C 改为 B/C 并注明「该案另有最高法知产法庭页可交叉」。

### H8 · USD/CNY 换算未标汇率与日期，且同一表内隐含汇率不一致

- **文件/位置**：`report.md` §4.3.3 公式 B 表（¥0.12≈$0.018 → 6.67；¥0.20≈$0.028 → 7.14）、§4.2 结构事实 (a)（¥4,299≈$605 → 7.105）、§4.8.4（$150–350/张 → ¥40万–94万 → 7.0）
- **问题**：四处换算均未标汇率值与取数日期，且隐含汇率在 6.67–7.14 之间浮动。deck p.11 与 p.14 复制了同样的换算。
- **怎么改**：在 §9.4「时间敏感数字」后新增一条口径说明「本报告所有 USD/CNY 换算统一取 X.XX（YYYY-MM-DD），换算值标 `≈` 并注明日期」；或更稳妥——**删除所有换算，改为并置原币种**（¥0.12/张；$0.018/张 由读者自算）。§4.3.3 表格建议直接删掉美元列。

### H9 · 美图「AI 商拍 8 美豆 ≈¥0.8/张」与同格「¥0.032/美豆」口径冲突

- **文件/位置**：`report.md` §4.1.4 #14；`deck.html` p.6 国内表
- **问题**：同格先写「折算 ¥0.032/美豆」（WHEE ¥58 ÷ 1,800 豆），后写「AI 商拍 8 美豆/张（≈¥0.8/张）」——8 × 0.032 = ¥0.256，与 ¥0.8 差 3 倍。实为混用了两个不同的美豆单价（WHEE 赠送档 ¥0.032/豆 vs 美图设计室充值档 ¥30/300 = ¥0.1/豆），未声明。
- **怎么改**：同格内拆成两行并各标口径：「WHEE：¥58/月 ÷ 1,800 赠送豆 = ¥0.032/豆 → 文生图 2 豆 = ¥0.064/张」；「美图设计室：¥30/300 豆 = ¥0.1/豆 → AI 商拍 8 豆 = ¥0.8/张」。deck p.6 同样拆分。

### H10 · 美图「79.9%」被改标签为「VIP 订阅占总收入」

- **文件/位置**：`report.md` §4.2 分类学表 #1（「美图 VIP（2026H1 VIP 订阅占总收入 79.9%）」）；`deck.html` p.7 商业模式表 #1（同表述）
- **问题**：79.9% 在 report §4.3.7 与美图官方稿中的口径是「**影像与设计产品收入 ¥17.69 亿占集团总收入 ¥22.13 亿的 79.9%**」（官方稿四舍五入为「约占总收入的 80%」），不是「VIP 订阅占总收入」。该格作为「C 端订阅」模式的代表作证，标签错误会被面试复述。
- **怎么改**：改为「美图影像与设计产品收入占总收入 79.9%（2026H1，A）」，或若确实要表达订阅占比，需另找美图披露的「VIP 订阅业务收入占比」数字并挂 URL。

> **备选（第 11 条，若 H10 修正后仍有余量）**：report §4.1.2 #16「70 万+ 社区模型」与 §4.7「150 万+ 模型/LoRA（2025 年底）」内部冲突，两处均无 A 级源，建议统一为「70 万+（C）/ 150 万+（C），二者口径与时间不一致，取数待核」。

---

## 10. 「可接受的不完美」清单（低严重级，不阻塞发布）

| # | 问题 | 为什么可接受 |
|---|---|---|
| 1 | `platform.openai.com/docs/deprecations` 已重定向到 `developers.openai.com/api/docs/deprecations` | 旧 URL 仍可用（自动跳转），内容一致；但 F6 的月度监控 URL 建议顺手更新 |
| 2 | `eur-lex.europa.eu/eli/reg/2026/1744/oj` 打开后落到 OJ 目录页（加 `/eng` 可取到原文） | 文件真实存在且 In force；只需在 §6 来源表补 `/eng` 后缀 |
| 3 | Adobe Q3 FY26 transcript PDF 在 WebFetch 层 fetch failed | 同源的美图/Adobe 数字已由其他 A 级源交叉覆盖；Adobe 的 AI-first ARR >$650M 与 2.4% 在 FP1/FP3 中与 Firefly ≈$300M 并列，非唯一支点 |
| 4 | ComfyUI 融资日期：官方博客 Apr 24, 2026 vs report 记 2026-04-25 | 1 天差异，不影响任何结论；顺手改即可 |
| 5 | E15 的间接效应 0.0943 / 95%CI 位于 Nature 页面 Table 8，本次正文段落未取到 | β 值三项已逐字命中，中介路径方向（OQ→PT→PUI 显著）已被原文「both mediating paths exclude 0」支持；建议补 PDF Table 8 截图存档 |
| 6 | E16 / E19 / E30 / E26 / E31 / E38 的账本 URL 与正文 URL 粒度不一致（首页 vs 具体页） | 均未构成编造，正文给的 URL 更具体；建议把正文 URL 回填账本 |
| 7 | 腾讯云混元生图计费页顶部有「迁移至 TokenHub、原平台停止支持新购模型服务」公告，report 未记录 | 该页正是 F1 的月度观测点，report 已要求「每月自行存档」，下次存档会自然捕捉到；建议在 §9.4 补一句提示 |
| 8 | 部分裸数字缺 timepoint：Adobe CC 22.6 万+ 企业技术栈、SynthID 1,000 亿+、Canva/美图 MAU 无 timepoint | 均为 C 级旁证，不进入任何结论与阈值；补 timepoint 或删掉即可 |
| 9 | 火山「日均算力成本估 ¥400 万–1,200 万」与 Canva 付费率 11.7% 无 formula | 前者已标 B 且不用于测算；后者仅出现在 §9.1 口径举例中，不进入结论 |
| 10 | memo 与 thesis 的 `[待确认]` / `[SINGLE_SOURCE]` 标注密度远低于 report（memo 1 处 / thesis 0 处） | report 是底稿，memo/thesis 为其派生；但建议在 memo §9 与 thesis meta 加一句「完整待确认清单见 report §8」 |
| 11 | Gemini App 9 亿 MAU、Nano Banana 500 亿张、Canva ARR $40 亿在部分位置未标 self-reported | 已标 B/C 等级，且报告 §9.1 已单列 self-reported 口径；属标注冗余度问题 |

---

## 11. 审计动作清单（按依赖顺序）

1. 修 H1（即梦）→ 会连带影响 B5 / NV5 / OC4 结论 / 定价带表 / F5 / 卡 3 / deck p.6、p.9、p.13、p.15，须同步改。
2. 修 H2（Sacra run-rate 口径）→ 会连带影响 max_assumption、bear 概率推导、F2 阈值。
3. 修 H5（deprecation 时态）→ report FP4 / 时间线 / memo 卡 7 / deck p.5、p.10 五处同步。
4. 修 H3、H4（两个 URL 不可回溯）→ 需要人工抓取替换 URL，是唯一需要联网补证的两条。
5. 修 H6、H7（标注与等级）→ 纯文本改动，可批量。
6. 修 H8、H9、H10（数值口径）→ 纯文本改动。
7. 修完 1–6 后重跑 F 节类比扫描与 E 节 ID 校验（新增 URL 时可能产生新 E 编号）。
