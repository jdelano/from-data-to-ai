import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT p.ProductName, c.CategoryName
FROM Products AS p
INNER JOIN Categories AS c
		ON p.CategoryID = c.CategoryID;
""", conn
)

print(df)
