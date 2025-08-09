import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT ProductName 
    FROM Products
    ORDER BY UnitPrice DESC;
    """, conn
)

print(df)