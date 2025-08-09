import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT CustomerID, COUNT(*) AS OrderCount
    FROM Orders
    GROUP BY CustomerID
    HAVING COUNT(*) >= 5;
    """, conn
)

print(df)