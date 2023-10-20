SELECT custID,orderDate, upc,
unitsaleprice * quantity AS subtotal,
FROM orderlines;