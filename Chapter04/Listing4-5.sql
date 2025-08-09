SELECT t.TerritoryDescription, et.EmployeeID
FROM Territories AS t
	LEFT JOIN EmployeeTerritories AS et
		ON t.TerritoryID = et.TerritoryID;