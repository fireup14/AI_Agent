"""电商销售数据可视化练习。

使用清洗后的固定样例数据生成图表，保证结果可以重复运行。
所有图表保存到 data_science_stack/charts/，不要求弹出 GUI 窗口。
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_DIR = Path(__file__).with_name("sample_data")
DATA_FILE = DATA_DIR / "ecommerce_sales_clean.csv"
CHART_DIR = Path(__file__).with_name("charts")

REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "category",
    "unit_price",
    "quantity",
    "sales_amount",
}


def load_visualization_data(
    file_path: str | Path = DATA_FILE,
) -> pd.DataFrame:
    """读取清洗后的数据；这是绘图前的公共准备步骤。"""

    sales = pd.read_csv(file_path, parse_dates=["order_date"])
    missing_columns = REQUIRED_COLUMNS.difference(sales.columns)
    if missing_columns:
        missing_text = ", ".join(sorted(missing_columns))
        raise ValueError(f"可视化数据缺少列：{missing_text}")
    return sales


def plot_daily_sales(
    sales: pd.DataFrame,
    output_dir: str | Path = CHART_DIR,
) -> Path:
    """题目 1：绘制每日销售额趋势折线图。

    要求：
    1. 按 order_date 汇总 sales_amount；
    2. 绘制带数据点的折线图；
    3. 添加英文标题、横轴、纵轴和网格；
    4. 保存为 daily_sales.png；
    5. 使用 tight_layout()，保存后关闭 Figure；
    6. 返回图片路径。
    """
    output_path = Path(output_dir) / "daily_sales.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    daily_sales = sales.groupby(
        "order_date",
        as_index=False,
        sort=True,
        dropna=True,
    ).agg(
        sales_amount = ("sales_amount","sum"),
    )

    figure, axes = plt.subplots(
        figsize=(8, 5),
    )
    figure.autofmt_xdate()
    axes.plot(
        daily_sales["order_date"],
        daily_sales["sales_amount"],
        marker="o",
    )
    axes.set_title("Daily Sales Trend")
    axes.set_xlabel("Order Date")
    axes.set_ylabel("Sales Amount")
    axes.grid(True)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)
    return output_path


def plot_category_sales(
    sales: pd.DataFrame,
    output_dir: str | Path = CHART_DIR,
) -> Path:
    """题目 2：绘制各品类销售总额柱状图。

    要求按销售额降序排列，添加标题和坐标轴，
    保存为 category_sales.png 并返回图片路径。
    """
    output_path = Path(output_dir) / "category_sales.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    category_sales  = sales.groupby(
        by = "category",
        as_index=False,
    ).agg(
        total_sales = ("sales_amount","sum"),
    )

    category_sales  = category_sales.sort_values(by="total_sales",ascending=False)

    figure,axes = plt.subplots()
    bars = axes.bar(
        category_sales["category"],
        category_sales["total_sales"],
    )
    axes.bar_label(bars,fmt="%.0f",padding=3)
    axes.set_title("Sales by Category")
    axes.set_xlabel("Category")
    axes.set_ylabel("Total Sales")
    axes.grid(True)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)
    return output_path


def plot_price_quantity_relationship(
    sales: pd.DataFrame,
    output_dir: str | Path = CHART_DIR,
) -> Path:
    """题目 3：绘制单价与销量关系散点图。

    要求：
    1. 横轴为 unit_price，纵轴为 quantity；
    2. 使用 category 区分颜色；
    3. 添加标题、坐标轴和图例；
    4. 保存为 price_quantity_scatter.png 并返回路径。
    """
    output_path = Path(output_dir) / "price_quantity_scatter.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure,axes = plt.subplots()
    sns.scatterplot(
        data = sales,
        x = "unit_price",
        y = "quantity",
        hue = "category",
        palette = "tab10",
        s = 80,
        marker = 'o',
        ax = axes,
    )
    axes.set_title("Unit Price vs Order Quantity")
    axes.set_xlabel("Unit Price")
    axes.set_ylabel("Order Quantity")
    axes.grid(True)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)
    return output_path


def plot_correlation_heatmap(
    sales: pd.DataFrame,
    output_dir: str | Path = CHART_DIR,
) -> Path:
    """题目 4：绘制数值变量相关性热力图。

    选择 unit_price、quantity、sales_amount，计算 corr()，
    使用 seaborn.heatmap() 显示数值，保存为 correlation_heatmap.png。
    """
    output_path = Path(output_dir) / "correlation_heatmap.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    numeric_data = sales[
        [
            "unit_price",
            "quantity",
            "sales_amount",
        ]
    ]
    correlation = numeric_data.corr()
    figure,axes = plt.subplots()
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.5,
        ax=axes,
    )
    axes.set_title("Correlation Heatmap")
    axes.set_xlabel("")
    axes.set_ylabel("")
    axes.grid(False)
    figure.tight_layout()
    figure.savefig(output_path)
    plt.close(figure)
    return output_path



def generate_all_charts(
    sales: pd.DataFrame,
    output_dir: str | Path = CHART_DIR,
) -> list[Path]:
    """题目 5：调用上述函数生成全部图表并返回路径列表。

    要求复用四个绘图函数，不要在这里重复绘图代码。
    """
    paths = [
        plot_daily_sales(sales, output_dir),
        plot_category_sales(sales, output_dir),
        plot_price_quantity_relationship(sales, output_dir),
        plot_correlation_heatmap(sales, output_dir),
    ]
    return paths



def run_checks() -> None:
    """完成全部题目后验证图表是否成功生成。"""

    sns.set_theme(style="whitegrid")
    sales = load_visualization_data()
    paths = generate_all_charts(sales)

    assert len(paths) >= 3
    assert len(set(paths)) == len(paths)
    for path in paths:
        assert path.exists(), f"图表不存在：{path}"
        assert path.stat().st_size > 0, f"图表内容为空：{path}"

    print("可视化基础验收通过：")
    for path in paths:
        print(f"- {path}")


if __name__ == "__main__":
    print(f"清洗后数据：{DATA_FILE}")
    print(f"图表输出目录：{CHART_DIR}")
    print("请完成题目 1～5，并在 analysis_findings.md 中填写分析结论。")

    run_checks()
