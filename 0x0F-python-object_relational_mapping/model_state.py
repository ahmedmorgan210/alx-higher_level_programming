#!/usr/bin/python3
"""
start link class to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#from model_state import Base, State


session = sessionmaker()

Base = declarative_base()


class State(Base):
    """defining the states table"""
    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column("name",String(128), nullable=False)
