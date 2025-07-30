import pandas as pd

revenue = pd.DataFrame({
    "year": [2022, 2023, 2024],
    "sales": [100, 120, 110]  # in thousands
})

revenue["change"] = revenue["sales"].diff()
revenue["pct_change"] = revenue["sales"].pct_change() * 100
print(revenue)