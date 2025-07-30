import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("northwind.db")

# Select just the ID and name from the first 5 customers
df = pd.read_sql("""
SELECT e.FirstName || ' ' || e.LastName AS EmployeeName,
       (SELECT AVG(OrderTotal.Total)
        FROM (SELECT o.OrderID, SUM(od.UnitPrice * od.Quantity) AS Total
              FROM Orders o
              INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
              WHERE o.EmployeeID = e.EmployeeID
              GROUP BY o.OrderID) AS OrderTotal) AS AvgOrderValue
FROM Employees e;

""", conn
)

print(df)
