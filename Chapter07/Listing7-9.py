import pandas as pd

students = pd.DataFrame({
    "age": [18, 19, 20, 20, 21, 22, 23, 25, 28, 35, 42, 55]
})

# Equal-width bins (width of 10 years)
students["age_decade"] = pd.cut(students["age"],
    bins=[10, 20, 30, 40, 50, 60]
)

# Equal-frequency bins (4 quartiles)
students["age_quartile"] = pd.qcut(students["age"], q=4)

print(students)