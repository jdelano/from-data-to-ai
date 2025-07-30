import pandas as pd
# Wide format data
students_wide = pd.DataFrame({
    "student_id": [101, 102, 103],
    "name": ["Alice", "Bob", "Cathy"],
    "math": [85, 78, 92],
    "science": [92, 85, 88],
    "english": [88, 90, 85]
})

print("=== Wide format ===")
print(students_wide)

# Convert to long format
students_long = students_wide.melt(
    id_vars=["student_id", "name"],  # Columns to keep as identifiers
    var_name="subject",               # Name for the new "variable" column
    value_name="score"                # Name for the new "value" column
)

print("=== Long format ===")
print(students_long)