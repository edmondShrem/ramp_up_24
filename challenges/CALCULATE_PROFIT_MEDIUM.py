def profit(d:dict):
    return round((d.get("sell_price") - d.get("cost_price")) * d.get("inventory"), 2)

