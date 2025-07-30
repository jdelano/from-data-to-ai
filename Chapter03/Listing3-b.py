import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
                 SELECT CustomerID, CompanyName
                 FROM Customers
                 WHERE Country <> 'USA'
                 LIMIT 5;
                 """, conn
)

print(df)