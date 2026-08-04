# 数据科学栈练习

本目录按照“NumPy → Pandas → 可视化”的顺序组织，所有数据均为本地生成的
小型虚构数据，不包含真实用户信息。

## 学习顺序

1. 完成 `01_numpy_basics.py`，理解数组、布尔索引、矩阵乘法、广播和聚合。
2. 完成 `02_pandas_basics.py`，从原始 CSV 完成检查、清洗、筛选、聚合与合并。
3. 完成 `03_visualization.py`，至少生成三张能够独立说明问题的图表。
4. 在 `analysis_findings.md` 中记录两条发现、证据和局限。

每个脚本末尾都有 `run_checks()`。完成对应题目后取消调用注释，再运行脚本。

## 运行命令

```powershell
python 00_Python_Advanced/data_science_stack/01_numpy_basics.py
python 00_Python_Advanced/data_science_stack/02_pandas_basics.py
python 00_Python_Advanced/data_science_stack/03_visualization.py
```

## 数据说明

- `ecommerce_sales_raw.csv`：包含缺失值和重复订单的清洗练习数据。
- `ecommerce_sales_clean.csv`：预期清洗结果，也是可视化的固定输入。
- `category_info.csv`：用于练习 `merge()` 的品类维表。

生成的图表放入 `charts/`。该目录会在绘图代码运行时创建。


pandas学习
    Series、DataFrame
    read_csv()、head()、info()、describe()
    列选择、loc、iloc
    布尔条件筛选
    缺失值和重复值
    类型转换
    创建计算列
    排序与 Top N
    groupby()、agg()
    merge()
    日期处理
    保存清洗结果