import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT p.ProductName
    FROM Products AS p
    WHERE NOT EXISTS (
        SELECT 1 
        FROM [Order Details] AS od
        WHERE od.ProductID = p.ProductID
    );
    """, conn
)

print(df)