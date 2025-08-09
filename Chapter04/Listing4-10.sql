SELECT c.CompanyName,
	SUM(od.UnitPrice * od.Quantity) AS TotalSales
FROM Customers AS c
	INNER JOIN Orders AS o
		ON c.CustomerID = o.CustomerID
	INNER JOIN [Order Details] AS od
		ON o.OrderID = od.OrderID
GROUP BY c.CompanyName;