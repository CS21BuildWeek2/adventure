#!/usr/bin/env python
#
from typing import Dict, Any, Tuple, List
from time import sleep
from random import choice, sample

from sqlalchemy import create_engine, exists # type: ignore
from sqlalchemy.orm.session import Session, sessionmaker # type: ignore
from sqlalchemy.exc import OperationalError # type: ignore

from api_funcs import (status, init, move_, take_)
from model import Room, Base
from settings import REVERSE
from utils import bf_paths, df_paths, make_graph
engine = create_engine('sqlite:///map.db')
Session = sessionmaker()
Base.metadata.create_all(engine, checkfirst=True)


def check_if_db() -> Tuple[int, List[str]]:
    """ checks if the current room you're in is in the database.
    if not, adds it.
    to be helpful, returns current room id
    """
    sess = Session(bind=engine)
    i = init()
    sleep(i['cooldown'])
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
    sleep(m['cooldown'])
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

def wander() -> Dict[str, Any]:
    sess = Session(bind=engine)
    curr, exits = check_if_db()
    # check which exits are unexplored.
    curr_room = sess.query(Room).filter(Room.room_id==curr).all()[0]
    for direction in sample(exits, len(exits)):
        next_candidate = curr_room.__dict__[f'{direction}_to']
        if not next_candidate:
            moved_to = move(direction)
            return moved_to
       
    moved_to = move(choice(exits)) # unless they're all explored, then take a random one.
    return moved_to

def goto(start: int, end: int) -> Dict[str, Any]:
    sess = Session(bind=engine)
    graph = make_graph(sess)
    paths = bf_paths(graph, start)
    # print(paths)
    path = paths[(start, end)]
    print(f"it will take {17 * len(path) / 60} minutes to make {len(path)} moves")
    for direction in path:
        moved_to = move(direction)
        print(f"{moved_to['room_id']}: {moved_to['title']}")
    return moved_to

if __name__=='__main__':
    while True:
        wandered_to = wander()
        print(f"{wandered_to['room_id']}: {wandered_to['title']}")

    #goto(457,110)
    # goto(323, 433)
