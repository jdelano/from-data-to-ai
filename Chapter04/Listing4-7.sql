SELECT o.OrderID, c.CompanyName, s.CompanyName AS 
	ShipperName
FROM Orders AS o
	INNER JOIN Customers AS c 
		ON o.CustomerID = c.CustomerID
	INNER JOIN Shippers AS s 
		ON o.ShipVia = s.ShipperID;