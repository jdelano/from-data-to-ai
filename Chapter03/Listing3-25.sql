-- WRONG: Can't use COUNT in WHERE
SELECT CustomerID, COUNT(*) AS OrderCount
FROM Orders
WHERE COUNT(*) > 5
GROUP BY CustomerID;

-- CORRECT: Use HAVING for aggregate conditions
SELECT CustomerID, COUNT(*) AS OrderCount
FROM Orders
GROUP BY CustomerID
HAVING COUNT(*) > 5;