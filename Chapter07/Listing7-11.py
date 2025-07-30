import pandas as pd

response_times = pd.DataFrame({
    "customer": ["A", "B", "C", "D", "E", "F"],
    "minutes": [2, 5, 8, 15, 60, 120]
})

response_times["speed"] = 1 / response_times["minutes"]
print(response_times)