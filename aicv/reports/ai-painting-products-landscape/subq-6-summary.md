# SQ6：AI 绘画的版权/合规约束与 2024–2026 行业格局演变

> Explorer 子代理产出｜检索日期 2026-10-12｜深度：决策级
> 用途：产品设计输入 / PM 面试话术 / 行业理解 / 工作流优化

---

## 0. 口径说明（读表前必读）

1. **本文不含任何类比段落**。所有结论均以可核验事实、日期、金额、条款原文支撑。
2. **source_grade 定义**：A = 官方/法院文书/法规原文/财报/一审证据/标准原文；B = 头部媒体（新华社、路透、《21世纪经济报道》等）或头部机构（头部律所、头部咨询/数据机构）；C = 自媒体/百科/聚合站/AI 摘要站。
3. **状态标注**：`[已生效]` `[已判决生效]` `[审理中]` `[征求意见稿]` `[预印本]` `[待确认]` `[SINGLE_SOURCE]` `[估算]`。
4. **金额/用户量口径必须连同 unit + timepoint + scope 一起读**。例如："月访问量（SimilarWeb 口径，2026-02，全球→www.midjourney.com）= 1283万次"。
5. 诉讼部分严格区分：**程序性裁定（是否进入证据开示）** ≠ **实体判决（是否侵权）**。多个被媒体热炒的"某方胜诉"实为动议阶段裁定。

---

## 1. 版权与诉讼对照表

| # | 案件 / 法规 | 司法辖区 | 关键时间（timepoint） | 结论（原文要点） | 对 AI 绘画产品的直接影响 |
|---|---|---|---|---|---|
| 1 | **Thaler v. Perlmutter**（" Creativity Machine "生成图《A Recent Entrance to Paradise》） | 美国 D.C. Cir. | 2023-08-18 地区法院判决；**2025-03-18 上诉法院一致意见**〔已判决生效〕；2026-03-02 最高法院驳回调卷申请〔B/C 单源〕`[SINGLE_SOURCE]` | 维持版权局拒绝登记：**作品必须"be authored in the first instance by a human being"** | 纯提示词输出在美国不可登记 → 产品若在 ToS 里承诺"生成物归你、可维权"，在美国存在**登记不能**的落地落差（S12, S17） |
| 2 | **USCO《Copyright and Artificial Intelligence Part 2: Copyrightability》** | 美国（版权局） | **2025-01-29 发布**〔官方报告，非立法〕 | 现行法足以处理，**不建议为新类别立法**；"prompts alone do not provide sufficient human control"；**"Repeatedly revising prompts does not change this analysis"**；但对 AI 输出的**创作性选择、协调、安排与创造性修改**可受保护； expressive inputs 若"perceptible in the output"，该部分可受保护 | 直接规定产品侧设计取舍：**"只对出图"不可保护，"可控编辑（region remix / 修手 / 局部重绘）+ 人工后制"可保护**。这是可写入产品 Roadmap 的能力项（S12, S13, S14） |
| 3 | **USCO Part 3: Generative AI Training（预印本）** | 美国（版权局） | **2025-05-09 傍晚以 pre-publication 形式挂网**〔预印本，终版时间`[待确认]`〕 | 核心四要素分析：训练"will often be transformative"，但取决于**是否成为训练作品的 market substitute**；提出 **market dilution（市场稀释）** 损害理论；AI 模型权重**若"memorize"并体现受保护表达则可作为侵权复制品**；对训练许可市场**"recommends allowing the licensing market to continue to develop without government intervention"**（即不建议政府强制许可） | (a) 美国层面**没有法定豁免**，训练数据合法性仍是 open question；(b) 官方明确倾向"让授权市场自己长出来"→ 授权数据采购成为商业可行路线而非政府强制（S15, S16, S17） |
| 4 | **Getty Images v. Stability AI（英国）** EWHC | 英国（英格兰及威尔士高等法院，Joanna Smith J） | 2023-01 起诉；2025-06 庭审；**2025-11-04 判决**〔已判决，205页〕 | 三方皆宣称部分胜诉。**法院认定：商标侵权成立**（限特定含水印图像），且**责任在模型提供方、不能转嫁给用户**；**次要版权侵权（secondary infringement）不成立**——"**一个不存储或复制任何版权作品（也从未这样做过）的 AI 模型（如 Stable Diffusion）不属于'侵权复制品'**"；但因缺乏英国境内训练/开发证据，**直接侵权主张被撤出**，训练环节版权问题**未被实体裁判** | 两点产品含义：①输出中出现可识别权利标记/水印 = 高危，**输出侧过滤权利标记/水印是硬要求**；②在英国法下"模型本身不是侵权复制品"这一路径被认可 → 降低开放式权重模型持有方的 UK 次生侵权风险，但**训练环节在美国仍完全开放**（S1, S2, S4） |
| 5 | **Getty Images (US) v. Stability AI** N.D. Cal. 3:25-cv-06891（最初 Delaware 1:23-cv-00135，2023-02-03 立案） | 美国（加州北区，Trina L. Thompson 法官） | 2025-08-14 重立案；**2026-04-23/24 动议裁定**〔审理中，**尚未实体判决**〕 | 法院**大部分驳回 Stability 的驳回动议**：核心版权侵权主张进入证据开示；唯一被驳回的是 DMCA §1202(a) 虚假 CMI 主张，理由是起诉状缺少足够的具体故意指控——"**However, the four corners of the Complaint lack allegations to suggest a specific intent to induce, enable, facilitate, or conceal the infringement.**"；双方约定在证据开示结束后 30 天进入 ADR | **训练环节实体问题仍悬而未决**，且已进入 discovery → 任何以未授权网络数据训练的产品在美国的法律敞口在 2026-2027 才有可能收敛（S2, S3） |
| 6 | **Andersen v. Stability AI Ltd.** N.D. Cal. 3:23-cv-00201 | 美国（加州北区，William H. Orrick 法官） | 2023-01-13 立案；2023-10-30 首轮大幅驳回；**2024-08-12 允许针对四名被告（Stability / Midjourney / DeviantArt / Runway）的直接侵权与诱导侵权主张继续**；2026-01 联合文件称 Midjourney 训练材料产出接近完成；2026-02 第三次修改起诉状、2026-03 被告答辩〔**审理中，无集团认证裁定**〕 | 2024-08-12 裁定：这些产品被合理地认定为"**built to a significant extent on copyrighted works**"；同时驳回原告 DMCA 主张；保留针对 Midjourney 的 Lanham Act trade dress 主张 | 关键：针对**未自行训练、仅分发/搭建在他人模型之上**的公司保留了"诱导侵权"理论 → **接入第三方未授权模型的下游产品同样有敞口**，这是"套壳/聚合器"模式的法律边界（S5, S6, S7） |
| 7 | **Disney / Universal v. Midjourney**（后与 Warner Bros. 合并）C.D. Cal. 2:25-cv-05275 | 美国（加州中区，Kronstadt 法官 / Richlin 治安法官） | **2025-06-11 迪士尼与环球起诉**；2025-09 WBD 另行起诉；2025-11 合并；**2026-06-15/16 证据开示裁定**；程序时间表：非专家证据截止 2026-09-21、专家证据 2026-11-09、**即决判决动议截止 2026-11-23**；开庭未定，**最早 2027**〔审理中，**无任何实体/合理使用实体裁决**〕 | 诉状称 Midjourney 是"**a quintessential copyright free-rider and a bottomless pit of plagiarism**"；针对 Midjourney 索赔法定赔偿与禁令；Midjourney 以**fair use + unclean hands** 抗辩，要求制片方交出自身 AI 训练数据/模型权重/董事会 AI 战略材料；2026-06 部分准许证据开示，范围以"面向消费者的 AI 产品"为界；法院未采纳"原告自己也训练同类模型即可证明具有转换性"的论点（S9 引判决书要点）；**双方至今未获得任何实体性或合理使用裁决** | 对 PM 的意义：合理使用大概率**先在法官书面即决判决命令里出现**，而不是陪审团剧情。任何依靠"用户提示词里的 IP 角色"的产品，应在迪士尼案 2026-11-23 即决判决动议截止前完成输出侧阻断与过滤策略（S8, S9, S10, S11） |
| 8 | 邻近领域（文本 LLM）但直接影响图片侧推理的关键判例：**Bartz v. Anthropic**（2025-06-23）、**Kadrey v. Meta**（2025-06-25） | 美国 N.D. Cal. | 2025-06（两案相隔两天） | Bartz：用**合法获取**作品训练是 fair use，"transformative—spectacularly so"；但对以**盗版副本组建中央资料库**的部分不予豁免 → 2025-09 集体诉讼初步批准 **15 亿美元和解**。Kadrey：同样是 fair use，但采用"market dilution"而非仅"替代"理论 | 尽管发生在文本领域，它确立了当前美国 AI 训练 fair use 分界线：**"数据来源是否合法"比"是否了训练"更决定结果**。图片侧三起案件（Getty 英国/美国、Andersen、Disney）尚未到这一步，但产品应假定这一界线会被沿用（S16） |
| 9 | **北京互联网法院（2023）京0491民初11279 号**（李某 vs 刘某；AI 生成图《春风送来了温柔》） | 中国（北京互联网法院） | 2023-02-24 生成；2023-08-24 开庭（17 万人在线观看）；**2023-11-27 一审判决**，双方均未上诉〔**已生效**〕；2024-01-23 入选北京市高院工作报告 | 认定涉案 AI 生成图构成**美术作品**，裁判要点：**原告（使用者）是作者、享有著作权**；AI 模型本身不是我国著作权法上的作者；赔偿额选用法定赔偿下限 **500 元人民币**（索赔 5000 元） | 中国是全球极少数在成案层面承认"提示词+参数反复调试"可构成作品的国家 → 对中国 ToC 产品，"用户拥有著作权"是**可写进条款、有生效判决支撑的**；同时明确：利用人工智能生成内容**是否构成作品需个案判断、不能一概而论**（S22, S23, S24, S25） |
| 10 | **张家港市人民法院"幻之翼透明艺术椅"案**（丰某某 v 东山公司） | 中国（江苏张家港法院） | 2023-08 生成；裁判结果见 2025-07-18 最高法知识产权法庭刊文〔案例已见公开报道，判决来源`[待确认]`〕 | 与北京案**相反结论**：原告仅输入简单提示词、设置参数，**无法提供创作过程流程图等原始记录**，难以体现从构想到最终选定的独创性智力投入 → **不构成作品** | 这是 ToC 产品最实用的风险提示：中国的可版权性保护**高度依赖过程留痕**。产品若能导出"生成过程记录（提示词/参数/迭代轮次/中间图）"，就是在给用户构建举证资产（S25） |
| 11 | **广州互联网法院（2024）粤0192民初113号 奥特曼案** | 中国（广州互联网法院） | **2024-02-08 判决**；2024-02-26 媒体披露已生效〔**已生效**，被称全球首例生成式AI服务侵犯著作权生效判决〕 | 认定被告 AI 绘画功能输出构成对奥特曼美术形象的**复制权 + 改编权**双重侵权，构成**直接侵权**（不适用避风港）；中止标准被写进判决："**防范程度应达到：用户正常使用与奥特曼相关的提示词，不能生成与案涉奥特曼作品实质性相似的图片**"；判赔 **1 万元人民币**（索赔 30 万元）；同时明确服务提供者注意义务：建立举报机制、提示风险、显著标识 | 这是产品侧最硬的一条：**中国司法要求对 IP 角色做"提示词层面的不可生成"级别的关键词/语义过滤**，且仅做部分过滤不够（庭审现场演示输入"迪迦"仍能出图被认定为未达标）。此外《暂行办法》《深度合成规定》被直接用作**判断主观过错与注意义务的依据**——即行政规章在民事侵权认定中被援引（S25, S26, S27） |
| 12 | **杭州互联网法院 奥特曼 LoRA 案** | 中国（杭州互联网法院） | **2024-09 一审**〔已判决〕 | 输入侧：用户上传侵权素材训练 LoRA，平台未直接参与训练，**不构成直接侵权**；输出侧：平台对侵权模型/图片未采取过滤、屏蔽等必要措施且通过会员充值获利 → **构成帮助侵权**；判赔 **3 万元人民币** | 与广州案形成分工：**自训/自接模型 = 直接侵权；允许用户上传素材训练 LoRA 且不做输出侧管控 = 帮助侵权**。这是"允许用户训练 LoRA / 风格模型"这一功能的最直接判例约束（S25） |
| 13 | **四位插画师诉小红书 Trik AI（伊普公司 / 行吟科技）** — 全国首例涉 AI 绘画大模型训练著作权侵权案 | 中国（北京互联网法院） | **2024-06-20 开庭**；截至 2025-06 尚未作出一审判决；2026-10 状态`[待确认]` | 争议焦点：训练数据是否构成合理使用、生成内容是否与原作存在"实质性相似"；被告以"已通过用户协议获得小红书平台内容使用权"抗辩；模型训练方否认参与模型开发 | **中国训练环节尚未有生效裁判**。若产品在中国采集 UGC 内容训练，不能以"用户协议已概括授权"作为唯一法律依据 → 需建立独立的数据授权链路（S25） |
| 14 | **《生成式人工智能服务管理暂行办法》（七部门令第 15 号）** | 中国 | **2023-07-10 公布，2023-08-15 施行**〔**已生效**〕 | 适用对象：**向境内公众提供**生成文本/图片/音频/视频的服务；**通过 API 提供服务的组织、个人也算服务提供者**（第二十二条）；研发/应用但不向公众提供的不适用。**第七条**：训练数据处理须"**使用具有合法来源的数据和基础模型**"、"涉及知识产权的，不得侵害他人依法享有的知识产权"。**第十二条**：按《深度合成规定》对图片、视频等生成内容进行标识。**第十七条**：提供**具有舆论属性或者社会动员能力**的服务须做**安全评估 + 算法备案（含变更/注销备案）** | 这是中国市场准入的底座：上线前必须完成 **①数据合法来源取证链 ②内容标识 ③具备舆论属性/社会动员能力时的算法备案与安全评估 ④用户服务协议** 四件事（S18） |
| 15 | **《人工智能生成合成内容标识办法》（国信办通字〔2025〕2 号）+ 强制性国标《网络安全技术 人工智能生成合成内容标识方法》** | 中国 | **2025-03-07 印发，2025-09-01 施行**；强标**同步实施**〔**已生效**〕 | 适用：符合三条规章情形的网络信息服务提供者。**显式标识**："**在图片的适当位置添加显著的提示标识**"（第四条第三项）；提供**下载/复制/导出**功能时应确保文件中含满足要求的显式标识。**隐式标识**：须在文件**元数据**中加入"生成合成内容属性信息、服务提供者名称或编码、内容编号"；鼓励数字水印。**第六条**：传播平台须核验元数据隐式标识，未核验到但检测到痕迹的须标"疑似"。**第七条**：**应用分发平台上架审核须核验标示材料**。**第九条**：用户主动要求无显式标识内容时，可通过用户协议明确其标识义务、并**留存提供对象信息不少于六个月**后提供。**第十条**：禁止恶意删除/篡改/伪造/隐匿标识，禁止提供去标识工具 | AI 绘画产品（含 App）在中国的**硬工程清单**：出图写入可见角标（显式标识）+ 文件元数据（隐式标识）双写；出口链路保证下载文件带标识；上架 App 商店须准备标识合规材料；"去水印/无水印出图"功能必须接留痕日志 ≥6 个月（S19, S20, S21） |
| 16 | **最高人民法院《关于依法审理涉人工智能纠纷案件的意见》法发〔2026〕10 号** | 中国 | **2026-09-07 发布**（5 部分、24 条）〔**已发布实施**〕 | **第十二条**（AI 生成内容侵害著作权）：不得以"系 AI 生成"免责，按**控制能力 + 注意义务相匹配**划分开发者/提供者/使用者责任，考量因素含"**训练数据来源、各方参与度、采取的必要措施以及获利情况**"；**举证责任分配**："**人工智能开发者提出不侵权抗辩的，应当责令其提供训练数据来源、训练过程记录、模型运行模式以及科学理论依据等予以佐证**"；使用者明知/应知在先作品且生成实质相似作品并无合理抗辩的，承担侵权责任 | (a) **举证责任倒置于开发者**：模型方必须能拿出"训练数据来源 + 训练过程记录 + 模型运行模式"。这是数据合规从"法务议题"变成"工程日志议题"的分水岭。<br>(b) 民三庭庭长李剑在发布会上明确：对**AI 生成内容的可版权性**、**未经许可使用他人作品训练大模型的定性**两个问题"**意见分歧很大，认识还有待进一步深化**"，《意见》**暂不作规定** → 中国最高司法层面目前对这两点**刻意留白**（S28, S29） |
| 17 | 中国行政执法：**"清朗·整治 AI 应用乱象"专项行动** | 中国（中央网信办） | 第一阶段通报 **2026-07-06**（行动自 2026-04 启动）；第二阶段通报 **2026-09-02** | 第一阶段累计：**处置违规网站/应用程序/智能体等 AI 产品 1.4 万余款，清理违法违规信息 600 余万条，处置账号 2.6 万余个，下架违规 AI 商品 1300 余个、违规开源数据集 9 个**；整治重点明确包含"**未按规定履行大模型备案登记义务**"、"**生成合成内容标识落实不到位**"、"AI 数据投毒"。第二阶段累计：清理违法违规信息 **561 万余条**、查处账号 **4.9 万余个**、处置违规网站与应用程序 **2400 余个** | 标识办法与备案要求是**真在被执法**，且下架对象包含"违规开源数据集" → 使用第三方数据集同样在射程内；另 App 商店侧被要求"增加生成式人工智能服务备案和标识专项审核"（S31, S32） |
| 18 | **EU AI Act 第 53 条（GPAI 提供者义务）** Reg (EU) 2024/1689 | 欧盟 | **义务自 2025-08-02 适用**〔**已生效**〕；**委员会对 GPAI 的监督检查与处罚权自 2026-08-02 起取得**；**2025-08-02 前已投放市场的存量模型合规截止 2027-08-02** | 义务：编制并更新技术文档、向下游提供者提供文档、**"put in place a policy to comply with Union law on copyright and related rights, and in particular to identify and comply with, including through state-of-the-art technologies, a reservation of rights expressed pursuant to Article 4(3) of Directive (EU) 2019/790"**、按 AI Office 模板**公开训练内容摘要**。自由开源许可证发布者原则上仅承担版权政策与训练摘要义务 | 在欧盟训练/投放的模型须：**①建版权合规政策并主动遵守机器可读的 TDM opt-out（robots/元数据 ）；②发布训练内容摘要**。这是纯粹的**工程与文档成本**，且罚款《第 99 条》上限为 **3500 万欧元或全球年营业额 7%**（自 2025-08-02 起适用）（S34, S35） |
| 19 | **EU AI Act 第 50 条透明度义务（含生成式系统机器可读标记）** | 欧盟 | **2026-08-02 起适用**〔**已生效，未被推迟**〕；就 **2026-08-02 前已投放市场**的系统的标记与检测要求，经 Regulation (EU) 2026/1744 推迟至 **2026-12-02** | 提供者义务：确保自然人明确知悉其正在与 AI 系统交互；**加 machine-readable marks 以便识别 AI 生成或被操纵内容**；部署者义务：在用户接触到 deepfake 时告知。委员会于 **2026-07-20** 发布第 50 条透明度指南 | 这是欧盟侧对 AI 绘画产品**最贴近出图管线的**一条：出图需带**机器可读标记**（实际落地常见形态为 C2PA/SynthID 一类内容凭证）。对中国出海产品而言，可与国内《标识办法》的元数据隐式标识**合并为同一条工程能力**（S38） |
| 20 | **Digital Omnibus on AI：Regulation (EU) 2026/1744** | 欧盟 | 2025-11-19 提案；欧洲议会 2026-06-16 通过立场；理事会 2026-06-29 最终批准；**OJ 公布 2026-07-24；生效 2026-07-27**；法案日期 2026-07-08 | 对 AI Act 提出 **43 处修改**：Annex III 独立高风险义务推迟至 **2027-12-02**；Annex I 嵌入产品高风险推迟至 **2028-08-02**；新增禁令点（未经同意的亲密影像、儿童性剥削材料生成，自 2026-12-02）；新增第 4a 条容许为偏差纠正处理敏感数据；AI Office 获自身监督与罚款权 | **注意一个常见误读**：被推迟的是"高风险"章节，**第 50 条透明度（含 AI 生成内容机器可读标记）没有推迟**，2026-08-02 如期适用。另有文章称"2026-04-28 三方会谈崩、8 月 2 日截止如期适用"——该说法已被后续立法事实（Reg 2026/1744 生效）覆盖，以 EUR-Lex 为准（S36, S37, S38, S39） |

---

## 2. 训练数据合规化转向清单

| # | 主体 / 交易 | 时间 | 公开条款与范围 | 金额 | 证据等级 |
|---|---|---|---|---|---|
| 1 | **Adobe Firefly ← Adobe Stock** | 官方页面持续公示（无时间点，截至 2026-10 仍在线） | "**Adobe Firefly models are trained on a dataset of licensed content, such as Adobe Stock, and public domain content where copyright has expired.**"Adobe 明确：**从未在客户内容/用户内容上训练**；"We do not mine the web or video hosting sites for content."；对**企业客户提供 IP 侵权赔偿（IP indemnification）** | 未公开；训练素材量级：Adobe 官方销售材料称 trained on **375M+ 高分辨率 Adobe Stock 素材** | **A**（S40, S41） |
| 2 | **OpenAI ← Shutterstock** | 初次 2022 起，**2023-07 续签六年** | OpenAI 获取额外的 Shutterstock **training data + metadata** 用于训练；Shutterstock 获 OpenAI 新技术优先使用权；同时设立 **Contributor Fund**，向数十万名创作者就其内容用于训练给予补偿并对新生成资产的许可持续付版税 | **未披露** `[待确认]` | **C**（MediaPost 报道，S44）+ **C**（科技媒体转述 S42） |
| 3 | **Getty Images ← NVIDIA** | 2023-09 宣布 | 推出 "**Generative AI by Getty Images**"，仅用 Getty 授权图库训练（基于 NVIDIA Edify/Picasso），并对工具生成图片提供法律保护 | 未披露 | **B/C**，中文转述源为 C 级；具体条款建议以 Getty 原始新闻稿复核 `[待确认]`（S42） |
| 4 | **Getty Images ↔ OpenAI** | **2026-06-22** | 双方签**展示合作协议**：Getty 授权图库内容在 **ChatGPT 的搜索与发现场景**呈现。"getty 获得授权的图库内容将在 ChatGPT 的搜索与发现体验场景中呈现" | 未披露 | **C**（IT之家/AIBase 转述，S42, S70）`[SINGLE_SOURCE 族群]` |
| 5 | **Disney ↔ OpenAI（Sora / ChatGPT Images）** | **2025-12-11 宣布** → **2026-03-24 终止** | 三年期授权：**200+ 个 Disney / Marvel / Pixar / Star Wars 角色**（含服装、道具、载具、标志性场景），可供 **Sora 视频**与 **ChatGPT Images** 生成；**明确排除任何演员肖像与声音**；迪士尼同时对 OpenAI 做 **10 亿美元股权投资**并取得追加认股权证 | 授权费未披露；**股权投资 10 亿美元** | **A**（迪士尼官方新闻稿 + OpenAI 官网，S45）<br>**结果与反转**：新华社报道 OpenAI 于 **2026-03-24** 宣布结束 Sora 等视频生成业务，"**并终止与美国迪士尼公司含 10 亿美元投资的合作协议**"；据 FT/路透披露，**这笔投资实际并未完成交割** `[SINGLE_SOURCE 族群]`（S46） |
| 6 | **Meta ← Midjourney** | **2025-08-22** | Meta 首席 AI 官 Alexandr Wang 公布：**授权 Midjourney 的"aesthetic technology"用于 Meta 未来模型与产品**，双方研究团队协作技术共研。Holz 强调 Midjourney 仍独立、无投资人 | **未披露** | **B**（CGTN 转路透，S48） |
| 7 | **Stability AI ← EA / Sony Music / UMG / WMG / AMD Ventures / Pacific Alliance** | **2026-08-25** Series B | 官方稿同时披露：此前 2025-10 起已与 UMG、EA、WMG 签共研协议；新资金投向创意制作产品生态与应用研究，**Stable Audio 3.0 系列明确是"trained on fully licensed data"** | **B 轮 7600 万美元；累计 2.32 亿美元** | **A**（Stability AI 官方新闻稿，S43）。注意：公司累计融资口径存在差异——公司口径 2.32 亿美元 vs PitchBook 口径 4.75 亿美元 `[待确认]` |
| 8 | **MPA（美国电影协会） ↔ 字节跳动（Seedance / Seedream）** | **2026-08-17** | 达成谅解备忘录，就**加强 Seedance、Seedream 等生成式 AI 视频与图像模型的知识产权保护建立合作框架** | 未披露 | **C**（百度百科转述，S67）`[SINGLE_SOURCE]` `[待确认]` |
| 9 | **Canva ← Leonardo.ai** | **2024-07-31 宣布收购** | Leonardo 全员并入 Canva；此后以 Leonardo Phoenix 模型支撑 Canva **Dream Lab（2024-10 上线）**；Leonardo 保持独立运营、专注研发 | 报道区间 ~[待确认]2.0–3.8 亿美元，来源互相冲突：**官方未披露金额** | **C**（多为二级/三级来源）`[金额未确认]`（S49） |
| 10 | **被否决的图库整合：Getty × Shutterstock** | 2025-01-06/07 签约 → **2026-07-07 Getty 书面终止** | CMA **2026-05-15 最终报告**结论：需**剥离 Shutterstock 全部 editorial 业务**方可放行；Getty 董事会 2026-06-30 一致决议不接受该条件、终止协议。另：美国 DOJ 已于 **2026-02-23 无条件放行**。Getty 2026 Q2 10-Q 披露因终止交易计入费用：**2026 上半年 920 万美元** | 交易规模约 **37 亿美元** `[估算，C 源]` | **A**（Getty SEC 10-Q + CMA 案件页 + Shutterstock IR，S72, S73, S74）<br>延伸：Getty 10-Q 显示 **2026-06-30 现金 5,160 万美元**，循环信贷 1.5 亿美元已全额提取，并按 ASC 205-40 作出持续经营（going concern）评估披露（S73） |

**转向小结（可核验部分）**：到 2026-10，三大路线的举证密度不同——
- **自建/自有授权语料**：Adobe（Adobe Stock）与 Stability（Stable Audio 3.0 全授权数据）有**官方一级声明**可核；
- **签约采购**：Shutterstock←OpenAI、Getty←OpenAI、Disney←OpenAI、Meta←Midjourney 均已公开，但**绝大多数未披露金额**；
- **从诉讼方转为出资方**：三大唱片集团 + EA 直接投资 Stability AI（2026-08-25），是截至检索时点最有解释力的一个结构变化，具备 **A 级一级来源**（S43）。

---

## 3. 2024–2026 格局演变时间线

> 单位与口径：日期为事件发生或官方公告日；融资单位为美元；流量单位为月度访问量（SimilarWeb 口径，经第三方聚合站发布）。

| 日期 | 事件 | 类别 | 关键数值 / 条款 | 来源等级 |
|---|---|---|---|---|
| 2024-02-08 | 广州互联网法院判决奥特曼 AI 生成图片侵权，判赔 1 万元 | 司法 | 见 §1-11 | B/C（S25, S26, S27；判决日期来自律所解析文 S27） |
| 2024-07-31 | Canva 收购 Leonardo.ai | 并购 | 团队约 120 人并入；之后 2024-10 上线 Dream Lab | C（金额未确认） |
| 2024-08-01 | **Black Forest Labs 成立并同日发布 FLUX.1**（schnell Apache 2.0 / dev 非商业 / pro API-only，均为 12B） | 融资+模型 | 种子轮 **3100 万美元**，a16z 领投 | C（事实多方一致，未见公司公告负债崩裂；官方 announcement 存在但本轮未直取） |
| 2024-08-13 | xAI Grok 集成 FLUX.1 | 分发 | — | C |
| 2024-10 | Stability 发布 **Stable Diffusion 3.5**；FLUX1.1 Pro | 模型 | SD3.5 系列；FLUX1.1 Pro 称快 6 倍 | C |
| 2024-12 | Seedream 2.0 上线豆包/即梦 | 模型 | 中英双语 | C |
| 2025-01-29 | 美国版权局发布 **Part 2: Copyrightability** | 监管 | prompts alone 不足以构成作者身份 | B（S12, S13, S14） |
| 2025-04 | **Seedream 3.0** | 模型 | 原生 2K；1K 图约 3 秒；Artificial Analysis 盲测榜曾列第一（Elo ~1158 vs GPT-4o 1157）`[估算，C 源]` | C |
| 2025-03-18 | D.C. Cir. 判决 **Thaler v. Perlmutter** | 司法 | human authorship 要求被维持 | B |
| 2025-03-25 | **GPT-4o 图像生成上线 ChatGPT**（自回归，区别于 DALL·E 的扩散） | 模型 | 首周：**1.3 亿用户生成 7 亿张以上图片**；触发限流，Altman 称GPU"melting"；免费用户限额每日 3 张 | B（GIGAZINE 转 TechCrunch + Lightcap 帖子，S56） |
| 2025-04-23 | **gpt-image-1 上线 API** | 模型/价格 | 后续 gpt-image-1-mini（2025-10-06，API 成本较 gpt-image-1 低 80%）、gpt-image-1.5（2025-12-16，图输入/输出便宜 20%、生成快至 4 倍） | C（Wikipedia mirror + 二手）`[待确认具体 pricing]` |
| 2025-05-09 | 美国版权局发布 **Part 3: Generative AI Training（预印本，108 页）** | 监管 | 见 §1-3 | B/C |
| 2025-05 | FLUX.1 Kontext（图文上下文编辑） | 模型 | dev 权重 2025-06 开放 | C |
| 2025-06 | Bartz v. Anthropic / Kadrey v. Meta 同月判决 | 司法 | 见 §1-8；Bartz 后于 2025-09 初步批准 15 亿美元和解 | B |
| 2025-06-11 | **Disney + Universal 起诉 Midjourney** | 司法 | 诉状称 Midjourney 2024 年营收 3 亿美元 | B |
| 2025-08-22 | **Meta 与 Midjourney 达成美学技术授权** | 合作 | 见 §2-6 | B |
| 2025-08-26 | **Google DeepMind 公开 "nano-banana" 即 Gemini 2.5 Flash Image** | 模型 | 上线 Gemini App / AI Studio / Vertex AI；带动 "3D 手办化" 病毒传播 | C（官宣日期多源一致：2025-08-26） |
| 2025-09-01 | **中国《人工智能生成合成内容标识办法》+ 强标施行** | 监管 | 见 §1-15 | **A** |
| 2025-09-09 | **Seedream 4.0** 上线豆包 App / 即梦 AI / 扣子，用户可免费体验 | 模型 | 最高 **4K**；2025-09-18 时在 Artificial Analysis 文生图与图像编辑两榜均列第一 `[C 源]` | B/C |
| 2025-09 | Sora App 上线，5 天下载破 100 万 | 模型 | 后续见 2026-03 关停 | B |
| 2025-11-04 | **英国高等法院 Getty v Stability AI 判决** | 司法 | 见 §1-4 | A/B |
| 2025-11-25 | **FLUX.2 pro/flex/dev** 发布（32B，原生 4MP，最多 10 张参考图，Mistral 3 24B VLM 文本编码器） | 模型 | 12-16 追加 FLUX.2 max（带实时联网） | C |
| 2025-12-01 | **BFL B 轮 3 亿美元，投后 32.5 亿美元**（Salesforce Ventures + AMP 共同领投，NVIDIA / Figma Ventures / Canva 等参投） | 融资 | 累计融资超 **4.5 亿美元**；披露年收入运行率在"数千万美元/年"量级 | C（多源一致；建议以 BFL 公告复核） |
| 2025-12-11 | **Disney–OpenAI 三年授权 + 10 亿美元股权投资** | 合作 | 200+ 角色；排除真人肖像/声音 | **A** |
| 2025-12 | Seedream 4.5 | 模型 | 强化多图一致性与排版指令遵循 | C |
| 2026-01-15 | **FLUX.2 klein**（4B Apache 2.0 / 9B 非商业） | 模型/开源 | 起算 VRAM 13GB；子秒级生成 | C |
| 2026-02-10 | **Seedream 5.0** 上线剪映 / CapCut / 小云雀，即梦灰度 | 模型 | 新增检索生图（real-time RAG）+ CoT + 笔刷编辑 | C（B 源：每经对 4.0；5.0 多为 C） |
| 2026-02-23 | DOJ 无条件放行 Getty×Shutterstock（HSR 等待期届满） | 反垄断 | 但英国 CMA Phase 2 未过 | **A**（S75） |
| 2026-02-27 | **Nano Banana 2（Gemini 3.1 Flash Image）** | 模型 | 支持 4K；在保持 Flash 速度的同时下放 Pro 级质量 `[C 源]` | C |
| 2026-03-24/25 | **OpenAI 宣布终止 Sora 全线业务** | 退场 | OpenAl help center：Sora 网页/应用 **2026-04-26 停服**；**Sora API 2026-09-24 停服**；ChatGPT 内**视频**功能同步关闭，但**图像生成功能保留** | **A/B**（S47, S71, S46） |
| 2026-04-21 | **GPT Image 2 发布**；DALL·E 2/3 于 **2026-05-12** 从 API 下线 | 模型/退场 | 引入 reasoning（先规划/联网检索/自检）；定价改为 token 计量：输入图像 8 美元/百万 token、输出图像 30 美元/百万 token；实践中 1024×1024 单图约 0.006 / 0.053 / 0.211 美元（低/中/高质量）`[估算，C 源]` | C（定价部分为第三方推算，未从 OpenAI 官方定价页核验 `[待确认]`） |
| 2026-04-23/24 | **Getty v Stability AI（N.D. Cal.）驳回动议裁定** | 司法 | 核心版权主张进入 discovery；DMCA 虚假 CMI 被驳且未重提 | C（判决文本转述）+ A（Getty 财报确认诉讼状态，S2） |
| 2026-04 | 中央网信办启动"清朗·整治 AI 应用乱象"专项行动第一阶段 | 执法 | 处置 AI 产品 1.4 万余款；下架违规开源数据集 9 个 | **A**（S31） |
| 2026-06-11 | Midjourney **V8.1 成为默认模型** | 模型 | 标准约 4 秒/张，HD 约 12 秒；2K 原生；**无免费层**：Basic 10 / Standard 30 / Pro 60 / Mega 120 美元每月，年付 8 折 | C（多源一致；版本默认日期有 4 月 vs 6 月分歧 `[待确认]`） |
| 2026-06-15/16 | Disney v Midjourney 证据开示裁定 | 司法 | 部分准许 Midjourney 要求制片方交出 AI 使用材料；纯内部研发/诉讼准备材料受 work product 保护 | C（含真实引用 2026 WL 2055488，S9） |
| 2026-06-22 | **Getty ↔ OpenAI 展示合作** | 合作 | 见 §2-4 | C |
| 2026-07-07 | **Getty 书面终止 Shutterstock 合并协议** | 并购失败 | 诱因：CMA 要求剥离 Shutterstock 全部 editorial 业务 | **A**（S72, S73, S74） |
| 2026-07-20 | 欧盟委员会发布 AI Act **第 50 条透明度指南** | 监管 | 针对生成式/交互式 AI 系统与 deepfake | B（S38） |
| 2026-07-24 / 07-27 | **Digital Omnibus on AI（Reg 2026/1744）OJ 公布 / 生效** | 监管 | Annex III 高风险推迟至 2027-12-02；Annex I 至 2028-08-02；第 50 条未推迟 | **A**（S36, S37） |
| 2026-07-23 / 08-04 | BFL 发布 **FLUX 3**（Self-Flow：图片/20 秒视频/同步音频/机器人动作）；**FLUX 3 Video GA 2026-08-04**；**2026-01-15 FLUX.2 klein** | 模型 | 一个模型家族从图片扩展到视频与具身智能 | C |
| 2026-08-17 | **Google Imagen 全系下线（含 Gemini Developer API 与 Agent Platform / Vertex AI）** | 退场 | 官方迁移文档明确："**All Imagen models are deprecated and will shut down as early as August 17, 2026.**"，替代路径为 Gemini 3.x Image（Nano Banana 系列） | **A**（S53） |
| 2026-08-17 | **MPA 与字节跳动签署谅解备忘录**（Seedance / Seedream IP 保护框架） | 合作 | 见 §2-8 | C `[SINGLE_SOURCE]` |
| 2026-08-25 | **Stability AI B 轮 7600 万美元**，UMG/Sony Music/WMG/EA/AMD Ventures/Pacific Alliance Ventures 参投，累计 2.32 亿美元 | 融资 | 投向音乐/游戏/娱乐创意制作工具与专业服务；此前 2025-10/11 已与 UMG、EA、WMG 签共研 | **A**（S43） |
| 2026-09-02 | 中央网信办通报"清朗·整治 AI 应用乱象"第二阶段 | 执法 | 累计清理违法违规信息 561 万余条、查处账号 4.9 万余个、处置违规网站与应用程序 2400 余个 | **A**（S32） |
| 2026-09-07 | **最高法发布《关于依法审理涉人工智能纠纷案件的意见》法发〔2026〕10 号** | 司法政策 | 24 条；第十二条举证责任倒置；对可版权性与训练定性**留白** | **A**（S28, S29） |
| 2026-09-27 | **Reve（reve.com）停止图像生成服务** | 退场 | 2026-09-17 停止新注册与付费订阅；2026-09-27 12:00 PT 停止生成；2026-10-31 前可下载历史图；9 月扣费用户 10 月中旬全额退款。背景：披露获 OpenAI 投资，部分 AI 研究团队成员加入 OpenAI 负责多模态研究，公司法人主体保留但终止创意图像业务 | C（S65, S66） |
| 2026-10-08（报道日） | 天津和平法院适用《意见》第十二条审结首例"文字作品→AI 漫剧"改编权/信息网络传播权案，调解结案 | 司法 | 被告删除全部侵权 AI 漫剧、停止传播并赔偿经济损失及维权合理开支 | B（S30） |

**时间线里最值得 PM 记住的 5 个转折**：英国高等法院 Getty v Stability AI 判决（2025-11-04）→ ChatGPT/ Gemini 的免费分发把"C 端付费生图"挤出主流（2025-03 起）→ Sora 与 Imagen 双双退场（2026-03 / 2026-08）→ Stability 由三大唱片出资转向"娱乐制作工具"（2026-08-25）→ 中国最高法把"训练数据来源举证"压到模型方（2026-09-07）。

---

## 4. 护城河维度表

| 维度 | 代表产品/公司 | 可核验证据（带数值/时间/口径） | 可持续性判断 |
|---|---|---|---|
| **合规与版权安全（可售的"法律免责"）** | Adobe Firefly | 官方：模型训练于 Adobe Stock 授权内容 + 版权过期公共域内容；**从未用客户/用户内容训练**；企业客户提供 **IP 赔偿**。训练素材量级官方口径 **375M+ Adobe Stock 素材**（A，S40/S41） | **强、但窄**。2026 年多篇横向评测把"是否提供 IP 赔偿"列为商业交付场景下的首要筛选条件（C 源，见 §7），可支撑"合规是采购硬门槛"这一判断；但合规只在 Firefly 体系内成立，替换成本高，能力天花板也受授权语料范围约束 |
| **分发渠道与"免费 + 超级入口"捆绑** | Google Gemini / Nano Banana；ChatGPT / GPT Image | Gemini 应用的 MAU 从 2025-07 的 **~4.5 亿** 增至 2025-10 的 **~6.5 亿**（scope：Gemini 应用 MAU；`[SINGLE_SOURCE]`，C）。Nano Banana 上线一个月后 **Gemini 单月新增 2300 万用户**（C 源引 Google 官博，未能直取原文 `[待确认]`）；上线以来累计 **2 亿次以上编辑、1000 万+ 新用户尝试 Gemini**（引 Josh Woodward，C） | **最强**。超级入口不需要把图像能力单独变现，就能覆盖绝大多数一次性生成需求。Sora 的退场（2026-03-24）恰恰证明：**只有流量、没有单位经济与留存，也会被砍** |
| **工作流与既有工具链捆绑** | Adobe Creative Cloud；Canva（含 Leonardo / Dream Lab） | Canva 收购 Leonardo.ai（2024-07-31）后 2024-10 上线 Dream Lab；Canva **2025 年 ARR 约 40 亿美元、同比约 +35%**（C，`[待确认]`）。Canva 2026-04 推出自研 Canva Design Model，生成对象为**可编辑图层**而非扁平位图 | **强**。扁平位图无法进生产线，可编辑图层 + 模板批量导出才是生产路径。这也是独立出图工具向画布型工具迁移的原因之一（C 源证据薄弱，见 §7） |
| **模型能力（盲测排位）** | GPT Image 2、FLUX.2、Nano Banana Pro、Seedream 4.x/5.0 | 2026-08 Artificial Analysis 盲测榜：GPT Image 2 Elo **1370**、领先第二名**约 97 分**，为榜史最大一二名差距；同时列图像编辑榜第一（1255，领先 Nano Banana Pro 8 分）（C 源，`[待确认]`另有 LLM-Stats 盲投榜显示 GPT Image 2 得分 506/115 场，样本量小） | **弱 → 需持续再投入**。排名以月为单位换手：2025-04 Seedream 3.0 曾居首；2025-09 Seedream 4.0 双榜第一；2026-04 起 GPT Image 2 领先。单看能力不构成留存壁垒 |
| **社区与模型市场（LoRA / 工作流资产）** | 集中在中国/亚太系社区站 | 杭州互联网法院 LoRA 案（2024-09）显示"用户上传素材训练 LoRA"在司法上即有直接侵权/帮助侵权分层（A/B，S25）；同时该生态在流量侧仍活跃：2026-02 全球图片生成站点月访问量中，海艺 SeaArt **1705 万次**、Civitai 2026-06 月访问量 **688 万次**（SimilarWeb 口径经聚合站发布，C，S57/S58） | **中，但带合规包袱**。社区资产能留住重度用户，但"允许用户训练/上传"在中国已被判例划出红绳（广州/杭州两案），需在产品内实现输出侧过滤与举报闭环 |
| **价格与单位经济** | Midjourney（无外部融资、无免费层） | 诉状披露 **2024 年营收 3 亿美元**（在案文件中的原告主张，S10）；多家二级追踪估算 2025 年 **~5 亿美元 ARR**，`[估算]`；外部融资 **0 美元**（A/B，S48 中 Holz 公开声明 + 多家营收分析） | **中**。极高人效构成防御；但"无免费层 + 订阅制"的结构随 ChatGPT/Gemini 免费额度增加而承压——2026-01/02 全球图片生成月访问榜上 Midjourney 仅列第 7（1500 万次/月） |
| **垂直场景深度 + 企业关系** | 失败的对照：NeuroPixel.AI（时尚电商 AI 模特/上新图） | 该公司 2020 年成立、累计融资约 **120 万美元**（Flipkart Ventures 等），客户含 Myntra / Fabindia / Van Heusen / Decathlon，宣称降低上新图成本至多 **70%**；**2026-04 关停**。创始人自述原因：Google 发布通用图像模型后能力被抹平，且一家大客户账款逾期超 **6 个月**（C，S63/S64） | **弱** 在被通用模型直接吸收的场景；**可成立** 在数据/合规/集成深度高的场景（对应本表前两行 Adobe 与 Stability 的娱乐共研路线） |

---

## 5. 可下注判断（每条挂引用）

**判断 1｜到 2026-10，AI 绘画的主要分发权已归属"免费超级入口"，独立生图产品的 C 端付费窗口在收缩。**
- 依据：Gemini 应用 MAU 从 2025-07 的 ~4.5 亿增至 2025-10 的 ~6.5 亿（`[SINGLE_SOURCE]`，C）；SimilarWeb 口径月访问量榜上 Midjourney 2026-02 为 **1,283 万次**、同期 Canva 为 **8.58 亿次**（C，S57）；Midjourney 官网产品至今**无免费层**（C，多源一致）。
- 反例约束：流量不等于收入——Midjourney 以零外部融资做到营收（2024 年 3 亿美元由诉状披露），而同样有大流量的 Sora 在上线约 6 个月后于 2026-03-24 被关停（A/B，S47、S71）。**下注方向应为"工作流/付费意愿"，不是"流量"。**

**判断 2｜"训练数据来源举证能力"正在从法务议题变成工程议题，且是全球同步的。**
- 中国：最高法《意见》第十二条明确"**人工智能开发者提出不侵权抗辩的，应当责令其提供训练数据来源、训练过程记录、模型运行模式以及科学理论依据等予以佐证**"（2026-09-07，A，S28）；《暂行办法》第七条要求"使用具有合法来源的数据和基础模型"（2023-08-15 施行，A，S18）。
- 欧盟：AI Act 第 53 条要求 GPAI 提供者制定版权政策并**发布训练内容摘要**（2025-08-02 适用，2026-08-02 起可被罚款，最高 3500 万欧元或全球年营业额 7%）（A/B，S34、S35、S38）。
- 美国：无强制披露义务，但 USCO Part 3 倾向"让授权市场自行发展"（B/C，S15、S16）；Andersen 与 Getty 已进入 discovery（2026-03/2026-04，S7、S3）。
- **产品含义**：数据血缘（provenance）记录系统要做到"每个训练批次（batch）的授权状态可导出"，而不是只在模型卡里写一句"数据来源合规"。

**判断 3｜"允许用户拿 IP 角色/他人素材训练或使用"已无模糊空间，必须做产品级阻断，且中国的标准是世界上最严格的之一。**
- 广州案判决写进主文的标准："**防范程度应达到：用户正常使用与奥特曼相关的提示词，不能生成与案涉奥特曼作品实质性相似的图片**"（2024-02，B/C，S26）；杭州案以"平台通过会员充值获利 + 未对输出侧采取过滤屏蔽措施"认定帮助侵权（2024-09，B，S25）；美国 Disney/Universal 案虽未判实体，但原告主张禁令，且 2026-11-23 为即决判决动议截止日（S8、S9）。
- **产品含义**：IP 过滤不能只做提示词黑名单；至少要覆盖语义层级与中国 UGC 侧的上传-LoRA-输出全链路过滤。

**判断 4｜" 'IP 方能从中赚钱' 的模型，正在取代 'IP 方被侵权才起诉' 的模型。"**
- Stability AI 的 B 轮（2026-08-25）引入了 Sony Music Group / Universal Music Group / Warner Music Group / Electronic Arts —— 这是既往把 Stability 当作诉讼对手的权利方转为出资方；此前 2025-10 起双方已签共研协议（**A**，S43）。
- 同期结构：Disney 对 OpenAI 的 10 亿美元股权投资虽落地失败（2026-03-24 终止，且据 FT/路透实际未交割），方向本身明确（`[SINGLE_SOURCE 族群]`，S45、S46）；Meta 授权 Midjourney 美学技术（2025-08-22，B，S48）；MPA 与字节就 Seedance/Seedream 签知识产权保护框架 MOU（2026-08-17，C `[SINGLE_SOURCE]`，S67）。
- **风险提示**：这条路径的证据目前主要是"投资方名单变化"，而非公开的费率/分账条款 —— 上述交易的授权费率与分账条款金额**均未披露**，下注时应把"估值溢价"与"实际结算量"分开看。

**判断 5｜只做"生成"、不做"生产"的产品本身不构成业务；能进生产线（可编辑、可批量、可合规撤回）的才是。**
- 支持：Canva 于 2026-04 发布 Canva Design Model，输出为**可编辑图层对象**而非扁平位图（C）；Adobe 把 Firefly 内嵌 Photoshop/Illustrator 并对企业客户提供 IP 赔偿（A，S40）。2026 年多篇横评把"画布编辑 + 文字图层 + 多格式导出"列为硬指标（C，证据薄弱，见 §7）。
- 反例：DreamStudio 的"即显出图 + 按量积分"模式已于 2026 年退场并被重定向至面向企业与品牌团队的 Brand Studio（C，S65；官方上线时间 2026-04-08 `[待确认]`）。

---

## 6. 来源清单

| # | 来源 | 类型 | 等级 | URL | 直接引文（quote，节选） |
|---|---|---|---|---|---|
| S1 | Getty Images Newsroom | 当事方官方声明 | A | https://newsroom.gettyimages.com/en/getty-images/getty-images-issues-statement-on-ruling-in-stability-ai-uk-litigation | "NEW YORK, November 4, 2025 … Today's ruling confirms that Stable Diffusion's inclusion of Getty Images' trademarks in AI‑generated outputs infringed those trademarks." |
| S2 | Getty Images Q3 2025 Results (IR) | 财报 | A | https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-third-quarter-2025-results | "On November 4, 2025, the High Court of England & Wales issued its ruling in the company's trademark and copyright infringement suit against Stability AI Limited." |
| S3 | AI Law Wiki — Getty Images v Stability AI | 聚合/维基 | C | https://ailawwiki.com/Getty_Images_v_Stability_AI | "3:25-cv-06891-TLT … April 23, 2026: dismissal motion granted in part. The false-CMI claim was dismissed with leave to amend …" |
| S4 | 商务部 IPR 频道（译自 IPWatchdog） | 机构转载 | B | https://ipr.mofcom.gov.cn/article/gjxw/gbhj/ozqt/yg/202511/1993780.html | "2025年11月5日，英国高等法院的法官乔安娜·史密斯(Joanna Smith)…作出…裁决…这份长达205页的判决书…" |
| S5 | Cleary Gottlieb | 头部律所分析 | B | https://www.clearygottlieb.com/news-and-insights/publication-listing/significant-roadblocks-for-plaintiffs-in-generative-artificial-intelligence--lawsuit-california-judge-dismisses-most-claims-against-ai-developers-in-andersen-v-stability-ai | "Andersen's direct copyright claim against Stability survived pleading-stage review, while most other claims were dismissed with leave to amend." |
| S6 | Court Explained — Andersen v. Stability AI | 判例摘要站 | C | https://www.courtexplained.org/opinion/9610335/andersen-v-stability-ai-ltd-9610335 | "In Andersen v. Stability AI Ltd., Judge Orrick largely granted defendants' motions to dismiss, allowed amendment, and denied Midjourney's class-allegation challenge." |
| S7 | Fiund — Andersen v Stability AI | 诉讼追踪站 | C | https://fiund.com/lawsuits/andersen-v-stability | "On August 12, 2024, Judge William Orrick let direct and induced copyright infringement claims proceed against all four defendants." |
| S8 | LexSummary — Disney v. Midjourney | 判例摘要站 | C | https://lexsummary.com/?p=1702/ | "Date Decided June 16, 2026 … Magistrate Judge A. Joel Richlin partially granted and partially denied Midjourney's motion to compel." |
| S9 | TagTeam / Harvard feed（含正式判例引用） | 法学内容聚合 | B | https://tagteam.harvard.edu/hub_feeds/3621/feed_items/18649518 | "Disney Enterprises, Inc. v. Midjourney, Inc., No. 2:25-cv-05275-JAK-AJR, 2026 WL 2055488 (C.D. Cal. Jun. 15, 2026)" |
| S10 | The Straits Times（含 Reuters 供稿） | 头部媒体 | B | http://straitstimes.com.sg/life/entertainment/a-bottomless-pit-of-plagiarism-disney-universal-sue-midjourney-for-copyright-infringement | "The company … generated US$300 million (S$385 million) in revenue in 2024 alone, the studios said." |
| S11 | JD Supra（法律媒体） | B | B | https://www.jdsupra.com/legalnews/major-studios-strike-back-disney-7609015 | "… describing Midjourney as … 'bottomless pit of plagiarism.'" |
| S12 | DLA Piper | 头部律所分析 | B | https://www.dlapiper.com/insights/publications/2025/03/copyrightability-of-genai-outputs-in-the-us-key-developments | "On March 18, 2025, the US Court of Appeals for the DC Circuit issued its unanimous opinion in Thaler v. Perlmutter … because copyrightable works must 'be authored in the first instance by a human being'" |
| S13 | Sidley Austin | 头部律所分析 | B | https://www.sidley.com/en/insights/newsupdates/2025/02/us-copyright-office-issues-report-on-artificial-intelligence-and-copyrightability | "On January 29, 2025, the U.S. Copyright Office issued the second part of its Report on Copyright and Artificial Intelligence … '[R]epeatedly revising prompts…'" |
| S14 | National Law Review | B | B | https://natlawreview.com/article/usco-releases-part-2-its-report-copyright-and-artificial-intelligence?amp | "Part 2 deals with the copyrightability of AI-generated materials." |
| S15 | 知产前沿（郑友德） | 专家分析的垂媒 | C | http://www.ipforefront.com/article_show.asp?id=4792 | "美国版权局选择上周五(5月9日)傍晚…低调发布了其AI研究项目的第三部分'预印本'" |
| S16 | Ohio State University Libraries | 机构 | B | https://library.osu.edu/site/copyright/2026/03/20/fair-use-and-artificial-intelligence-2026-update/ | "Since then, Part 3: Generative AI Training of the U.S. Copyright Office's AI report was published…" |
| S17 | The Leveraged Years | 自出版资讯站 | C | https://www.theleveragedyears.com/ai-regulation-news/copyright-office-part-3-ai-training-human-authorship-2026 | "The final version of Part 3 is expected in 2026 … The cert denial, reported as March 2, 2026…" |
| S18 | 中央网信办 | 法规原文 | A | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | "《生成式人工智能服务管理暂行办法》…自2023年8月15日起施行。"；"第七条 …(一)使用具有合法来源的数据和基础模型；(二)涉及知识产权的，不得侵害他人依法享有的知识产权" |
| S19 | 中央网信办等四部门 | 法规原文 | A | https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm | "第十四条 本办法自2025年9月1日起施行。"；"第四条 …(三)在图片的适当位置添加显著的提示标识"；"第九条 …依法留存提供对象信息等相关日志不少于六个月" |
| S20 | 中国政府网（新华社） | 官方解读 | A | https://www.gov.cn/zhengce/202503/content_7014281.htm?ddtab=true | "配套强制性国家标准《网络安全技术 人工智能生成合成内容标识方法》也同时发布…将于2025年9月1日起施行" |
| S21 | 人民网（转网信办答记者问） | 官方媒体 | A | https://politics.people.com.cn/n1/2025/0314/c1001-40439289.html | "《标识办法》…自2025年9月1日起施行"；"设定《标识办法》和配套强制性国家标准6个月左右的施行过渡期" |
| S22 | 中国法院网 / 人民法院 | 法院系统媒体 | A | https://www.chinacourt.cn/article/detail/2024/02/id/7796864.shtml | "2023年末，北京互联网法院审结了李某与刘某作品署名权和信息网络传播权纠纷一案…被告公开道歉不少于24小时，并向原告赔偿500元" |
| S23 | 光明网 | 头部媒体 | B | https://m.gmw.cn/2023-11/29/content_1303585783.htm | "北京互联网法院…作出一审判决：涉案AI绘画图片具备'独创性'要件…应当被认定为作品，受到著作权法保护" |
| S24 | 北京市人大常委会（2024 高院报告） | 官方 | B | https://www.bjrd.gov.cn/zyfb/zt/16j2crdh2024/bgjd/lygzbg/202401/t20240123_3543208.html | "审结全国首例AI生成图片著作权案" |
| S25 | 最高人民法院知识产权法庭 | 最高司法机关 | A | https://ipc.court.gov.cn/zh-cn/news/view-4513.html | "2024年，广州互联网法院与杭州互联网法院相继审理了涉生成式人工智能的著作权侵权案件，两案均围绕奥特曼形象的AI生成内容展开，但裁判思路存在显著差异"；张家港案："难以体现其从最初构思到最终选定的整个过程进行了独创性的智力投入，故案涉图片不符合作品的构成要件" |
| S26 | 中国版权 Protection 中心系统文稿（转21世纪经济报道） | C | C | https://www.ccct.net.cn/html/bqzx/2024/0227/4966.html | "法院最终定下被告需要向原告赔偿经济损失为10000元（包含取证费等合理开支）"；"防范程度应达到：用户正常使用与奥特曼相关的提示词，不能生成与案涉奥特曼作品实质性相似的图片" |
| S27 | Merits & Tree（律所） | B | B | https://meritsandtree.com/Content/2024/09-26/1651065811.html | "(2024)粤0192民初113号 …2024年2月8日，广州互联网法院就某AI平台…做出判决" |
| S28 | 最高人民法院知识产权法庭 | 最高司法机关原文 | A | https://ipc.court.gov.cn/zh-cn/news/view-6033.html | "第（十二）条 …人工智能开发者提出不侵权抗辩的，应当责令其提供训练数据来源、训练过程记录、模型运行模式以及科学理论依据等予以佐证。法发〔2026〕10号 … 2026年9月7日" |
| S29 | 中国青年报（记者现场发布会） | 头部媒体 | B | https://www.toutiao.com/a7682703131808924212 | "李剑透露…对人工智能生成内容的可版权性，以及未经许可使用他人作品训练人工智能大模型的定性问题，意见分歧很大…《意见》对这两个问题暂不作规定" |
| S30 | 北方网 / 津云（天津和平法院） | 头部媒体 | B | http://news.enorth.com.cn/system/2026/10/08/059847997.shtml | "被告立即删除全部侵权AI漫剧内容，停止网络传播行为，并向原告赔偿经济损失及维权合理开支" |
| S31 | 中央网信办 | 官方通报 | A | https://www.cac.gov.cn/2026-07/06/c_1785081384384987.htm | "第一阶段累计处置违规网站、应用程序、智能体等AI产品1.4万余款，清理违法违规信息600余万条，处置账号2.6万余个，下架违规AI商品1300余个、违规开源数据集9个" |
| S32 | 中央网信办 | 官方通报 | A | https://www.cac.gov.cn/2026-09/02/c_1790099041364574.htm | "截至目前，累计清理违法违规信息561万余条，查处账号4.9万余个，处置违规网站、应用程序等2400余个" |
| S33 | 沈阳市委网信办（东北新闻网） | 地方网信部门 | B | https://liaoning.nen.com.cn/network/liaoningnews/lnnewsshehuifazhi/2026/08/05/939601358103778539.shtml | "依据《生成式人工智能服务管理暂行办法》《人工智能生成合成内容标识办法》等法律法规…且未对信息来源、人工智能生成信息等内容进行标注" |
| S34 | EU AI Act（全文站） | 法规条文 | B | https://artificialintelligenceact.eu/article/53 | "Comes into force 2 August 2025, according to Article 113(b) … (d) draw up and make publicly available a sufficiently detailed summary about the content used for training…" |
| S35 | European Commission — Digital Strategy | 官方 | A | https://digital-strategy.ec.europa.eu/en/factpages/general-purpose-ai-obligations-under-ai-act | "These obligations enter into application on 2 August 2025. … Publish a summary of the model's training content" |
| S36 | EUR-Lex / data.europa.eu | 官方法规原文 | A | https://data.europa.eu/eli/reg/2026/1744 | "REGULATION (EU) 2026/1744 … of 8 July 2026 amending Regulations (EU) 2024/1689 … OJ L, 2026/1744, 24.7.2026" |
| S37 | European Commission — Digital Strategy | 官方公告 | A | https://digital-strategy.ec.europa.eu/da/news/ai-omnibus-enters-force | "Den 27. juli 2026 træder AI-omnibussen i kraft i hele EU…" （对应英文版 "The Artificial Intelligence Omnibus entered into force on 27 July 2026"） |
| S38 | NSF（法规实施综述） | 专业机构 | B | https://www.nsf.org/life-science-regulatory-news/implementation-of-eu-ai-act | "published in the Official Journal on 24 July 2026 as Regulation 2026/1744"；"The transparency obligations for providers and deployers of certain AI systems … since 2 August 2026"；"Guidelines on transparency obligations … 20 July 2026" |
| S39 | SimpleAct.eu | 合规资讯站 | C | https://simpleact.eu/digital-omnibus-ai-act | "The European Parliament adopted its position on 16 June 2026 and the Council approved it on 29 June 2026… entered into force on the third day after that, 27 July 2026" |
| S40 | Adobe 官方（Firefly 生成式 AI 方法页） | 厂商官方 | A | https://www.adobe.com/ai/overview/firefly/gen-ai-approach.html | "Adobe Firefly models are trained on a dataset of licensed content, such as Adobe Stock, and public domain content where copyright has expired."；"We do not mine the web or video hosting sites for content."；"Adobe provides intellectual property indemnification for enterprise customers for content generated with Adobe Firefly." |
| S41 | Adobe Business（PDF） | 厂商官方 | A | https://business.adobe.com/assets/uk/pdf/supercharge-creative-teams-with-generative-ai.pdf | "Models are trained on 375M+ high-resolution, high-value Adobe Stock assets, ensuring content is ethically sourced and attributed." |
| S42 | IT之家 | 科技媒体 | C | https://www.ithome.com/0/966/758.htm | "2026年6月22日…视觉内容公司 Getty Images 宣布与 OpenAI 达成一项展示合作协议"；"2023 年 7 月，其与图片平台 Shutterstock 延续了为期六年的合作" |
| S43 | Stability AI 官方新闻稿 | 厂商官方 | A | https://stability.ai/news-updates/stability-ai-latest-funding-backed-by-entertainment-industry-biggest-names | "LOS ANGELES - AUGUST 25, 2026 - Stability AI … announced a Series B fundraise of $76M in new capital. The news brings total funding to $232M … Electronic Arts, … Sony Music Group, Universal Music Group and Warner Music Group, … AMD Ventures and Pacific Alliance Ventures."；"Stable Audio 3.0, a family of open-weight music models trained on fully licensed data." |
| S44 | MediaPost | 行业媒体 | C | https://www.mediapost.com/publications/article/387123 | "Shutterstock has signed a new six-year agreement with OpenAI … OpenAI has access to additional Shutterstock training data and meta data." |
| S45 | The Walt Disney Company 官方新闻稿 | 官方 | A | https://thewaltdisneycompany.com/press-releases/the-walt-disney-company-and-openai-reach-landmark-agreement-to-bring-beloved-characters-from-across-disneys-brands-to-sora/ | "December 11, 2025 … drawing on more than 200 Disney, Marvel, Pixar and Star Wars characters."；"Disney will make a $1 billion equity investment in OpenAI, and receive warrants to purchase additional equity."；"The agreement does not include any talent likenesses or voices." |
| S46 | 新华网 | 头部官方媒体 | B | https://www.news.cn/world/20260325/20c661ac2f5542d8b8eccd5c764af5c8/c.html | "美国开放人工智能研究中心(OpenAI)24日宣布重大战略转型举措。该人工智能初创企业将结束'天空(Sora)'应用等视频生成业务，并终止与美国迪士尼公司含10亿美元投资的合作协议" |
| S47 | OpenAI 帮助中心 | 厂商官方 | A | https://help.openai.com/zh-hans-cn/articles/20001152-what-to-know-about-the-sora-discontinuation | "Sora 网页版和应用端将于 2026 年4月 26 日停止服务。Sora API 将于 2026 年9月 24 日停止服务。" |
| S48 | CGTN（含 Reuters 供稿） | 头部媒体 | B | https://news.cgtn.com/news/2025-08-23/Meta-inks-deal-with-Midjourney-on-AI-image-and-video-generation-1G44SbBrcxW/share_amp.html | "Meta has signed a deal with generative artificial intelligence (AI) lab Midjourney to license the startup's 'aesthetic technology' for the social media company's future models and products." |
| S49 | AI Wiki — Canva AI | 聚合维基 | C | https://aiwiki.ai/wiki/canva_ai | "2024 Leonardo.ai Generative AI image platform (Australia) ~$320 million+" |
| S50 | Startuply.vc | 数据站 | C | https://startuply.vc/startup/black-forest-labs-1uhzaf | "By December 2025, the company had closed a $300 million Series B round co-led by Salesforce Ventures and AMP at a post-money valuation of $3.25 billion" |
| S51 | QuidProQuo（FLUX 家族长文） | 自出版 | C | https://quidproquo.cc/posts/tech/2026-08-26-ai-model-family-flux-en | "Series B 2025-12-01 $300M at $3.25B, co-led by Salesforce Ventures and AMP"；"Sacra estimated $96M annualized revenue by August 2025" |
| S52 | AI Wiki — FLUX.1 | 聚合维基 | C | https://aiwiki.ai/wiki/flux_1 | "Black Forest Labs emerged from stealth on August 1, 2024 … The seed round of $31 million was led by Andreessen Horowitz" |
| S53 | Google / Firebase 官方迁移文档 | 厂商官方 | A | https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization?hl=es-419 | "All Imagen models are deprecated and will shut down as early as August 17, 2026." （英文档案版：https://firebase.google.cn/docs/ai-logic/imagen-models-migration?hl=it 同义表述） |
| S54 | Wikipedia mirror（GPT Image） | C | C | https://en.wiki2.org/en/GPT_Image | "OpenAI later said that over 130 million users around the world had created more than 700 million images in the first week" |
| S55 | GIGAZINE（转 TechCrunch） | 科技媒体 | C | https://gigazine.net/gsc_news/en/20250404-chatgpt-users-generated-over-700m-images/ | "Since last Tuesday (March 26), over 130 million users have generated over 700 million images."（引 Brad Lightcap） |
| S56 | EdgeChat — Nano Banana Wiki | C | C | https://ai.miraheze.org/wiki/Nano_Banana | "Google publicly confirmed the model's identity on August 26, 2025"；"Google reported that its Gemini platform's monthly active users grew from approximately 450 million in July 2025 to 650 million by October 2025" （`[SINGLE_SOURCE]`） |
| S57 | AIBase（基于 SimilarWeb） | 数据聚合 | C | https://app.aibase.com/best-ai-tools/monthly/global-image-tools-traffic-2026-02 | "The report is based on traffic data provided by SimilarWeb … Canva Text to Image … 858.24M … Midjourney … 12.83M"（口径：全球、2026-02、月访问量） |
| S58 | AICPB（AI 产品榜） | 数据聚合 | C | https://www.aicpb.com/da/ai-rankings/products/ai-image-generator-rankings | "Hjemmeside Besøg — jun. 2026 #1 Higgsfield 27.97M … #4 Midjourney 10.30M -6.20% #9 Civitai 6.88M"（口径：网站访问量、月） |
| S59 | 新浪财经（转每经 × QuestMobile） | 头部媒体 | B | https://t.cj.sina.com.cn/articles/view/6890756658/19ab89a3204001h7k8 | "即梦AI：一季度月活1352.5万，下载量558.9万"（口径：中国大陆 AI 原生 App、QuestMobile、2026Q1） |
| S60 | 腾讯新闻（CNMO，转 QuestMobile） | C | C | https://news.qq.com/rain/a/20260429A06TZU00 | "根据QuestMobile TRUTH人工智能洞察数据库最新发布的2026年3月数据 … 豆包 … 34493万 … 即梦AI 1352万" |
| S61 | Sinolytics Radar（引 QuestMobile 2026-03） | 咨询机构 | B | https://sinolytics.de/global-business-news/blog/public/uploads/article/pdf/84/Sinolytics_Radar_232.pdf | "JIMENG AI (ByteDance) | January MAU 800 | March MAU 1,352"（单位：万；口径：中国大陆 AI 原生 App MAU） |
| S62 | ToolDirectory.ai（含 AI Graveyard 数据） | C | C | https://tooldirectory.ai/blog/state-of-ai-image-and-video-generation-2026 | "OpenAI shut down Sora … on March 24, 2026 — roughly six months after launch"；"20 of the 258 are dead or acquired, 18 of them on the image side" |
| S63 | CEO Vine（含创始人 LinkedIn 原文引述） | 自媒体 | C | https://www.ceovine.com/why-neuropixel-ai-failed-the-founders-own-words-on-getting-outgunned-overnight | "After 5 years, it's unfortunately the end of the road for us at NeuroPixel.AI"；"we got massively outgunned overnight sometime in late 2025" |
| S64 | The AI Cemetery | C | C | https://theaicemetery.com/neuropixel-ai | "Reports in April 2026 said NeuroPixel.AI shut down amid rising competition and financial pressure." |
| S65 | ToolChase（DreamStudio 状态页） | C | C | https://toolchase.com/tool/dreamstudio | "As of 2 August 2026: dreamstudio.ai returns a 301 redirect to brandstudio.com" |
| S66 | DigitalToday（Reve 关停） | 媒体 | C | https://www.digitaltoday.co.kr/en/view/105109/startup-reve-to-end-image-generation-service-after-openai-investment-sept-27 | "Reve said image generation on reve.com will be unavailable from 12 p.m. Pacific time on Sept. 27" |
| S67 | 百度百科 — Seedream | C | C | https://baike.baidu.com/item/Seedream/67390954 | "当地时间8月17日，美国电影协会(MPA)与字节跳动宣布达成谅解备忘录，就加强Seedance､Seedream等生成式AI视频和图像模型的知识产权保护建立合作框架" |
| S68 | 每日经济新闻（经今日头条） | 头部媒体 | B | https://www.toutiao.com/article/7547949057466221066 | "9月9日，字节跳动Seed团队宣布推出豆包图像创作模型Seedream 4.0 … 用户可以在豆包App、即梦AI、扣子等产品正式上线，用户可以免费体验" |
| S69 | LLM-Stats（盲投榜） | C | C | https://llm-stats.com/leaderboards/best-ai-for-image-generation | "Updated September 4, 2026 … 1 GPT Image 2 506 115 matches" |
| S70 | AIBase（中文版流量榜） | C | C | https://app.aibase.com/zh/best-ai-tools/monthly/global-imgen-traffic-2026-01 | "#7 Midjourney 图片生成 1499.81万"（口径：SimilarWeb、全球、2026-01 月访问量） |
| S71 | 中国科学网 / 澎湃新闻 | 头部媒体 | B | https://news.sciencenet.cn/htmlnews/2026/3/561934.shtm | "当地时间3月25日，OpenAI宣布将停止使用其视频生成工具Sora"；"据Appfigures数据显示，Sora在去年12月的下载量环比下降了32%，今年1月继续下降45%" |
| S72 | Getty Images 2026 Q2 10-Q（SEC 存档） | 财报原文 | A | https://investors.gettyimages.com/node/16391/html | "As of June 30, 2026, the Company had cash and cash equivalents of approximately $51.6 million"；"On June 30, 2026, the Board of Directors of Getty Images unanimously resolved (a) not to proceed with the process to sell Shutterstock's editorial business…" |
| S73 | UK CMA 案件页 | 官方监管 | A | http://dft.gov.uk/cma-cases/getty-images-slash-shutterstock-merger-inquiry | "8 July 2026: The CMA has cancelled its merger inquiry into the anticipated acquisition by Getty Images Holdings, Inc. of Shutterstock, Inc. … Outcome: Mergers - phase 2 cancellation" |
| S74 | Shutterstock Investor Relations | 官方 IR | A | https://investor.shutterstock.com/node/14586/pdf | "February 23, 2026 — Getty Images … and Shutterstock … announced today that the United States Department of Justice (DOJ) has concluded its review … without conditions." |
| S75 | FreeAI（含 Artificial Analysis 榜引述） | C | C | http://freeai.help/blog/gpt-image-2-dominates-ai-image-leaderboard-august-2026-en-719384 | "As of August, it sits at Elo 1,370 with a lead of approximately 97 points over second place" |
| S76 | 吕梁市离石区人民法院（山西省高院系统） | 法院系统 | B | https://lllsfy.shanxify.gov.cn/article/detail/2026/09/id/9503511.shtml | "图片、视频的显式标识应当放置在画面边缘或四角，字体清晰可辨识，文字高度不低于画面最短边长度的5%，主动向公众提示该内容由AI生成" |

---

## 7. 查不到 / 证据薄弱清单（诚实边界）

| # | 事项 | 状态 | 说明与建议下一步 |
|---|---|---|---|
| 1 | **OpenAI–Shutterstock 续约金额**（六年协议的金额/版税条款） | `[待确认]` | 多家媒体只写"six-year agreement"，未披露金额。建议查 Shutterstock 10-K/10-Q 的 material contracts 段落 |
| 2 | **Getty–NVIDIA 具体条款与上线时间** | `[待确认]` | 仅见二手转述"Generative AI by Getty Images…承诺为使用该工具生成的图片提供法律保护"。建议查 Getty 2023-09 官方 newsroom 原始稿 |
| 3 | **Canva 收购 Leonardo.ai 金额** | `[未确认]` | 已见三个互相冲突的报道值（约 2.0 亿美元 / 约 3.0–3.2 亿美元 / 约 3.8 亿美元）；Canva 仅承认"现金+股票"混合支付，**官方未披露数字**。建议在正式汇报中只写"报道区间约 2.0–3.8 亿美元，未获官方确认" |
| 4 | **Stability AI 累计融资**：公司口径 2.32 亿美元 vs PitchBook 口径 4.75 亿美元 | `[待确认]` | 官方 A 级来源是 2.32 亿；PitchBook 数值来自第三方。汇报时按"公司口径"表述并注明差异 |
| 5 | **Gemini 应用 MAU 450M(2025-07) → 650M(2025-10)、Nano Banana 单月 2300 万新增用户** | `[SINGLE_SOURCE]` | 唯一可用来源是 AI 维基类聚合站（C 级）。建议改为引用 Google/Alphabet 季报或官方博客；本次未能直取原文 |
| 6 | **Midjourney 2025 年 ~5 亿美元 ARR** | `[估算]` | 公司不披露财务。可靠锚点仅两处：①诉状披露 2024 年 3 亿美元；②Holz 公开声明"无投资者"。其余均为 Sacra/第三方估算，且"员工数 40 vs 163"两组估算本身互相冲突 |
| 7 | **Disney 对 OpenAI 的 10 亿美元投资是否实际交割** | `[SINGLE_SOURCE 族群]` 且互相加强 | 新华社引 FT/路透称"这笔交易最终未能达成"，迪士尼仅确认协议终止。建议查 OpenAI/Disney 8-K 或 Disney FY2026 财报中的投资披露 |
| 8 | **DreamStudio → Brand Studio 的确切转型时间点** | `[待确认]` | 一份 C 源称 Brand Studio 于 2026-04-08 上线、dreamstudio.ai 2026-08-02 起 301 重定向；另一份 C 源在 2026-03 仍称 DreamStudio 正常运营。建议直连 stability.ai 新闻室与站点核验 |
| 9 | **Reve 关停的确切年份** | 推断为 2026-09（未见矛盾证据） | DigitalToday 原文无年份；按文中"去年3月发布 Reve Image 1.0"与 2026-09-21 周报归属推断为 2026。建议以 Reve 官方博客原文确认 |
| 10 | **中国"AI 生成内容可版权性"与"未授权训练的正当性"** | **最高人民法院明确留白**（不是"查不到"，是官方暂无态度） | 民三庭庭长李剑 2026-09-07 发布会明确两问题"意见分歧很大…《意见》对这两个问题暂不作规定"。任何声称"中国已认定 AI 训练是否侵权"的说法均与事实不符 |
| 11 | **四位插画师诉 Trik AI 案的一审判决结果** | `[待确认]` | 可核验信息只到 2024-06-20 开庭、2025-06 仍未宣判。未找到 2025-07 之后的一审判决书或权威报道 |
| 12 | **短板：Civitai / SeaArt 等社区的收入、留存、付费转化** | 无证据 | 仅有 SimilarWeb 访问量（C 级）。没有可用于决策的收入/留存数据 |
| 13 | **短板：中国 AI 绘画 App 的付费收入口径** | 无证据 | QuestMobile 提供 MAU/下载量，未提供付费额。七麦数据本次未检索到可直接引用的公开榜。AI 产品榜（AICPB）为网站访问量口径，与中国 App MAU 口径不可直接比较 |
| 14 | **短板：FLUX / Black Forest Labs 的收入** | `[估算]` | 仅见 Sacra 估算 ~96M 美元年化（2025-08）与官方口径"数千万美元/年"。无 A 级财报 |
| 15 | **短板：2026 年 AI 绘画整体的市场规模/付费规模** | 不可用 | 检索到的市场测算文章（如某 2026 全景文宣称 2026 年 32 亿美元）来自营销型内容站，且方法不透明，**未纳入本报告** |

---

### 附：给 PM 面试的"一页版"（可直接口播）

1. **训练环节是否侵权，全球三个主要辖区到 2026-10 都还没有终局答案**：美国 USCO Part 3 是预印本、Andersen 与 Getty 都在 discovery、Disney v Midjourney 最早 2027 才可能开庭；中国最高法 2026-09-07《意见》**明确对"AI 生成内容可版权性"与"未授权训练的定性"留白**。
2. **但"举证责任"已经落地**：中国最高法第十二条要求开发者不侵权抗辩时必须提供"训练数据来源、训练过程记录、模型运行模式"；欧盟 AI Act 第 53 条要求公开训练内容摘要；两者都意味着**合规 = 数据血缘系统**。
3. **中国对 IP 角色的过滤标准写到判决主文**：必须用"用户正常使用相关提示词无法生成实质性相似图片"的程度做验证，不是黑名单能过关的。
4. **合规标识已从"规定"变成"执法"**：2026-04 起的两个阶段行动，处置 AI 产品 1.4 万余款、下架违规开源数据集 9 个。
5. **被免费分发重创的是纯出图工具**：Imagen 全系 2026-08-17 下线、Sora 2026-03-24 宣布终止、Reve 2026-09-27 停服、DreamStudio 转向 Brand Studio；而 Midjourney 靠无免费层 + 高人效活下来（2024 年营收 3 亿美元、零外部融资）。这是"押流量 vs 押工作流"的分水岭。
