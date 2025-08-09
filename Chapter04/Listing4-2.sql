SELECT Products.ProductName, Categories.CategoryName
FROM Categories
	INNER JOIN Products
		ON Categories.CategoryID = Products.CategoryID;