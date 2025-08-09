import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT p.ProductName,
        (SELECT s.CompanyName
        FROM Suppliers AS s
        WHERE s.SupplierID = p.SupplierID) AS SupplierName
    FROM Products AS p;
    """, conn
)

print(df)