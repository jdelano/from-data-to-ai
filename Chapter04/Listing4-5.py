import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT t.TerritoryDescription, et.EmployeeID
    FROM Territories AS t
        LEFT JOIN EmployeeTerritories AS et
            ON t.TerritoryID = et.TerritoryID;
    """, conn
)

print(df)