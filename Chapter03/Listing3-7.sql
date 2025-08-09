SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE (ShipCountry = 'USA' OR ShipCountry = 'Canada')
	AND OrderDate >= '2022-10-01' 
	AND OrderDate <= '2022-12-31';