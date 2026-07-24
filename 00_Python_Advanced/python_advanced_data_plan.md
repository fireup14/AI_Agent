# 🚀 Python 进阶与数据科学基础学习计划 (Python Advanced & Data Science Stack)

恭喜你完成了 Python 基础语法和面向对象基础的学习！

结合你的 **AI & AI Agent 学习路线图**，在进入“阶段二：深度学习与 NLP”之前，你需要跨越两座桥梁：
1. **Python 进阶语法**：在大模型框架（如 PyTorch、LangChain、LangGraph）中，高级语法（装饰器、生成器、类型提示、多进程/协程）无处不在。
2. **数据科学核心库 (NumPy, Pandas, Matplotlib)**：这是 AI 和机器学习的数据处理基石，所有模型输入本质上都是 NumPy 数组（张量的前身）。

本计划预计用时 **1-2 周**，帮你打通这两部分内容。

---

## 📅 学习日程与模块设计

| 模块 | 主题 | 核心内容 | 重要性 |
| :--- | :--- | :--- | :--- |
| **模块 1** | Python 高级特性 | 魔法方法、装饰器、生成器、类型提示 (Type Hinting) | ⭐⭐⭐⭐⭐ |
| **模块 2** | 并发编程与上下文管理 | 线程与进程、异步协程 (`asyncio`)、自定义上下文管理器 | ⭐⭐⭐⭐ |
| **模块 3** | NumPy 科学计算 | 多维数组 (`ndarray`)、向量化运算、矩阵操作、广播机制 | ⭐⭐⭐⭐⭐ |
| **模块 4** | Pandas 数据处理 | DataFrame 与 Series、数据清洗、分组聚合 (`groupby`)、数据合并 | ⭐⭐⭐⭐⭐ |
| **模块 5** | Matplotlib/Seaborn 可视化 | 绘制折线图、散点图、直方图、热力图，用于数据探索 (EDA) | ⭐⭐⭐ |

---

## 📂 推荐目录结构
建议在 `Python_Advanced` 文件夹下保持以下结构来进行代码练习：
```text
Python_Advanced/
├── python_advanced_data_plan.md  # 本学习计划文件
├── advanced_topics/              # 模块 1 & 2：高级语法练习
│   ├── 01_dunder_methods.py
│   ├── 02_decorators.py
│   ├── 03_generators.py
│   ├── 04_type_hinting.py
│   └── 05_asyncio.py
└── data_science_stack/           # 模块 3, 4 & 5：数据科学库练习
    ├── 01_numpy_basics.py
    ├── 02_pandas_basics.py
    └── 03_visualization.py
```

---

## 📖 每日详细学习内容

### 🔴 Day 1-2: Python 魔法方法与类型提示
- **学习目标**：掌握 Python 的“双下划线”魔法方法，编写规范的类型安全代码。
- **核心知识点**：
  1. **常用的魔法方法 (Dunder Methods)**：
     - `__str__` 与 `__repr__` 的区别（用户友好 vs 开发者调试）。
     - `__len__`：让你的对象支持 `len()` 函数。
     - `__getitem__` 与 `__setitem__`：让你的类对象可以像列表或字典一样通过中括号 `[index]` 取值和赋值。
  2. **类型提示 (Type Hinting)**：
     - 基础类型提示：`def add(x: int, y: int) -> int:`。
     - 复杂类型提示：从内置库 `typing` 导入 `List`, `Dict`, `Tuple`, `Union`, `Optional`, `Callable`。
     - 使用 `mypy` 静态类型检查工具。
- **实战练习**：
  - **任务 1**：设计一个 `Vector2D`（二维向量）类，实现 `__add__` (向量相加)、`__mul__` (向量数乘) 以及 `__str__` 和 `__repr__` 魔法方法。
  - **任务 2**：为你的 Day 7 命令行待办事项项目中的所有类和函数加上完整的 Type Hinting。

---

### 🔴 Day 3-4: 装饰器、生成器与上下文管理器
- **学习目标**：理解 Python 的闭包与函数式编程特性，掌握高效内存管理及自定义 `with`。
- **核心知识点**：
  1. **装饰器 (Decorators)**：
     - 理解函数是“一等公民”（可以作为参数传递、作为返回值）。
     - 编写不带参数的装饰器和带参数的装饰器。
     - 常用内置装饰器：`@property` (属性化方法), `@staticmethod`, `@classmethod`。
  2. **生成器 (Generators)**：
     - `yield` 关键字的作用与运行机制。
     - 相比于普通列表，生成器的大数据内存节省优势。
  3. **上下文管理器 (Context Managers)**：
     - 实现 `__enter__` 和 `__exit__` 方法。
     - 使用 `contextlib` 模块的 `@contextmanager` 装饰器简化编写。
- **实战练习**：
  - **任务 1：性能计时装饰器**：编写一个装饰器 `@timer`，用于测量任意函数的运行时间并打印。
  - **任务 2：大文件生成器读取**：编写一个生成器函数，按行读取一个 1GB 的大型日志文件，确保内存占用极低。
  - **任务 3：自定义数据库连接管理器**：利用上下文管理器模拟数据库的 `connect` 和 `close` 流程，确保遇到异常时也能安全关闭连接。

---

### 🔴 Day 5: 异步编程 (Asyncio) 基础
- **学习目标**：理解 Python 中单线程异步 I/O 的概念，这在编写高并发 Agent 工具调用和 API 请求时至关重要。
- **核心知识点**：
  1. **协程 (Coroutine)**：使用 `async def` 定义协程，使用 `await` 挂起阻塞的 I/O 任务。
  2. **事件循环 (Event Loop)**：`asyncio.run()` 的工作原理。
  3. **并发执行**：使用 `asyncio.gather()` 同时并发运行多个 API 请求。
- **实战练习**：
  - **任务 1：模拟并发 LLM API 请求**：模拟 5 个并行的网络请求（每个请求使用 `asyncio.sleep` 随机挂起 1-3 秒），统计使用 `asyncio.gather` 并发请求的总耗时。

---

### 🔴 Day 6-7: NumPy 科学计算 (矩阵与向量)
- **学习目标**：摆脱循环思维，转向高效的“向量化”数学计算思维，为机器学习打下坚实的矩阵基础。
- **核心知识点**：
  1. **创建阵列**：`np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`。
  2. **基本属性**：`shape`, `dtype`, `ndim`, `reshape()`。
  3. **切片与索引**：多维数组的切片，布尔索引（如 `arr[arr > 5]`）。
  4. **矩阵运算**：
     - 逐元素运算 (`+`, `-`, `*`, `/`)。
     - 矩阵乘法：`np.dot(A, B)` 或现代符号 `A @ B`。
     - 转置：`A.T`。
  5. **广播机制 (Broadcasting)**：理解不同维度数组之间自动对齐并计算的原理。
- **实战练习**：
  - **任务 1：矩阵乘法与验证**：手动用嵌套循环实现两个 $3 \times 3$ 矩阵的乘法，再使用 NumPy 的 `@` 运算符实现，对比两者的代码简洁度和运行速度（可以用 `@timer` 装饰器测量）。
  - **任务 2：数据归一化**：给定一个包含 100 行 5 列的随机数据矩阵，计算每一列的均值和标准差，并利用 NumPy 广播机制实现 Z-Score 归一化：$X_{norm} = \frac{X - \mu}{\sigma}$。

---

### 🔴 Day 8-9: Pandas 数据清洗与处理
- **学习目标**：掌握表格化数据的读取、清洗、转换和聚合，这是机器学习特征工程的核心。
- **核心知识点**：
  1. **核心对象**：`Series` (一维) 和 `DataFrame` (二维)。
  2. **读取与写入**：`pd.read_csv()`, `pd.read_excel()`, `df.to_csv()`。
  3. **数据探索**：`df.head()`, `df.info()`, `df.describe()`, `df.shape`。
  4. **数据清洗**：
     - 处理缺失值：`df.isnull()`, `df.dropna()`, `df.fillna()`。
     - 处理重复值：`df.drop_duplicates()`。
  5. **数据筛选与操作**：
     - `loc` (标签定位) 与 `iloc` (位置定位)。
     - 使用 `df.apply()` 或 `df.map()` 进行元素级变换。
  6. **高级分析**：
     - 分组与聚合：`df.groupby('category').mean()`。
     - 数据合并：`pd.concat()`, `pd.merge()`。
- **实战练习**：
  - **任务 1：电商销售数据分析**：读取一份模拟的 CSV 销售记录，完成以下任务：
    - 找出缺失值并用均值或默认值填充。
    - 统计各商品分类的总销售额和平均单价。
    - 筛选出销售额最高的前 5 个订单。

---

### 🔴 Day 10: Matplotlib & Seaborn 数据可视化
- **学习目标**：学会将复杂的数据表格转化为直观的图表，进行探索性数据分析 (EDA)。
- **核心知识点**：
  1. **折线图 (Line Plot) & 散点图 (Scatter Plot)**：展示变量间的关系与趋势。
  2. **柱状图 (Bar Plot) & 直方图 (Histogram)**：展示分类数据与数值分布。
  3. **热力图 (Heatmap)**：常用于展示特征之间的相关性系数矩阵。
- **实战练习**：
  - **任务 1**：绘制销售额随时间变化的折线图，以及商品单价与销量的散点图。
  - **任务 2**：计算特征之间的相关系数，并用 Seaborn 绘制热力图。

---

## 🛠️ 推荐第三方库安装
在开始学习前，请在终端（建议在你的虚拟环境中）安装以下库：
```bash
pip install numpy pandas matplotlib seaborn mypy
```

祝你学习顺利！这一阶段的每一项练习，都会在阶段二的 PyTorch 以及后续的机器学习实操中发挥巨大的作用。
