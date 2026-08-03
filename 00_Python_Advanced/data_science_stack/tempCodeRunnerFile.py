    assert cleaned["unit_price"].notna().all()
    assert cleaned["quantity"].notna().all()
    assert (cleaned["unit_price"] > 0).all()
    assert (cleaned["quantity"] > 0).all()
    assert "sales_amount" in cleaned.columns