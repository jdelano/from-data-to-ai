SELECT od.OrderID, o.OrderDate, p.ProductName,
	c.CompanyName
FROM [Order Details] AS od
	INNER JOIN Orders AS o 
		ON od.OrderID = o.OrderID
	INNER JOIN Products AS p 
		ON od.ProductID = p.ProductID
	INNER JOIN Customers AS c 
		ON o.CustomerID = c.CustomerID;