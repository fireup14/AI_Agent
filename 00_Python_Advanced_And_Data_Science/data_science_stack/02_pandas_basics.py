"""Pandas 电商销售数据练习。

数据处理目标：
读取原始 CSV → 检查质量 → 清洗 → 筛选 → 聚合 → 合并 → 保存结果。

本文件只提供函数契约、题目要求和验收代码，不包含 TODO 的实现答案。
"""

from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).with_name("sample_data")
RAW_SALES_FILE = DATA_DIR / "ecommerce_sales_raw.csv"
CATEGORY_FILE = DATA_DIR / "category_info.csv"
CLEAN_SALES_FILE = DATA_DIR / "ecommerce_sales_clean.csv"

REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "category",
    "product",
    "unit_price",
    "quantity",
    "region",
    "payment_method",
}


def load_sales(file_path: str | Path = RAW_SALES_FILE) -> pd.DataFrame:
    """题目 1：读取原始销售 CSV。

    要求：
    1. 使用 pd.read_csv；
    2. 将 order_date 解析为日期类型；
    3. 检查 REQUIRED_COLUMNS 是否全部存在；
    4. 缺少列时抛出 ValueError；
    5. 返回 DataFrame。
    """
    sales = pd.read_csv(
        file_path,
        parse_dates=["order_date"],
    )

    missing_columns = REQUIRED_COLUMNS.difference(sales.columns)

    if missing_columns:
        raise ValueError(f"存在缺失列:{missing_columns}")

    return sales

def inspect_sales(sales: pd.DataFrame) -> None:
    """题目 2：检查数据结构与质量。

    要求输出：
    1. head()；
    2. info()；
    3. 数值列 describe()；
    4. 每列缺失值数量；
    5. 重复行数量。

    本函数只做检查和输出，不修改 sales。
    """
    print("---------------------数值head---------------------")
    print(sales.head())
    print("---------------------数值结构---------------------")
    sales.info()
    print("---------------------数值统计---------------------")
    # print(sales.describe(include="all"))
    print(sales.describe())
    print("---------------------lose---------------------")
    print(sales.isna().sum())
    print("---------------------repeat---------------------")
    print(f"重复行数量：{sales.duplicated().sum()}")

def clean_sales(sales: pd.DataFrame) -> pd.DataFrame:
    """题目 3：清洗原始销售数据。

    要求：
    1. 使用 copy()，不得修改调用者传入的 DataFrame；
    2. 根据 order_id 删除重复订单，保留第一次出现的数据；
    3. category 缺失值填充为 "Unknown"；
    4. unit_price 和 quantity 转换为数值，非法值转为缺失值；
    5. 删除日期、单价或数量缺失的记录；
    6. 仅保留单价和数量都大于 0 的记录；
    7. 新增 sales_amount = unit_price * quantity；
    8. 重置索引后返回结果。
    """
    cleaned = sales.copy()
    cleaned = cleaned.drop_duplicates(
        subset=["order_id"],
        keep="first",
    )

    cleaned["category"] = cleaned["category"].fillna("Unknown")

    cleaned["unit_price"] = pd.to_numeric(
        cleaned["unit_price"],
        errors = "coerce",
    )

    cleaned["quantity"] = pd.to_numeric(
        cleaned["quantity"],
        errors="coerce",
    )

    cleaned = cleaned.dropna(
        subset=[
            "order_date",
            "unit_price",
            "quantity",
        ]
    )

    valid_price = cleaned["unit_price"] > 0
    valid_quantity = cleaned["quantity"] > 0
    valid_rows = valid_price & valid_quantity
    cleaned = cleaned.loc[valid_rows].copy()

    cleaned["sales_amount"] = cleaned["unit_price"] * cleaned["quantity"]

    cleaned = cleaned.reset_index(drop = True)

    return cleaned

def select_sales(
    sales: pd.DataFrame,
    category: str,
    minimum_amount: float,
) -> pd.DataFrame:
    """题目 4：使用 loc 和布尔条件筛选订单。

    返回指定 category 且 sales_amount 不低于 minimum_amount 的记录，
    并按 sales_amount 从高到低排序。
    """
    select = sales.copy()

    valid_category = select["category"] == category
    valid_sales = select["sales_amount"] >= minimum_amount
    select = select.loc[valid_category & valid_sales].copy()

    select = select.sort_values(
        by = "sales_amount",
        ascending = False
    )

    select = select.reset_index(drop=True)

    return select

def summarize_by_category(sales: pd.DataFrame) -> pd.DataFrame:
    """题目 5：按品类分组聚合。

    使用 groupby() 和 agg()，为每个 category 计算：
    1. order_count ：订单数量；
    2. total_quantity ：商品总数量；
    3. average_unit_price ：平均单价；
    4. total_sales ：销售总额。

    最终按 total_sales 从高到低排序。
    """
    ### 方法一 ###
    # grouped_sales_amount = sales.groupby("category")["sales_amount"].sum()
    # grouped_unit_price = sales.groupby("category")["unit_price"].mean()
    # grouped_quantity = sales.groupby("category")["quantity"].sum()
    # grouped_order_count = sales.groupby("category").size()
    # grouped = pd.DataFrame({
    #     "order_count": grouped_order_count,
    #     "total_quantity": grouped_quantity,
    #     "average_unit_price": grouped_unit_price,
    #     "total_sales": grouped_sales_amount,
    # })
    # grouped = grouped.sort_values(by="total_sales", ascending=False)
    # print(grouped.head())
    # return grouped

    ### 方法二 ###
    summary = sales.groupby("category",as_index=False,).agg(
        order_count=("order_id", "count"),
        total_quantity=("quantity", "sum"),
        average_unit_price=("unit_price", "mean"),
        total_sales=("sales_amount", "sum"),
    )
    summary = summary.sort_values(
        by = "total_sales",
        ascending = False,
    )
    summary = summary.reset_index(drop=True)
    return summary

def top_orders(sales: pd.DataFrame, count: int = 5) -> pd.DataFrame:
    """题目 6：返回销售额最高的 count 个订单。

    count 小于或等于 0 时抛出 ValueError。
    结果至少包含 order_id、category、product 和 sales_amount。
    """
    if count <= 0:
        raise ValueError("count 小于或等于 0")
    else:
        count = min(count, sales.shape[0])

    ### 方法一 ###
    # top = sales.sort_values(
    #     by = "sales_amount",
    #     ascending=False,
    # ).head(count).reset_index(drop = True)
    # top = top[["order_id", "category", "product", "sales_amount"]].copy()
    # return top

    ### 方法二 ###
    top = sales.nlargest(count,"sales_amount",keep="first",).reset_index(drop = True)
    top = top[["order_id", "category", "product", "sales_amount"]].copy()
    return top

def merge_category_info(
    summary: pd.DataFrame,
    category_file: str | Path = CATEGORY_FILE,
) -> pd.DataFrame:
    """题目 7：将品类汇总结果与品类信息表合并。

    要求：
    1. 读取 category_info.csv；
    2. 使用 merge() 按 category 左连接；
    3. 验证合并前后汇总表行数不变；
    4. 返回合并结果。
    """
    category_info = pd.read_csv(category_file)

    merged = pd.merge(
        summary,
        category_info,
        on = "category",
        how = "left",
        validate = "one_to_one",
    )

    before_count = len(summary)
    after_count = len(merged)
    if before_count != after_count:
        raise ValueError("合并前后汇总表行数不同")

    return merged






def run_checks() -> None:
    """完成全部题目后运行的基础验收。"""

    raw_sales = load_sales()
    # inspect_sales(raw_sales)
    original_shape = raw_sales.shape
    cleaned = clean_sales(raw_sales)

    assert raw_sales.shape == original_shape, "clean_sales 不应修改原始数据"
    assert cleaned["order_id"].is_unique
    assert cleaned["unit_price"].notna().all()
    assert cleaned["quantity"].notna().all()
    assert (cleaned["unit_price"] > 0).all()
    assert (cleaned["quantity"] > 0).all()
    assert "sales_amount" in cleaned.columns

    expected = pd.read_csv(CLEAN_SALES_FILE, parse_dates=["order_date"])
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True),
        expected.reset_index(drop=True),
        check_dtype=False,
    )

    summary = summarize_by_category(cleaned)
    assert {
        "category",
        "order_count",
        "total_quantity",
        "average_unit_price",
        "total_sales",
    }.issubset(summary.columns)

    assert len(top_orders(cleaned, 5)) == 5
    merged = merge_category_info(summary)
    assert len(merged) == len(summary)

    print("Pandas 基础验收通过。")


if __name__ == "__main__":
    print(f"原始练习数据：{RAW_SALES_FILE}")
    print("请依次完成题目 1～7，然后取消 run_checks() 的注释。")

    run_checks()
