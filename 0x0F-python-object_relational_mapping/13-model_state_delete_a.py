#!/usr/bin/python3
"""
Display the first state in states.id
    You are not allowed to fetch all states from the database
    before displaying the result
"""

import sys
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To update a value
from sqlalchemy import update

Base = declarative_base()


class States(Base):
    """
    Represent a state in 'states' table
    """
    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)


def main():
    """
    The main func to fetch and display all states in database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(States
                                     ).filter(States.name.contains('a')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    result = session.query(States).all()

    if not result:
        print("Not found")
    else:
        for i, state in enumerate(result, start=1):
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
