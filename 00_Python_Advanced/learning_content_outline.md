# Python 进阶内容大纲与打卡清单

本文件是 `python_advanced_data_plan.md` 的执行清单。学习时以“理解 → 编写 → 验证 → 提交”为一个完整循环。

## 0. 开始前

- [ ] 已完成 Git 学习中的本地提交、分支和 GitHub 推送。
- [ ] 已创建并激活 Python 虚拟环境。
- [ ] 已安装 NumPy、Pandas、Matplotlib、Seaborn；`mypy` 为可选。
- [ ] 已阅读 [学习计划](python_advanced_data_plan.md)。

## 1. 可维护代码

关键词：类型提示、`dataclass`、异常处理、模块职责。

- [ ] 能为函数写出参数与返回值类型。
- [ ] 理解 `list[str]`、`dict[str, int]`、`T | None` 的含义。
- [ ] 知道何时抛出、捕获和重新抛出异常。
- [ ] 为已有 Todo 小项目完成一次类型与异常处理改造。

产出：更新 `advanced_topics/04_type_hinting.py`，并提交一次 `refactor:` 或 `feat:`。

## 2. Python 运行机制

关键词：对象协议、闭包、装饰器、迭代、资源清理。

- [ ] `__str__` 与 `__repr__`
- [ ] `__len__`、`__getitem__`、运算符重载
- [ ] `functools.wraps` 与带参数装饰器
- [ ] `yield`、惰性计算、迭代器
- [ ] `with`、`__enter__`、`__exit__`、`contextlib`

产出：`Vector2D`、`@timer`、日志生成器、上下文管理器示例各一个。

## 3. 异步 I/O

关键词：协程、事件循环、任务、并发、超时。

- [ ] 会使用 `async def`、`await` 和 `asyncio.run()`。
- [ ] 会使用 `asyncio.gather()` 并发等待多个任务。
- [ ] 理解网络等待与 CPU 密集任务的区别。
- [ ] 能处理一个任务超时或失败的情形。

产出：更新 `advanced_topics/05_asyncio.py`，包含串行/并发耗时对比。

## 4. NumPy

关键词：数组、形状、索引、向量化、矩阵、广播。

- [ ] 创建与变形：`array`、`arange`、`linspace`、`reshape`
- [ ] 索引：切片、布尔索引、多维索引
- [ ] 运算：聚合、`axis`、`*` 与 `@`
- [ ] 广播与 Z-Score 归一化

产出：更新 `data_science_stack/01_numpy_basics.py`，完成矩阵验证与归一化。

## 5. Pandas

关键词：表格数据、清洗、筛选、聚合、合并。

- [ ] `Series` 与 `DataFrame`
- [ ] `head`、`info`、`describe`
- [ ] 缺失值和重复值处理
- [ ] `loc`、`iloc`、条件筛选
- [ ] `groupby`、`agg`、`merge`

产出：新建 `data_science_stack/02_pandas_basics.py`，完成电商销售分析。

## 6. 可视化与结业成果

关键词：EDA、趋势、分布、关系、相关性。

- [ ] 折线图：时间趋势
- [ ] 柱状图或直方图：分类或分布
- [ ] 散点图：两个数值变量关系
- [ ] 热力图：相关性
- [ ] 图表包含标题、坐标轴、图例；输出可复现

产出：新建 `data_science_stack/03_visualization.py`，并写出简短分析结论。

## 结业检查

- [ ] 所有脚本可独立运行。
- [ ] 每个模块至少有一次清晰的 Git 提交。
- [ ] GitHub 仓库中不包含密钥和本地环境文件。
- [ ] 能向别人解释本阶段项目使用了哪些 Python 能力。
- [ ] 已准备进入机器学习或 LLM API 阶段。
