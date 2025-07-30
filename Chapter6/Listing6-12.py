import pandas as pd
# Sample student data
students = pd.DataFrame({
    "Name": ["alice", "bob", "charlie", "diana"],
    "Test": [85, 92, 78, 96],
    "Participation": [8, 9, 7, 10]
})

# Apply simple transformations
students["Name"] = students["Name"].apply(
    lambda name: name.title()
)
students["Curved"] = students["Test"].apply(
    lambda test: test + 5
)
students["Total"] = students.apply(
    lambda row: row["Test"] + row["Participation"],
    axis=1
)
print("After applying lambda functions:")
print(students)