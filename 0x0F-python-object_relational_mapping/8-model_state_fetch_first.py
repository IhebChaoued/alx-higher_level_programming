#!/usr/bin/python3
"""Script to print the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Main execution block"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT * FROM states ORDER BY id ASC LIMIT 1"""
    cursor.execute(sql)
    state = cursor.fetchone()

    if state:
        print("1: {}".format(state[1]))
    else:
        print("Nothing")

    cursor.close()
    db.close()
