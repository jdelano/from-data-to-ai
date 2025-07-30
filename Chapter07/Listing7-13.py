import pandas as pd

participation = pd.DataFrame({
    "student": ["Ana", "Ben", "Carlos", "Diana", "Emma", 
                "Frank"],
    "score": [2, 3, 7, 8, 9, 10]
})

participation["score_sq"] = participation["score"] ** 2
print(participation)