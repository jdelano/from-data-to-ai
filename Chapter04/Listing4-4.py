import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT o.OrderID, c.CompanyName
    FROM Orders AS o
        INNER JOIN Customers AS c
            ON o.CustomerID = c.CustomerID;
    """, conn
)

print(df)