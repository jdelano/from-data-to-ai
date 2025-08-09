SELECT o.OrderID, o.OrderDate, ic.TotalItems
FROM Orders AS o
	INNER JOIN (
		SELECT OrderID, SUM(Quantity) AS TotalItems
		FROM [Order Details]
		GROUP BY OrderID
	) AS ic
		ON o.OrderID = ic.OrderID;