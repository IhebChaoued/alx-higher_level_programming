#!/usr/bin/python3
"""Script to list states from a MySQL database"""
import sys
import MySQLdb


if __name__ == "__main__":
    """Main execution block"""
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    cursor = db.cursor()

    query = """
    SELECT * FROM states WHERE name = %s ORDER BY id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
