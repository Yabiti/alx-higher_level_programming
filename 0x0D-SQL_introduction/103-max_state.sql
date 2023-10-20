SELECT DISTNICT prodname, unitsaleprice
FROM PRODUCTS NATURAL JOIN orderlines
WHERE unitsaleprice = the average unot sale price