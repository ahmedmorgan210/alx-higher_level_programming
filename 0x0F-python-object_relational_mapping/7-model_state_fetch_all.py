#!/usr/bin/python3

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

class State(Base):
    """defining the states table"""
    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)


# engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
#                         .format(sys.argv[1], sys.argv[2], sys.argv[3]),
#                         pool_pre_ping=True)


# Session = sessionmaker()
# session = Session()
result = session.query(State).order_by(State.id).all()

for sort, state in enumerate(result, start = 1):
    print(f"{sort}: {state.name}")

if __name__ == "__main__":
    # engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
    #                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
    #                        pool_pre_ping=True)
    Base.metadata.create_all(engine)