#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///dogs.db', echo=True)


Session = sessionmaker(bind=engine)


session = Session()


Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())


Base.metadata.create_all(engine)
