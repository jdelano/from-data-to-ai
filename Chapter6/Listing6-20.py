import pandas as pd

# Sample survey data with missing values and placeholders
survey = pd.DataFrame({
    "student_id": [1001, 1002, 1003, 1004, 1005],
    "satisfaction": [4, 5, None, 3, None],
    "income": ["Low", "Medium", None, "Medium", "High"],
    "comments": [None, "Awesome!", "Meh", None, "Great!"]
})

# Simple imputation with summary statistics
# Fill numeric columns with median
survey["satisfaction"] = survey["satisfaction"].fillna(
    survey["satisfaction"].median()
)

# Fill categorical columns with mode (most common value)
income_mode = survey["income"].mode()
survey["income"] = survey["income"].fillna(income_mode[0])

# Fill with meaningful placeholder
survey["comments"] = survey["comments"].fillna("No Comment")

print(survey)
