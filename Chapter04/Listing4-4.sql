SELECT o.OrderID, c.CompanyName
FROM Orders AS o
	INNER JOIN Customers AS c
		ON o.CustomerID = c.CustomerID;