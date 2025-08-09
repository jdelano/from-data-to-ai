SELECT CustomerID, COUNT(*) AS OrderCount
FROM Orders
GROUP BY CustomerID;