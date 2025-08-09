import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT p.ProductName
    FROM Products AS p
    WHERE p.ProductID NOT IN (
        SELECT od.ProductID 
        FROM [Order Details] AS od
    );
    """, conn
)

print(df)