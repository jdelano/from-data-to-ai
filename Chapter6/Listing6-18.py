import pandas as pd

# Sample survey data with missing values
survey = pd.DataFrame({
    "student_id": [1001, 1002, 1003, 1004, 1005],
    "satisfaction": [4, 5, None, 3, None],
    "study": [20, None, 15, 25, 18],
    "income_range": ["Low", "Medium", None, None, "High"]
})

# Drop rows missing critical survey questions
survey = survey.dropna(subset=["satisfaction", "study"])

# If you decide a column isn't useful, remove it by name
survey = survey.drop(columns=["income_range"])
print(survey)