import pandas as pd

scores = pd.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "Diana"],
    "score": [45, 80, 75, 90]
})

min_val = scores["score"].min()
max_val = scores["score"].max()
scores["scaled"] = (scores["score"] - min_val) / (max_val - min_val)

print(scores)