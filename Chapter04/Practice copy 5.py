import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT c.CompanyName,
       (SELECT COUNT(*)
        FROM Orders AS o
        WHERE o.CustomerID = c.CustomerID) AS OrderCount
FROM Customers AS c;

""", conn
)

print(df)
