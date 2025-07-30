import pandas as pd

# Sample student data with some quality issues
students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [19, 22, 150, 20, -5],
    "GPA": [3.8, 3.2, 4.0, 1.9, 2.1]
})

# Record academic status based on GPA
deans_list = students["GPA"] >= 3.5
students.loc[deans_list, "Academic Status"] = "Dean's List"

good = (students["GPA"] < 3.5) & (students["GPA"] >= 2.0)
students.loc[good, "Academic Status"] = "Good"

probation = students["GPA"] < 2.0
students.loc[probation, "Academic Status"] = "Probation"

print("Students with academic status:")
print(students)