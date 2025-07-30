import pandas as pd

# Sample student data for string operations
students = pd.DataFrame({
    "Name": ["alice johnson", "BOB SMITH"],
    "Email": ["ALICE@SCHOOL.EDU", "Bob@School.Edu"],
    "Major": ["Computer Science", "Computer Science"]
})

# Create formatted display names
students["Name"] = students["Name"].str.title()
# Standardize email format
students["Email"] = students["Email"].str.lower()
# Create major abbreviations
students["Major_Code"] = students["Major"].str.replace("Computer Science", "CS")

print("Students with formatted information:")
print(students)