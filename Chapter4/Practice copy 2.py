import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT c.CompanyName,
		SUM(od.UnitPrice * od.Quantity) AS TotalSales
FROM Customers AS c
		INNER JOIN Orders AS o
			ON c.CustomerID = o.CustomerID
		INNER JOIN [Order Details] AS od
			ON o.OrderID = od.OrderID
GROUP BY c.CompanyName;

""", conn
)

print(df)
