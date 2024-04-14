"""
This module demonstrates how to use SQLAlchemy to fetch and display all states from a MySQL database.

Usage:
    python3 7-model_state_fetch_all.py <username> <password> <database_name>

This script connects to a MySQL database using the provided username, password, and database name. It then queries the 'states' table, sorts the results by the state name in ascending order, and prints each state name along with its corresponding number in the sorted list.

The script uses SQLAlchemy, a popular SQL toolkit and Object-Relational Mapping (ORM) system for Python, to abstract the database operations. It defines a `State` class that maps to the 'states' table in the database, and uses a session to query the database.

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
    id = Column("id", Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)

def main():
    """
    Main function to fetch and display all states from the database.

    This function creates a SQLAlchemy engine and session, queries the 'states' table, sorts the results by the state name, and prints each state name along with its corresponding number in the sorted list.
    """
    if len(sys.argv) < 4:
        print("Usage: python3 7-model_state_fetch_all.py <username> <password> <database_name>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.name).all()

    for i, state in enumerate(result, start=1):
        print(f"{i}: {state.name}")

if __name__ == "__main__":
    main()