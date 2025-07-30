import pandas as pd
# Sample grade data
grades = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie"],
    "Test": [85, 92, 78],
    "Curve": [5, 3, 7]
})

# Add curve points to test scores
grades["Final"] = grades["Test"] + grades["Curve"]

# Convert percentages to decimal (divide by 100)
grades["Percent"] = grades["Final"] / 100

print("Grades after calculations:")
print(grades)
