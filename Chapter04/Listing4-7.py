import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT o.OrderID, c.CompanyName, s.CompanyName AS 
        ShipperName
    FROM Orders AS o
        INNER JOIN Customers AS c 
            ON o.CustomerID = c.CustomerID
        INNER JOIN Shippers AS s 
            ON o.ShipVia = s.ShipperID;
    """, conn
)

print(df)