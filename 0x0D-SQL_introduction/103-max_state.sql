SELECT custID, orderDate, SUM(unitsaleprice * quantity) AS total
FROM orderlines
GROUP BY custID, orderdate