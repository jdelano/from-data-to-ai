import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT CategoryID, COUNT(*) AS ActiveProducts
    FROM Products
    WHERE Discontinued = 0
    GROUP BY CategoryID
    HAVING COUNT(*) > 5;
    """, conn
)

print(df)