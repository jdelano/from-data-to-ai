SELECT CategoryID, MIN(UnitPrice) AS Cheapest,
	MAX(UnitPrice) AS MostExpensive
FROM Products
GROUP BY CategoryID;