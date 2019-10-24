#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy import Column, Integer, String # type: ignore

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    room_id = Column(Integer, primary_key=True)
    title =  Column(String(200), nullable=False)
    n_to = Column(Integer, nullable=True)
    s_to = Column(Integer, nullable=True)
    w_to = Column(Integer, nullable=True)
    e_to = Column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"{self.room_id}: {self.title}"
