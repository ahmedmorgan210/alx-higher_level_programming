#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city in the 'cities' table.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The identifier of the state the city belongs to.
    """

    __tablename__ = 'cities'
    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(
        'states.id'), nullable=False)
