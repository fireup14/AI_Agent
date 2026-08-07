# 🤖 大模型应用开发与智能体 (LLM App & Agent) 进阶学习计划

由于你选择先跳过数据科学三剑客（NumPy, Pandas, Matplotlib），我们的学习路线将直接从 **“Python 进阶语法”** 跨越到 **“大模型应用开发与工程化”**。

这一路线在工业界被称为 **LLM 应用工程师 / 智能体研发工程师 (LLM Application Developer)**。它的核心是不从零训练模型，而是通过 API、Prompt、工程框架和系统架构设计，将大模型组合成高可靠、高自动化的 Agent 系统。

---

## 📅 阶段学习日程概览

| 阶段 | 主题 | 核心内容 | 预计耗时 |
| :--- | :--- | :--- | :--- |
| **阶段 1** | 工程开发工具链 | Git 版本控制、Linux 常用操作、Docker 容器化基础 | 3-5 天 |
| **阶段 2** | 大模型 API 与结构化输出 | OpenAI/DeepSeek API 交互、Stream 模式、Pydantic 结构化数据提取 | 3-4 天 |
| **阶段 3** | LLM 框架 (LangChain/LlamaIndex) | 提示词模板、LCEL 链式表达、Memory 对话上下文管理 | 5-7 天 |
| **阶段 4** | 向量数据库与轻量级 RAG | 文档加载切分、Embedding 向量化、ChromaDB 向量检索 | 4-5 天 |
| **阶段 5** | 智能体开发 (Agent & LangGraph) | Tool Calling (工具调用)、ReAct 单智能体、LangGraph 复杂状态机 | 7-10 天 |

---

## 📂 推荐目录结构
建议在当前工作区下创建 `LLM_Agent_Learning` 文件夹来存放后续代码：
```text
AI_Agent/
├── LLM_Agent_Learning/
│   ├── 01_engineering_tools/    # Docker 与 Git 练习
│   ├── 02_llm_api/               # API 基础与 Pydantic 结构化
│   │   ├── basic_call.py
│   │   └── structured_output.py
│   ├── 03_langchain/             # LangChain 链式调用与 Memory
│   │   └── lcel_demo.py
│   ├── 04_rag_lite/              # 简易检索增强生成 (RAG)
│   │   └── chromadb_demo.py
│   └── 05_agent_graph/           # 智能体开发
│       ├── tool_calling.py
│       └── langgraph_agent.py
```

---

## 📖 各阶段详细学习内容与实践任务

### 🔴 阶段 1: 工程开发工具链 (筑基工程)
- **学习目标**：掌握现代后端与 AI 开发必备的环境配置与容器化工具，为你后续在 Docker 中运行向量数据库和隔离沙箱做准备。
- **核心知识点**：
  1. **Git**：克隆、分支管理（`branch`/`checkout`）、代码合并（`merge`）、解决冲突、提交规范。
  2. **Linux**：常用命令（`ls`, `cd`, `pwd`, `mkdir`, `rm`, `ps`, `kill`, `chmod`, `nohup`）、环境变量配置（`.bashrc`）。
  3. **Docker**：镜像（Image）与容器（Container）概念、常用命令（`docker pull`, `run`, `ps`, `exec`, `logs`, `stop`）、编写简单的 `Dockerfile`、多容器管理工具 `docker-compose`。
- **实战练习**：
  - **任务 1**：编写一个简单的 Python 脚本，并使用 `Dockerfile` 将其打包成 Docker 镜像，在本地容器中成功运行。

---

### 🔴 阶段 2: 大模型 API 与结构化输出 (数据骨架)
- **学习目标**：深入理解大模型的输入输出协议，掌握如何让大模型 100% 返回符合程序要求的 JSON 数据结构。
- **核心知识点**：
  1. **大模型 API**：使用官方客户端（如 `openai` 库），调用 `ChatCompletion`。理解 `system`, `user`, `assistant` 角色。
  2. **流式传输 (Streaming)**：如何利用生成器逐字获取模型输出，提升用户体验。
  3. **Pydantic**：数据验证与类型提示库。定义 `BaseModel`、类型校验、嵌套模型。
  4. **结构化输出 (Structured Outputs)**：将 Pydantic 模版传给 API 的 `response_format` 参数，确保大模型输出稳定的 JSON 格式。
- **实战练习**：
  - **任务 1**：编写脚本调用 DeepSeek 或 OpenAI API，支持输入 Prompt 并通过 `stream` 逐字打印。
  - **任务 2**：设计一个 Pydantic 模型 `MovieInfo`（包含电影名、上映年份、导演、演员列表、评分），让大模型阅读一段影评后提取对应字段，并自动解析为 Python 的 Pydantic 对象。

---

### 🔴 阶段 3: LLM 框架 (LangChain & LCEL)
- **学习目标**：掌握大模型生态中最主流的框架，学会用工程化的方式连接组件。
- **核心知识点**：
  1. **PromptTemplate**：如何动态插值生成提示词。
  2. **LCEL (LangChain Expression Language)**：使用 `|` 运算符把提示词、大模型和输出解析器（Parser）链式拼接。
  3. **对话上下文 (Memory)**：如何管理多轮对话历史，并在每次请求时合理截断或总结。
- **实战练习**：
  - **任务 1**：使用 LCEL 搭建一条链路：用户输入 -> 提示词模板（翻译成英文） -> 大模型 -> 字符串解析输出。
  - **任务 2**：设计一个带记忆窗口的命令行聊天机器人，能够记住最近的 5 轮对话历史。

---

### 🔴 阶段 4: 向量数据库与轻量级 RAG
- **学习目标**：让大模型能够访问你本地的专属文档，解决幻觉问题。
- **核心知识点**：
  1. **文档加载与切片**：使用文本加载器（Loader）加载 txt/markdown，使用字符切分器（Splitter）分割成小块（Chunk）。
  2. **Embedding 模型**：将文本 Chunk 转换为向量的原理及接口调用。
  3. **ChromaDB（本地向量库）**：初始化数据库、创建 Collection、写入向量数据、执行相似度查询（Similarity Search）。
  4. **检索增强生成 (RAG) 闭环**：检索与输入最相关的 Top-K 个文本块，拼接到提示词中，让大模型基于参考资料回答问题。
- **实战练习**：
  - **任务 1**：在本地创建一个含有你个人备忘录的文件夹，读取这些文件并写入 Chroma 向量库，最后实现“基于我本地备忘录的智能问答助手”。

---

### 🔴 阶段 5: 智能体开发 (Agent & LangGraph)
- **学习目标**：理解 Agent 的运行机制，能够开发具备“推理-工具调用-执行-反思”闭环的自主运行智能体。
- **核心知识点**：
  1. **工具调用 (Tool Calling/Function Calling)**：向大模型提供函数声明，模型自动判断是否需要调用、并输出对应的函数参数。
  2. **ReAct 智能体模式**：让模型自主循环执行：Reasoning（思考） -> Action（执行工具） -> Observation（观察结果） -> Repeat。
  3. **LangGraph 状态图基础**：
     - 理解 Node（节点，执行计算）和 Edge（边，控制逻辑流向）。
     - State（图的状态，贯穿所有节点的全局共享数据）。
     - 实现分支决策（Conditional Edges）。
- **实战练习**：
  - **任务 1：天气/计算查询 Agent**：写两个本地函数（例如 `get_weather(city)` 和 `calculate(expression)`），注册为大模型的工具，实现一个可以通过调用这些工具解决复杂问题的 Agent。
  - **任务 2：LangGraph 工作流**：设计一个翻译 Agent 图流程：输入草稿 -> 节点 A 翻译 -> 节点 B 语法校对 -> 节点 C 润色输出。

---

## 🛠️ 下一阶段工具包准备
你可以使用 `pip` 在本地安装以下大模型应用开发常用库：
```bash
pip install openai pydantic langchain langchain-openai langchain-community chromadb langgraph
```
