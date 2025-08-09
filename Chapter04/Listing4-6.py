import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter04/northwind.db")

df = pd.read_sql("""
    SELECT t.TerritoryDescription, et.EmployeeID
    FROM EmployeeTerritories AS et
        RIGHT JOIN Territories AS t
            ON et.TerritoryID = t.TerritoryID;
    """, conn
)

print(df)