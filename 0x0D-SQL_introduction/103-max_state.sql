SELECT DISTNICT prodname, unotsaleprice
FROM PRODUCTS NATURAL JOIN orderlines
WHERE unitsaleprice = the average unot sale price