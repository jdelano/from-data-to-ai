import pandas as pd

revenue = pd.DataFrame({
    "company": ["TechCo", "RetailMart", "ServicePro"],
    "revenue": [1500000, 750000, 2300000]  # in dollars
})

revenue["revenue_millions"] = revenue["revenue"] / 1_000_000
print(revenue)
