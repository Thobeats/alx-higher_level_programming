#!/usr/bin/python3
"""
Write a python file that
contains the class definition
of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from relationship_city import City, Base


class State(Base):
    """
    define a State class that
    connects to the mysql states table
    """
    __tablename__ = "states"
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
