SELECT CategoryID, COUNT(*) AS ActiveProducts
FROM Products
WHERE Discontinued = 0
GROUP BY CategoryID
HAVING COUNT(*) > 5;