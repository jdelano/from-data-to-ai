SELECT p.ProductName,
	(SELECT s.CompanyName
	FROM Suppliers AS s
	WHERE s.SupplierID = p.SupplierID) AS SupplierName
FROM Products AS p;