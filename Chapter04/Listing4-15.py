import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT o.OrderID, o.OrderDate, ic.TotalItems
    FROM Orders AS o
        INNER JOIN (
            SELECT OrderID, SUM(Quantity) AS TotalItems
            FROM [Order Details]
            GROUP BY OrderID
        ) AS ic
            ON o.OrderID = ic.OrderID;
    """, conn
)

print(df)