import pandas as pd
# Student data
df = pd.DataFrame({
    "student_id": [1001, 1002, 1003],
    "age": [18, 19, 150],
    "gpa": [3.5, 3.8, 4.2],
    "major": ["CS", "CS", "Biology"]
})

# Transformations
df["student_id_scaled"] = df["student_id"] / 1000
df["age"] = df["age"] / df["age"].max()  # Scale age
df["gpa_squared"] = df["gpa"] ** 2
df["age_scaled"] = df["age"] / 100  # Scale age again
major_codes = {"CS": 1, "Biology": 2, "Chemistry": 3}
df["major_code"] = df["major"].map(major_codes)
print(df)