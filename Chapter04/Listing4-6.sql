SELECT t.TerritoryDescription, et.EmployeeID
FROM EmployeeTerritories AS et
	RIGHT JOIN Territories AS t
		ON et.TerritoryID = t.TerritoryID;