import pandas as pd

# Create data frames with overlapping column names
emp = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Cathy"],
    "dept": [10, 20, 30],
    "manager": ["Yes", "No", "No"]  # This column will conflict
})

dept = pd.DataFrame({
    "dept_code": [10, 20, 30, 40],
    "dept_name": ["Sales", "Engineering", "HR", "Finance"],
    "manager": ["John", "Sarah", "Mike", "Lisa"]  # Same column name!
})

# Merge with different key names
print("=== Merge with different key names ===")
result1 = pd.merge(emp, dept, 
                   left_on="dept", 
                   right_on="dept_code", 
                   how="left")
print(result1)

# Merge with custom suffixes for conflicting columns
print("=== Merge with custom suffixes ===")
result2 = pd.merge(emp, dept,
                   left_on="dept",
                   right_on="dept_code",
                   how="left",
                   suffixes=("_emp", "_dept"))
print(result2)

# Use indicator to track merge results
print("=== Merge with Indicator ===")
result3 = pd.merge(emp, dept,
                   left_on="dept",
                   right_on="dept_code",
                   how="outer",
                   indicator=True)
print(result3)
print("Merge summary:")
print(result3["_merge"].value_counts())