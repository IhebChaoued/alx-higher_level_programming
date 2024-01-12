#!/usr/bin/python3


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            username=sys.arg[1],
            password=sys.arg[2],
            db=sys.arg[3],
            host="localhost",
            port=3306
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
