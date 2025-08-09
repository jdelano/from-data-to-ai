SELECT c.CompanyName,
	(SELECT COUNT(*)
	FROM Orders AS o
	WHERE o.CustomerID = c.CustomerID) AS OrderCount
FROM Customers AS c;