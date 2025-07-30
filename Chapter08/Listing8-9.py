import pandas as pd

# Dataset 1 uses abbreviations
df1 = pd.DataFrame({
    "employee_id": [101, 102, 103, 104],
    "name": ["Alice", "Bob", "Cathy", "Dan"],
    "emp_status": ["FT", "PT", "FT", "CT"]  
})

# Dataset 2 uses full words
df2 = pd.DataFrame({
    "employee_id": [102, 103, 105, 106],
    "department": ["Sales", "Engineering", "Marketing", "HR"],
    "status": ["Part-time", "Full-time", "Full-time", "Contract"]
})

# Create mapping dictionary
status_mapping = {
    "FT": "Full-time",
    "PT": "Part-time",
    "CT": "Contract"
}

# Harmonize Dataset 1 to match Dataset 2"s format
df1["emp_status"] = df1["emp_status"].replace(status_mapping)

# Rename column for consistency
df1 = df1.rename(columns={"emp_status": "status"})

# Now we can merge successfully
merged = pd.merge(df1, df2, on=["employee_id", "status"], how="inner")
print("After harmonization:")
print(merged)
