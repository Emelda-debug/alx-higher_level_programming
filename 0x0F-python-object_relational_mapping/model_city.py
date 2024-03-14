#!/usr/bin/python3
""" python file that contains the class definition of a City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ inherits from Base (imported from model_state),
    links to the MySQL table cities
    has class attribute id that represents a column of an auto-generated primary key
    has class attribute name that represents a column of a
    string of 128 characters and can’t be null
    has class attribute state_id that represents a column of an integer
    that can’t be null and is a foreign key to states.id
    """
     __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
