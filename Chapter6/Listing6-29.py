import pandas as pd
# Sample survey data with obvious problems
survey = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6],
    "age": [19, 22, 8, 20, 150, 21],
    "study_hours": [25, 35, 200, 15, -10, 40],
    "satisfy": [4, 5, 15, 3, 2, 1]
})

# Fix study hours over 168 (probably meant per month)
survey["study_hours"] = survey["study_hours"].apply(
    lambda hours: hours / 4 if hours > 168 else (abs(hours) if hours < 0 else hours)
)

# Cap satisfy ratings at valid scale limits
survey["satisfy"] = survey["satisfy"].clip(lower=1, upper=5)

# Cap ages at reasonable college student range
survey["age"] = survey["age"].clip(lower=16, upper=100)

print("After fixing obvious errors:")
print(survey)