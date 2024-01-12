#!/usr/bin/python3
"""Script to delete State objects with a name containing 'a'"""
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

    states_to_delete = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
            )

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    print("{} states deleted successfully".format(len(states_to_delete)))

    session.close()
