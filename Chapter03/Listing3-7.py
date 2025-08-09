import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT OrderID, CustomerID, OrderDate
    FROM Orders
    WHERE (ShipCountry = 'USA' OR ShipCountry = 'Canada')
        AND OrderDate >= '2022-10-01' 
        AND OrderDate <= '2022-12-31';
    """, conn
)

print(df)