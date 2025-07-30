import pandas as pd

# Sample survey data with missing values
survey = pd.DataFrame({
    "student_id": [1001, 1002, 1003, 1004, 1005],
    "satisfy": [4, 5, None, 3, None],
    "income": ["Low", "Medium", "Low", None, "High"]
})

# Step 1: Create indicator columns before filling anything
survey["no_satisfy"] = survey["satisfy"].isnull()
survey["no_income"] = survey["income"].isnull()

# Step 2: Fill the missing values
satisfy_med = survey["satisfy"].median()
survey["satisfy"] = survey["satisfy"].fillna(satisfy_med)

income_mode = survey["income"].mode()
survey["income"] = survey["income"].fillna(income_mode[0])

print("Data with missing indicators:")
print(survey)