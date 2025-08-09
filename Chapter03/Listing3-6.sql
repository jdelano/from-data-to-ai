SELECT CompanyName, City
FROM Customers 
WHERE (Country = 'USA' OR Country = 'UK') 
    AND PostalCode LIKE '9%';