-- Clear and semantic: counting discontinued products
SELECT CategoryID, COUNT(*) AS DiscontinuedProducts
FROM Products
WHERE Discontinued = 1
GROUP BY CategoryID;

-- Less clear: what does summing Discontinued mean?
SELECT CategoryID, SUM(Discontinued) AS
	DiscontinuedProducts
FROM Products
GROUP BY CategoryID;