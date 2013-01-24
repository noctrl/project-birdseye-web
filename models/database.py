__author__ = 'mjholler'

from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://birdseye:password@localhost/birdseye')
meta = MetaData(bind=engine, reflect=True)

