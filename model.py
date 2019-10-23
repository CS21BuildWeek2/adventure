#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy import Column, Integer, String # type: ignore

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    title =  Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    elevation = Column(Integer, nullable=False)
    terrain = Column(String(100))
    n_to = Column(Integer, nullable=True)
    s_to = Column(Integer, nullable=True)
    w_to = Column(Integer, nullable=True)
    e_to = Column(Integer, nullable=True)
