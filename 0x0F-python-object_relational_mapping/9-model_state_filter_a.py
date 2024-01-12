#!/usr/bin/python3
"""Script to list all State objects containing the letter 'a' from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Main execution block"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id)
              .all())

        print("{}: {}".format(state.id, state.name))

    session.close()
