import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT Products.ProductName, Categories.CategoryName
    FROM Categories
        INNER JOIN Products
            ON Categories.CategoryID = Products.CategoryID;
    """, conn
)

print(df)