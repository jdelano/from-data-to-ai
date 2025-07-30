import pandas as pd
# Sample survey data with obvious problems
survey = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6],
    "age": [19, 22, 8, 20, 150, 21],
    "study": [25, 35, 200, 15, -10, 40],
    "satisfy": [4, 5, 15, 3, 2, 1]
})

# Remove rows with impossible values
clean_survey = survey[
    (survey["age"] >= 16) & (survey["age"] <= 100) &
    (survey["study"] >= 0) & (survey["study"] <= 168) &
    (survey["satisfy"] >= 1) & (survey["satisfy"] <= 5)
]

print("Clean data:")
print(clean_survey)