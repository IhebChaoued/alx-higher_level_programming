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

    cursor.execute("SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s", (sys.argv[4],))

    result = cursor.fetchone()

    print(result[0])

    cursor.close()
    db.close()
