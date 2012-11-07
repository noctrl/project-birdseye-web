__author__ = 'mjholler'

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import delcarative_base
from sqlalchemy.types import Boolean, DateTime
from sqlalchemy.orm import relationship, backref

# Classes and tables relative to Base
engine = create_engine('')
Base = delcarative_base() # Declaring the base

"""
TODO:
    - Determine TimeZone
    - DateTime.now()?



"""
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    salt = Column(String) # Type?
    #group_id
    #api_key
    #api_secret
    created = Column(DateTime)
    #first_login
    #last_login
    
    def __init__(self, username, password, salt):
        self.username = username
        self.password = password
        self.salt = salt

class Lot(Base):
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

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    created = Column(DateTime)
    active = Column(Boolean)
    #api_key
    #api_secret

    # Many-to-one
    lot_id = Column(Integer, ForeignKey('lot.id'))
    lot = relationship("Lot", backref=backref("lots", order_by=id))

    def __init__(self, name, location, created, active):
        self.name = name
        self.location = location
        self.created = created
        self.active = active

class SensorLog(Base):
    __tablename__ = 'sensor_log'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    
    # One-to-one
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    sensor = relationship("Sensor", uselist=False, backref=backref("sensor_log", uselist=False))

    # One-to-one
    lot_id = Column(Integer, ForeignKey("lots.id"))
    lot = relationship("Lot", uselist=False, backref=backref("lots", uselist=False))

    def __init__(self, created):
        self.created = created




# create tables

Base.metadeta.create_all(engine)        
    




