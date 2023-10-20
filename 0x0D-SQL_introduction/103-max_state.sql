SELECT custID,orderplace, upc,
unitsaleprice * quantity  AS subtotal
FROM orederlines;