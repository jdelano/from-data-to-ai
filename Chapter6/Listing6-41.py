import pandas as pd
# Sample data with mixed and problematic date formats
events = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8],
    "date": ["2023-01-15", "01/15/2023", "January 15, 2023", "15-Jan-2023", 
                   "2023.01.15", "1/15/23", "invalid date", "2023-02-30"],
    "status": ["valid", "valid", "valid", "valid", "valid", "valid", "invalid", "impossible"]
})

events["date_clean"] = events["date"].apply(
    lambda date: pd.to_datetime(date, errors="coerce")
)

print("After date standardization:")
print(events)

# Check the data type and count problems
print("Data type of cleaned dates:", events["date_clean"].dtype)
invalid_dates = events["date_clean"].isnull().sum()
print(f"Number of invalid dates: {invalid_dates}")