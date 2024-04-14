#!/usr/bin/python3
"""
start link class to table in database
"""
import sys
from sqlalchemy import create_engine, column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'
        id = column(Integer, autoincrement=True, nullable=False)
        name = column(String(128), nullable=False)

    Base.metadata.create_all(engine)
