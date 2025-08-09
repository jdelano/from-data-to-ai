SELECT CategoryID, COUNT(*) AS ProductCount
FROM Products
GROUP BY CategoryID;