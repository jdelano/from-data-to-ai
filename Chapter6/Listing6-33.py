import pandas as pd
# Sample survey data with obvious problems
survey = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "age": [19, 22, 8, 20, 150, 21],
    "study": [25, 35, 200, 15, -10, 40],
    "satisfy": [4, 5, 15, 3, 2, 1]
})

# Create indicator columns for outliers
survey["age_out"] = (survey["age"] < 16) | (survey["age"] > 100)
survey["hours_out"] = (survey["study"] < 0) | (survey["study"] > 168)
survey["satisfy_out"] = (survey["satisfy"] < 1) | (survey["satisfy"] > 5)

# Now correct the outlier values
survey["age"] = survey["age"].clip(lower=16, upper=100)
survey["study"] = survey["study"].clip(lower=0, upper=168)
survey["satisfy"] = survey["satisfy"].clip(lower=1, upper=5)

print("Data with outlier indicators:")
print(survey)