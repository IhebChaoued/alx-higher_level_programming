#!/usr/bin/python3
"""Script to print the State object with the given name"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Main execution block"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = sys.argv[4]
    state = (session.query(State)
             .filter(State.name == state_name)
             .first())

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
