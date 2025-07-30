import pandas as pd
# Sample survey data with obvious problems
survey = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6],
    "study": [25, 35, 200, 15, -10, 40],
})

# Find obviously impossible values using domain knowledge
problems = survey[(survey["study"] < 0) | (survey["study"] > 168)]

print("Students with unrealistic study hours:")
print(problems)