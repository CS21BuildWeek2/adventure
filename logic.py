#!/usr/bin/env python
#
from typing import Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy import exists
from sqlalchemy.exc import OperationalError
from time import sleep
from api_funcs import (status, init, move_, take_)
from model import Room, Base
from settings import REVERSE

engine = create_engine('sqlite:///map.db')
Session = sessionmaker()
Base.metadata.create_all(engine, checkfirst=True)


def check_if_db() -> int:
    """ checks if the current room you're in is in the database.
    if not, adds it.
    to be helpful, returns current room id
    """
    sess = Session(bind=engine)
    i = init()
    sleep(1)
    room_ = sess.query(Room).filter(Room.room_id==i['room_id'])

    if not room_.all():
        room = Room(room_id=i['room_id'], title=i['title'])
        sess.add(room)

    sess.commit()
    return i['room_id'], i['exits']
  
def move(direction: str) -> Dict[str, Any]:
    sess = Session(bind=engine)
    prev, _ = check_if_db()
    m = move_(direction)
    sleep(15)
    curr, _ = check_if_db()
    assert curr==m['room_id']

    prev_room = sess.query(Room).filter(Room.room_id==prev).all()[0]

    # pardon this awful switch case business, prev_room.__dict__['direction_to'] didn't work.
    if direction == 'n':
        prev_room.n_to = curr
    elif direction == 's':
        prev_room.s_to = curr
    elif direction == 'e':
        prev_room.e_to = curr
    elif direction == 'w':
        prev_room.w_to = curr

    reverse = REVERSE[direction]
    curr_room = sess.query(Room).filter(Room.room_id==curr).all()[0]

    if reverse == 'n':
        curr_room.n_to = prev
    elif reverse == 's':
        curr_room.s_to = prev
    elif reverse == 'e':
        curr_room.e_to = prev
    elif reverse == 'w':
        curr_room.w_to = prev

    sess.commit()
    return m

def wander():
    sess = Session(bind=engine)
    curr, exits = init()
    sleep(1)
    # check which exits are unexplored.

    # take any unexplored one

    # unless they're all explored, then take a random one.
    pass

if __name__=='__main__':
   
    # print(move('s'))
    # print(move('w'))
    # print(move('e'))
