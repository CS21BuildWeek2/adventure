#!/usr/bin/env python
from typing import Dict, Any
import os
from subprocess import run
import requests
import urllib
import json
from settings import (TOK, AUTH, TREASURE_HUNT, INIT, TO_POST, TAKE, MOVE, BC)

auth = f"""-H "Authorization: Token {TOK}" """
content_type_application_json = """-H "Content-Type: application/json" """
post = "curl -X POST " + auth + content_type_application_json
get = "curl -X GET " + auth
n = 'n'
s = 's'
w = 'w'
e = 'e'

def status() -> Dict[str, Any]:
    headers = TO_POST
    response_ = requests.post(f'{TREASURE_HUNT}status/', headers=headers)
    response = response_.json()
    return response

def init() -> Dict[str, Any]:
    headers = AUTH
    response_ = requests.get(f'{TREASURE_HUNT}init/', headers=headers)
    response = response_.json()
    return response

def move_(direction: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {'direction': direction}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}move/', headers=headers, data=data, verify=True)
    response = response_.json()
    return response

def move_wise_(direction: str, next_room_id: int) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {'direction': direction, "next_room_id": f"{next_room_id}"}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}move/', headers=headers, data=data, verify=True)
    response = response_.json()
    return response

def take_(item: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"name": item}
    data = json.dumps(data_)
    response_ = requests.post(TAKE, headers=headers, data=data)
    response = response_.json()
    return response

def sell_init_(item: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"name": item}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}sell/', headers=headers, data=data)
    response = response_.json()
    return response

def sell_confirm_(item: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"name": item, "confirm": "yes"}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}sell/', headers=headers, data=data)
    response = response_.json()
    return response

def name_change(new_name: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"name": f"[{new_name}]", "confirm": "aye"}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}change_name/', headers=headers, data=data)
    response = response_.json()
    return response

def examine(thing: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"name": thing}
    data = json.dumps(data_)
    response_ = requests.post(f'{TREASURE_HUNT}examine/', headers=headers, data=data)
    response = response_.json()
    return response

def pray() -> Dict[str, Any]:
    headers = TO_POST
    response_ = requests.post(f'{TREASURE_HUNT}pray/', headers=headers)
    response = response_.json()
    return response

def mine_(new_proof: str) -> Dict[str, Any]:
    headers = TO_POST
    data_ = {"proof": new_proof}
    data = json.dumps(data_)
    response_ = requests.post(f'{BC}mine/', headers=headers, data=data)
    response = response_.json()
    return response

def last_proof_() -> Dict[str, Any]:
    headers = AUTH
    response_ = requests.get(f'{BC}last_proof/', headers=headers)
    response = response_.json()
    return response



#f __name__=='__main__':
#   #print(move(s))
#    print(init())
#   x = move(s)
#   y = init()
#   print(type(x))
#   print(type(y))
