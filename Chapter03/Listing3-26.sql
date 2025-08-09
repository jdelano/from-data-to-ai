-- Less efficient: filters after grouping
SELECT Country, AVG(UnitPrice)
FROM Products
GROUP BY Country
HAVING Country = 'USA';

-- Better: filters before grouping
SELECT Country, AVG(UnitPrice)
FROM Products
WHERE Country = 'USA'
GROUP BY Country;