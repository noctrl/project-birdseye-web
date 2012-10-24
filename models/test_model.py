__author__ = 'mjholler'

from sqlalchemy.ext.declarative import delcarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Boolean

# Classes and tables relative to Base
Base = delcarative_base() # Declaring the base

class Lots(Base):
    __tablename__ = 'lots'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    total_spaces = Column(Integer)
    available_spaces = Column(Integer)
    active = Column(Boolean)

    def __init__(self, name, location, total_spaces, available_spaces, active):
        self.active = name
        self.location = location
        self.available_spaces = available_spaces
        self.total_spaces = total_spaces
        self.active = active





