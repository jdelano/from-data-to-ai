import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT p.ProductName, c.CategoryName
    FROM Categories AS c
        INNER JOIN Products AS p
            ON c.CategoryID = p.CategoryID;
    """, conn
)

print(df)