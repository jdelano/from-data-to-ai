SELECT o.OrderID, c.CompanyName, s.CompanyName AS
	ShipperName
FROM Orders AS o
	-- Join customers to get company names
	INNER JOIN Customers AS c 
		ON o.CustomerID = c.CustomerID
	-- Join shippers to get shipping company
	INNER JOIN Shippers AS s 
		ON o.ShipVia = s.ShipperID
WHERE o.OrderDate >= '1996-07-01';