import pandas as pd

orders = pd.DataFrame({
    "date": pd.to_datetime(["2024-01-15", "2024-01-16", 
                            "2024-06-30", "2024-07-04", 
                            "2024-12-25"]),
    "amount": [50, 125, 75, 200, 450]
})

orders["month"] = orders["date"].dt.month
orders["day_name"] = orders["date"].dt.day_name()
orders["quarter"] = orders["date"].dt.quarter
print(orders)