# 样例数据说明

这些 CSV 均为学习用途的虚构数据，不包含真实订单或个人信息。

## ecommerce_sales_raw.csv

| 字段 | 含义 |
| --- | --- |
| order_id | 订单编号 |
| order_date | 下单日期 |
| category | 商品品类 |
| product | 商品名称 |
| unit_price | 单价 |
| quantity | 数量 |
| region | 区域 |
| payment_method | 支付方式 |

原始数据特意包含一条重复订单、一项缺失单价和一项缺失品类。

## ecommerce_sales_clean.csv

按照 `02_pandas_basics.py` 中的规则清洗后的预期结果，新增
`sales_amount = unit_price * quantity`。它同时作为可视化模块的稳定输入。

## category_info.csv

商品品类维表，用于练习按照 `category` 进行左连接。
