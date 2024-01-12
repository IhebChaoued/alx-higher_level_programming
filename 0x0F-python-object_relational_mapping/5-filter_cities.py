#!/usr/bin/python3
"""Script to list cities from a MySQL database based on a state"""
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
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
