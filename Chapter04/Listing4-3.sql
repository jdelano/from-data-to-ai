SELECT p.ProductName, c.CategoryName
FROM Categories AS c
	INNER JOIN Products AS p
		ON c.CategoryID = p.CategoryID;