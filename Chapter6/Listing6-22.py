import pandas as pd

# Survey data with missing study hours by class level
study_data = pd.DataFrame({
    "student": ["Al", "Bob", "Chuck", "Dan", "Eve", "Fred"],
    "class": ["FR", "JR", "JR", "FR", "JR", "SO"],
    "study": [15, None, 25, None, 30, 20]
})

# Fill missing study hours with mean for each class level

class_grouping = study_data.groupby("class")
study_data["study"] = class_grouping["study"].transform(
    lambda hours: hours.fillna(hours.mean())
)

print("After group-based imputation:")
print(study_data)
