#!/usr/bin/python3
"""
Write a python file that
contains the class definition
of a City and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class City(Base):
    """
    define a City class that
    connects to the mysql cities table
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
