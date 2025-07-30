import pandas as pd
# Example: nested JSON data
nested_data = {
    "team": "Data Science",
    "members": [
        {"name": "Alice", "role": "Analyst"},
        {"name": "Bob", "role": "Engineer"}
    ]
}

# Flatten into a DataFrame
df = pd.json_normalize(nested_data, "members", meta="team")
print(df)
