#!/usr/bin/python3
"""
python script
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states\
                   WHERE name = %s\
                   ORDER BY id ASC;', ('{}'.format(argv[4]),))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
