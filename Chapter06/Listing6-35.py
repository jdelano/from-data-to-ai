import pandas as pd

# Sample data with common text formatting problems
students = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "first_name": [" Al ", "bob", "CHUCK", "dan ", "Eve"],
    "last_name": ["brown ", " LEE", "Smith", "Wilson", " JONES "],
    "major": ["Math Ed", "math ed", "MATH ED", "Biology", "biology "],
    "email": ["AB@U.EDU", "bl@u.edu", "cs@U.edu", "dw@u.EDU", "ej@u.edu"]
})

# Remove extra whitespace and standardize case
students["first_name"] = students["first_name"].str.strip().str.title()
students["last_name"] = students["last_name"].str.strip().str.title()
students["major"] = students["major"].str.strip().str.title()
students["email"] = students["email"].str.lower()

print("After cleaning whitespace and case:")
print(students)