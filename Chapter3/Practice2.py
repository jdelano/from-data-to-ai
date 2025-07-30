import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
                 SELECT COUNT(OrderDate) AS NumberOfOrders,
                    strftime('%Y', OrderDate), strftime('%m', OrderDate)
                 FROM Orders 
                 GROUP BY strftime('%Y-%m', OrderDate)
                 """, conn
)

print(df)