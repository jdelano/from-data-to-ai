SELECT c.CompanyName
FROM Customers AS c
WHERE (SELECT COUNT(*)
	FROM Orders AS o 
	WHERE o.CustomerID = c.CustomerID) > 5;