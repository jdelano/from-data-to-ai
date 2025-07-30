import pandas as pd

employees = pd.DataFrame({
    "name": ["Alice", "Bob", "Carlos", "Diana"],
    "sales": [12000, 8500, 6000, 15000],
    "hours": [160, 120, 80, 200]
})

# Calculate sales per hour
employees["sales_per_hour"] = employees["sales"] / employees["hours"]
print(employees)
