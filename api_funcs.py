#!/usr/bin/env python

import os
from subprocess import run
import requests
from settings import (TOK, AUTH, TREASURE_HUNT, INIT, TO_POST, TAKE, MOVE)

auth = f"""-H "Authorization: Token {TOK}" """
content_type_application_json = """-H "Content-Type: application/json" """
post = "curl -X POST " + auth + content_type_application_json
get = "curl -X GET " + auth
n = 'n'
s = 's'
w = 'w'
e = 'e'

def status() -> dict():
    headers = TO_POST
    response_ = requests.post(f'{TREASURE_HUNT}status/', headers=headers)
    response = response_.json()
    return response

def init() -> dict():
    headers = AUTH
    response_ = requests.get(f'{TREASURE_HUNT}init/', headers=headers)
    response = response_.json()
    return response

def move(direction: str) -> dict():
    headers = TO_POST
    data = {'direction': direction}
    response_ = requests.post(f'{TREASURE_HUNT}move/', headers=headers, data=data, verify=True)
    # response = response_.json()
    print(response_.headers)
    return response_

def take(item: str) -> str:
    headers = TO_POST
    data = {
        "name", item
    }
    response = requests.post(TAKE, headers=headers, data=str(data))
    return response.json()

if __name__=='__main__':
    #print(move(s))
#    print(init())
    x = move(s)
    y = init()
    print(type(x))
    print(type(y))
