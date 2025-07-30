import pandas as pd
df = pd.read_excel("students.xlsx", sheet_name="Sheet1")
print(df.head())  # Displays the first few rows of the DataFrame