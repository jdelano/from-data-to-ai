import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT p.ProductName,
       (SELECT s.CompanyName 
        FROM Suppliers AS s
        WHERE s.SupplierID = p.SupplierID) AS SupplierName
FROM Products AS p;

""", conn
)

print(df)
