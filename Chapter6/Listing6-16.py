import pandas as pd

# Sample survey data with missing values and placeholders
survey = pd.DataFrame({
    "ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Satisfaction": [4, 5, None, 3, "", "N/A"],
    "study_hours": [20, None, 15, 25, 18, "Null"],
    "income": ["Low", "Medium", None, "", "High", "Medium"]
})

# Convert placeholder values to proper missing values
survey = survey.replace(["", "N/A", "Null"], pd.NA)

# Get comprehensive overview of missing values
print("Missing value summary:")
print(survey.isnull().sum())

# Find rows with any missing values
missing_rows = survey.isnull().any(axis=1)
print(f"Rows with missing data: {missing_rows.sum()}")