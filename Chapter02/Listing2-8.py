import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table"
response = requests.get(url)
tables = pd.read_html(response.text)

# Get the medal table
medal_df = tables[3]  # The main Olympics medal table

# Take a quick look at what we got
print(medal_df.head())
print(medal_df.info())

# Save to CSV
medal_df.to_csv("data/raw/olympics_medals_2024.csv", index=False)

