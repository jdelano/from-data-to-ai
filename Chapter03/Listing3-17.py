import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT CategoryID, MIN(UnitPrice) AS Cheapest,
        MAX(UnitPrice) AS MostExpensive
    FROM Products
    GROUP BY CategoryID;
    """, conn
)

print(df)