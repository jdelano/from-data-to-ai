import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    SELECT EmployeeID 
    FROM Employees 
    WHERE BirthDate IS NULL;
    """, conn
)

print(df)