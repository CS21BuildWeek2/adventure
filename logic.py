#!/usr/bin/env python

from api_funcs import (status, init, move, take)


def move_and_take_items(direction: str):
    n = move(direction)
    for item in n['items']:
        take(item)
