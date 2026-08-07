# Python 进阶学习计划

本阶段位于 Python 基础与机器学习/LLM 开发之间。目标不是覆盖所有 Python 特性，而是形成能支撑数据处理、API 调用和 AI Agent 工程的编程能力。

## 阶段目标与完成定义

- 能写出带类型标注、异常处理和清晰模块边界的 Python 程序。
- 能理解并使用装饰器、生成器、上下文管理器与 `asyncio`。
- 能用 NumPy 与 Pandas 完成一份小型数据集的清洗、分析和可视化。
- 能将学习成果按主题提交到 GitHub，而不是只保留零散脚本。

完成本阶段后，再进入经典机器学习与 LLM API 学习。

## 推荐学习节奏

建议用 10 个学习日完成；每次 2–4 小时，并保持“学习 1 小时，练习 1 小时”的比例。若某个模块没有达到完成标准，可以延长，不必为了赶日期跳过。

| 模块 | 学习日 | 主题 | 主要产出 | 完成标准 |
| --- | --- | --- | --- | --- |
| A | Day 1–2 | 可维护代码 | 类型标注、数据类、错误处理 | 为一个已有小项目补全类型与异常处理 |
| B | Day 3–4 | Python 运行机制 | 魔法方法、装饰器、生成器、上下文管理器 | 4 个独立可运行的练习 |
| C | Day 5 | 异步 I/O | 协程、任务、`gather`、超时与异常 | 并发请求模拟器 |
| D | Day 6–7 | NumPy | ndarray、索引、矩阵、广播、向量化 | 数据归一化与矩阵实验 |
| E | Day 8–9 | Pandas | 清洗、筛选、聚合、合并 | 电商销售数据分析 |
| F | Day 10 | 可视化与整合 | Matplotlib、Seaborn、EDA | 图表与简短分析报告 |

## 目录与成果组织

保持现有目录，按“一个主题一个脚本、一个模块一个提交”的方式继续扩展：

```text
00_Python_Advanced/
├── README.md                         # 可选：阶段成果说明
├── python_advanced_data_plan.md      # 本学习计划
├── learning_content_outline.md       # 知识点与任务清单
├── advanced_topics/
│   ├── 01_dunder_methods.py
│   ├── 02_decorators.py
│   ├── 03_generators.py
│   ├── 04_type_hinting.py
│   ├── 05_asyncio.py
│   └── 06_context_managers.py        # 后续新增
└── data_science_stack/
    ├── README.md
    ├── 01_numpy_basics.py
    ├── 02_pandas_basics.py
    ├── 03_visualization.py
    ├── analysis_findings.md
    └── sample_data/                   # 小型练习数据；不存放敏感或大型数据
```

> 现有 `advanced_topics/test.py` 可作为临时试验文件；可复用的正式练习请使用带序号、能说明主题的文件名。

## 模块计划

### A. 可维护代码：类型、数据与异常（Day 1–2）

学习内容：基础与复合类型、`Optional`、`Callable`、`TypedDict`/`dataclass`、函数边界、异常类型与 `try/except/else/finally`。

任务：

1. 完善 `04_type_hinting.py`，为函数、集合和返回值添加准确的类型标注。
2. 为 Python 基础阶段的 Todo 项目选择一个模块，补充类型标注与可读的异常提示。
3. 使用 `mypy`（可选）检查一个练习文件。

完成标准：能区分“正常业务分支”和“异常”，不使用裸 `except:`；函数输入、输出和可能失败的地方清楚可见。

### B. Python 运行机制（Day 3–4）

学习内容：对象表示与运算符重载、闭包与装饰器、迭代器与生成器、资源管理与上下文管理器。

任务：

1. 在 `01_dunder_methods.py` 实现 `Vector2D`：支持打印、加法、标量乘法与长度计算。
2. 在 `02_decorators.py` 实现保留函数元信息的 `@timer`，并理解 `functools.wraps`。
3. 在 `03_generators.py` 实现按行读取日志的生成器，并说明其内存优势。
4. 新建 `06_context_managers.py`，模拟资源打开、异常发生和清理的完整流程。

完成标准：能说明装饰器、生成器和上下文管理器分别解决什么问题，并为每个主题保留一个可运行示例。

### C. 异步 I/O（Day 5）

学习内容：协程、事件循环、`asyncio.create_task`、`asyncio.gather`、超时、并发异常处理。

任务：

1. 在 `05_asyncio.py` 模拟 5 个并发 API 请求。
2. 对比串行与并发运行的总耗时。
3. 为一个任务添加超时或失败情形，并保证其他任务的结果可被正确处理。

完成标准：能解释异步 I/O 适合网络/API 等等待型任务，不把它误认为 CPU 密集计算加速方案。

### D. NumPy 与向量化思维（Day 6–7）

学习内容：数组创建、形状与数据类型、切片/布尔索引、逐元素计算、矩阵乘法、广播和聚合函数。

任务：

1. 完善 `01_numpy_basics.py`，练习 `shape`、`reshape`、布尔索引和 `axis`。
2. 手写小型矩阵乘法，并用 `@` 验证结果。
3. 生成 100×5 数据矩阵，使用广播完成 Z-Score 归一化并验证每列均值接近 0、标准差接近 1。

完成标准：能够判断逐元素乘法 `*` 与矩阵乘法 `@` 的区别，并尽量用向量化替代 Python 循环。

### E. Pandas 数据处理（Day 8–9）

学习内容：`Series`、`DataFrame`、CSV 读写、数据检查、缺失值、重复值、筛选、分组聚合和合并。

任务：

1. 新建 `02_pandas_basics.py`，构造或读取一份小型电商销售数据。
2. 清洗缺失值与重复记录，输出清洗前后的数据规模。
3. 计算各品类销售额、平均单价与销售额前 5 的订单。

完成标准：从原始数据到统计结论的每一步都可重复运行，且不手工修改结果表。

### F. 可视化与阶段整合（Day 10）

学习内容：折线图、散点图、柱状图、直方图、相关性热力图；标题、坐标轴、图例和保存图片。

任务：

1. 新建 `03_visualization.py`，基于模块 E 的数据生成至少 3 张图。
2. 用不超过 200 字的 Markdown 说明：数据中最重要的两条发现、证据和可能局限。
3. 整理目录、更新本计划中的完成状态，并提交到 GitHub。

完成标准：图表能独立说明问题，代码、数据来源和结论之间能够追溯。

## 每次学习后的 Git 流程

在项目根目录执行，且只暂存本次学习有关的文件：

```bash
git status
git diff
git add 00_Python_Advanced/<本次相关文件>
git commit -m "feat: complete <学习主题>"
git push
```

提交前检查：不上传 `.env`、密钥、虚拟环境、`__pycache__/`、大型数据或模型文件。

## 环境准备

建议在独立虚拟环境中安装：

```bash
pip install numpy pandas matplotlib seaborn mypy
```

## 阶段验收项目

完成模块 F 后，提交一个“小型销售数据分析”成果：可运行的分析脚本、生成的图表（可选）以及简短结论。它将成为后续机器学习特征工程和 RAG 数据处理的基础。
