import pandas as pd

# Sample student data with some quality issues
students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [19, 22, 150, 20, -5],
    "GPA": [3.8, 3.2, 4.0, 1.9, 2.1]
})

# Find students with normal ages AND high GPAs
normal_high_achievers = (students["Age"] >= 16) & (students["Age"] <= 100) & (students["GPA"] > 3.5)