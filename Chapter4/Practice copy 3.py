import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT e.FirstName || ' ' || e.LastName AS EmployeeName, AVG(ov.TotalOrderValue) AS AvgOrderValue
FROM Employees AS e
	INNER JOIN Orders AS o
 		ON e.EmployeeID = o.EmployeeID
    INNER JOIN (
			SELECT OrderID,	SUM(UnitPrice * Quantity) AS TotalOrderValue
			FROM [Order Details]
			GROUP BY OrderID
   		) AS ov
		ON o.OrderID = ov.OrderID
GROUP BY e.EmployeeID, e.FirstName, e.LastName;
""", conn
)

print(df)
