import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT e.FirstName || ' ' || e.LastName AS EmployeeName,
       AVG(od.UnitPrice * od.Quantity) AS AvgLineItemValue
FROM Employees AS e
INNER JOIN Orders AS o 
    ON e.EmployeeID = o.EmployeeID
INNER JOIN [Order Details] AS od 
    ON o.OrderID = od.OrderID
GROUP BY e.EmployeeID, e.FirstName, e.LastName;

""", conn
)

print(df)
