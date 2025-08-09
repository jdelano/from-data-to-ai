import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT c.CompanyName,
        (SELECT COUNT(*)
        FROM Orders AS o
        WHERE o.CustomerID = c.CustomerID) AS OrderCount
    FROM Customers AS c;
    """, conn
)

print(df)