import pandas as pd
# Starting with long format data
grades_long = pd.DataFrame({
    "student_id": [101, 101, 101, 102, 102, 102],
    "student_name": ["Alice", "Alice", "Alice", "Bob", "Bob", "Bob"],
    "test_type": ["midterm", "final", "project", "midterm", "final", "project"],
    "score": [85, 88, 92, 78, 82, 85]
})

print("Long format:")
print(grades_long)

# Convert to wide format
grades_wide = grades_long.pivot(
    index=["student_id", "student_name"],  # Columns that identify each row
    columns="test_type",                    # Values become column names
    values="score"                          # Values to fill the table
)

print("=== Wide format ===")
print(grades_wide)

# Flatten column names and reset index
grades_wide = grades_wide.reset_index()
print("=== Cleaned wide format ===")
print(grades_wide)