#!/usr/bin/python3
"""
Display the first state in states.id
    You are not allowed to fetch all states from the database
    before displaying the result
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """
    Main function to fetch and display all City objects from the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State, City.state_id == State.id
                                      ).order_by(City.id).all()

    for city in cities:
        print(f"{city.State.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    main()
