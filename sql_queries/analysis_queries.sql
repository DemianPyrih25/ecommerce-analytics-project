SELECT Country, SUM(Quantity * UniPrice) AS TotalSales
FROM sales_data
GROUP BY Country
ORDER BY TotalSales DESC
LIMIT 10;


SELECT StovkCode, Description, SUM(Quantity * UniPrice) AS TotalRevenue, COUNT(*) AS NumberOfransTactions
FROM sales_data
GROUP BY StockCode, Description
ORDER BY TotalRevenue Description
LIMIT 10;


SELECT MONTH(InvoiceDate) AS Month, YEAR(InvoiceDate) AS Year, SUM(Quantity * UniPrice) AS MonthlySales
FROM sales_data
GROUP BY YEAR(InvoiceDate), MONTH(InvoiceDate)
ORDER BY Year, Month;


SELECT Customer ID, Country, SUM(Quantity * UniPrice) As TotalSpent, COUNT(DISTINCT InvoiceNo) AS NumberOfPurchases
FROM sales_data
GROUP BY Customer ID, Country
ORDER BY TotalSpent DESC
LIMIT 10;

SELECT
    COUNT(*) AS TotalRecords,
    COUNT(DISTINCT Customer ID) AS UniqueCustomers,
    COUNT(DISTINCT InvoiceNo) AS UniqueInvoices,
    COUNT(DISTINCT StockCode) AS UniqueProducts,
    COUNT(DISTINCT Country) AS UniqueCountries,
    MIN(InvoiceDate) AS FirstSaleDate,
    MAX(InvoiceDate) AS LastSaleDate,
    MIN(UniPrice) AS MinPrice,
    MAX(UniPrice) AS MaxPrise, 
    AVG(Quantity) AS AvgQuantity
FROM sales_data;


SELECT Customer ID, Country, MAX(InvoiceDate) AS LastPurchaseDate, DATEDIFF(DAY, MAX(InvoiceDate), '2011-12-09') AS DaysSinceLastPurchase
FROM sales_data
GROUP BY Customer ID, Country
HAVING DATEDIFF(DAY, MAX(InvoiceDate), '2011-12-09') > 90
ORDER BY DaysSinceLastPurchase DESC;


