#!/usr/bin/python3
"""
This module demonstrates how to use SQLAlchemy to\
    fetch and display all states from a MySQL database.

"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the 'states' table.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """

    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)


def main():
    """
    Main function to fetch and display all states from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).all()

    for i, state in enumerate(result, start=1):
        print(f"{i}: {state.name}")


if __name__ == "__main__":
    main()
