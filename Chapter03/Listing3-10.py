import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT ProductName, UnitPrice 
    FROM Products
    ORDER BY UnitPrice DESC
    LIMIT 5;
    """, conn
)

print(df)