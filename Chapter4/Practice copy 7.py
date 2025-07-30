import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT t.TerritoryDescription, et.EmployeeID
FROM Territories AS t
		LEFT JOIN EmployeeTerritories AS et
			ON t.TerritoryID = et.TerritoryID;

""", conn
)
import numpy as np
#print(df)
#print(df.isna().sum())  # Check for null values in the DataFrame
df.replace(float("nan"), 0, inplace=True)  # Replace NA with None
print(df)
print(df.isna().sum())  # Check for null values in the DataFrame
