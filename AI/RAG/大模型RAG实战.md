# 前置篇：Curosr 开发环境配置
1. 安装 Cursor
2. 使用 Cursor 的基本功能
3. 配置 DeepSeek 和其他模型

# 基础篇：RAG 三问

**教学目标**：
通过三个问题，快速了解 RAG 的核心概念、应用场景和优化方向，为后续学习打下基础。

- 1、掌握 RAG 的基本概念和整体框架。
- 2、了解 RAG 的典型应用场景和优势。
- 3、明确 RAG 系统的关键优化方向和步骤。

**详细内容**：
1、**RAG 的整体框架是什么？**

- a. 详解 RAG 的三个核心组成部分：文档读取、检索和生成。
- b. RAG 的完整流程，并讲解每个环节的作用和意义。
- c. 使用 LlamaIndex 和 LangChain 快速搭建 RAG 系统。

2、**RAG 的应用场景有哪些？**
- a. 学术领域：文献综述、论文写作、知识问答等。
- b. 产业界：智能客服、销售顾问、市场分析等。
- c. 实战案例：基于 RAG 的智能客服系统。

3、**从何处入手优化 RAG 系统？**
- a. 分块策略：不同粒度对检索效率和准确度的影响。
- b. 嵌入策略：如何选择合适的嵌入模型和向量数据库。
- c. 检索策略：关键词检索、语义检索和混合检索的优缺点。
- d. 生成策略：如何控制生成内容的质量和相关性。
- e. 评估体系：如何评估 RAG 系统的性能和效果。



| 课程模块 | 内容详情 |
|----------|----------|
| **第一部分：RAG基础和 RAG 真实落地项目实战** | |
| RAG三问 | - RAG的整体框架和技术组件是什么？<br>- 如何快速搭建RAG系统？<br>- 从何处入手优化RAG系统？ |
| 安装最新版Cursor并配置DeepSeek等大模型 | 1. 安装最新版Cursor<br>  - Cursor的特点及其对AI编程的优化<br>  - 下载安装最新版本的Cursor<br>  - 配置适用于大模型开发的环境与插件<br>2. 配置DeepSeek等大模型<br>  - 安装并配置DeepSeek-V3、DeepSeek-R1<br>  - 介绍GPT-4o/DeepSeek-V3/DeepSeek-R1的区别及适用场景<br>  - 配置API调用，支持在Cursor内无缝切换不同模型 |
| 实战项目1：构建自己的 RAG 前端和后端框架 | - 设计前端界面，包括用户输入、结果展示、交互功能等<br>- 使用JavaScript、HTML、CSS等实现数据传输和交互<br>- 后端RAG系统进行API对接，实现实时前端交互<br>- 优化前端性能，提升用户体验 |
| 实战项目2：金融/医疗领域专有词汇标准化系统开发 | - 收集整理银行/医疗领域的专有词汇和相关文档<br>- 构建RAG系统，实现对专有词汇的识别和标准化 |
| 实战项目3：企业文档合规性检索和问答系统开发 | - 收集整理企业内部文档和相关法律法规、行业标准等<br>- 构建RAG系统，实现对文档的检索和识别等<br>- 对文档进行预处理，包括分词、实体识别等功能<br>- 尝试BM25、Naive RAG、混合检索等多种算法<br>- 对系统进行评估和优化，提升准确性和效率 |
| 实战项目4：基于 GraphRAG、LightRAG和LazyGraphRAG的知识图谱 RAG 系统构建 | - 收集整理知识图谱数据<br>- 基于知识图谱构建RAG系统 |
| **第二部分：RAG各组件与核心技术详细拆解** | |
| 数据导入技术 | 1. 简单文本的读取：<br>  - 使用LangChain和Llamaindex读取txt文档<br>  - 各种主要文档加载器的介绍和使用<br>2. 表格数据的导入：<br>  - 使用Unstructured处理CSV数据<br>  - 自动形成和手动指定元数据<br>3. PDF图像表格和网页数据的处理：<br>  - 使用OCR技术将网页图像中的文字<br>  - 利用LLM解析图文信息<br>  - 爬取网页数据并进行解析 |
| 文本分块技术 | 1. 分块的重要性：<br>  - 影响检索效率和准确度<br>  - 避免LLM的上下文窗口限制<br>2. 不同的分块策略：<br>  - 按大小分块：固定长度、滑动窗口等<br>  - 按格式分块：段落、章节等<br>  - 按语义分块：主题、实体等<br>3. 高级分块技巧：<br>  - 使用Tiktoken块计算Token数量<br>  - 为文本块添加元数据<br>  - 构建多层次索引 |
| 嵌入技术 | 1. 嵌入模型的原理：<br>  - 将文本转换为向量表示<br>  - 捕捉文本的语义信息<br>2. 不同嵌入模型的特点：<br>  - 商用模型：OpenAI、Cohere、VoyageAI等<br>  - 开源模型：BGE、Sentence Transformer等<br>  - 实战案例：使用OpenAI嵌入模型进行文本聚类<br>3. 嵌入模型的评估和选择：<br>  - MTEB基准测试<br>  - 稀疏嵌入和密集嵌入<br>  - 重排序模型 |
| 向量存储和索引技术 | 1. 向量数据库的工作原理：<br>  - 存储和检索文本向量<br>  - 加速语义检索<br>2. 不同向量数据库的特点：<br>  - Milvus、Weaviate、Qdrant等<br>  - 索引和搜索设置<br>  - 实战案例：使用Milvus构建RAG系统<br>3. 向量数据库的高级应用：<br>  - 混合检索和混合索引（稀疏检索+密集检索/BM25+ANN相似度检索）<br>  - 多模态检索 |
| 预检索-查询优化技术 | 1. 查询构建（Query Rewriting）：<br>  - Text-to-SQL：将自然语言转为SQL语句<br>  - Text-to-Cypher：适配图数据库的查询转换<br>  - Self-query Retriever：自动从查询中提取结构化信息<br>2. 查询优化（Query Translation）：<br>  - 查询重写（Query Rewriting）：使用LLM优化查询语句或改写原始查询以提高准确性<br>  - 查询分解（Query Decomposition）：将复杂查询拆分为多个子查询<br>  - 查询澄清（Query Clarification）：通过交互明确用户意图<br>  - 查询扩展（Query Expansion）：通过语义发散来增强查询效果<br>3. 查询路由：<br>  - 语义路由：根据查询内容选择合适的知识库<br>  - 定义路由：基于预设规则进行查询分发 |
| 提升检索准确性的方法 | 1. 检索策略：<br>  - 从小到大：节点-句子滑动窗口技术<br>  - 从粗到细：RecursiveRetriever构建多层次索引<br>  - 分层合并：组合相关节点<br>  - 混合查询：结合关键词检索和语义检索<br>2. 检索问题和解决方法：<br>  - 关键词未被检索到<br>  - 关键词排名不够高<br>  - 检索结果不全而面或过于宽泛<br>  - 检索结果过于冗长 |
| 检索后处理技术 | 1. 重排：<br>  - 根据语义相似度、时效等因素对检索结果重新排序<br>  - RRF、CrossEncoder Reranking等方法<br>2. 压缩：<br>  - 精简检索结果，避免LLM的上下文窗口限制<br>  - LLMlingua、RECOMP等方法<br>3. 校正：<br>  - 纠正检索结果中的错误和偏差<br>  - Corrective RAG等方法 |
| 生成过程中的技术 | 1. 提示设计：<br>  - 规范化生成结果<br>  - 控制生成内容的准确性和多样性<br>2. 检索结果集成方式：<br>  - 输入层集成、输出层集成和中间层集成<br>3. 高级生成技术：<br>  - Self-RAG：自我反思式生成<br>  - RRR：动态生成优化 |
| 评估检索结果的技术 | 1. 评估指标：<br>  - 检索评估：精确率、召回率、F1值等<br>  - 响应评估：语义相似度、忠实度等<br>2. 评估框架：<br>  - RAGAS、Phoenix、TruLens等<br>3. 评估结果的应用：<br>  - 优化决策策略、嵌入模型、检索算法等<br>  - 构建高性能RAG系统 |
| 复杂检索策略和范式 | 1. GraphRAG：<br>  - 利用图结构增强语义检索<br>  - 构建知识图谱，实现更精准的知识问答<br>2. Contextual Retrieval：<br>  - 基于上下文和多轮对话的高级检索策略<br>  - 实现对结构化数据的精准检索<br>3. 多模态RAG：<br>  - 融合图像、视频等多模态信息<br>  - 实现更全面的信息检索和理解<br>4. Agentic-RAG：<br>  - 基于Agent的检索和生成策略<br>  - Agent作为检索控制器，实现更智能的检索和生成<br>  - 动态检索路由（Dynamic Retrieval Planning） |
| 其他工具、论文和开源项目 | 1. Modular RAG：<br>  - 构建可插拔的RAG系统<br>  - 提高系统的“灵活性”和“扩展性”<br>2. RAG Fine-tuning：<br>  - 进一步提高LLM的性能<br>  - 结合RAG和微调技术<br>3. RAG相关论文和开源项目：<br>  - 原始论文《Retrieval-Augmented Generation for Large Language Models: A Survey》<br>  - 香港理工大学论文《A Survey on RAG Meets LLMs: Towards Retrieval-Augmented Large Language Models》<br>  - LightRAG、StructRAG、LazyGraphRAG、Agentic-RAG等新进展 |
| **加餐：DeepSeek-V3、DeepSeek-R1技术详解** | |
| DeepSeek的架构特点和性能优势 | 1. 不同规模DeepSeek模型的能力与特点：<br>  - DeepSeek-V3/vs DeepSeek-R1<br>  - 原版671B和蒸馏版 <br> - 文本、代码生成和模型推理能力分析 <br> - 对比GPT-4o/Claude等模型的优势<br>2. 不同场景下的模型选择策略：<br>  - RAG系统中的最佳实践<br>  - 本地部署 Vs API调用的选择 |
| DeepSeek核心技术创新详解 | 1. R1的推理增强架构设计<br>2. MoE（Mixture of Experts）结构：<br>  - 专家路由机制原理<br>  - 动态计算资源分配<br>  - 性能和效率的平衡<br>3. 多头潜在注意力（MLA）：<br>  - 注意力机制的改进<br>  - 上下文理解能力提升<br>4. 多令牌预测（MTP）：<br>  - 并行生成策略<br>  - 生成效率优化 |
| 如何在本地快速部署已开源的DeepSeek模型 | - 不同硬件配置下的部署选择<br> - 量化方案（4bit/8bit）对比<br> - 推理加速技术（vLLM/TGI等） |


要不要我帮你整理一份**课程模块核心要点清单**？