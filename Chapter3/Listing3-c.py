import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
                 SELECT OrderID, CustomerID, OrderDate
                 FROM Orders
                 WHERE (ShipCountry = 'USA' OR ShipCountry = 'Canada')
                    AND OrderDate >= '2022-10-01' AND OrderDate <= '2022-12-31';
                 """, conn
)

print(df)