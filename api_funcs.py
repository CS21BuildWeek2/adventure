#!/usr/bin/env python

import os
from subprocess import run
from settings import (TOK, AUTH, INIT, TO_POST, TAKE, MOVE)

auth = f"""-H "Authorization: Token {TOK}" """
content_type_application_json = """-H "Content-Type: application/json" """
post = "curl -X POST " + auth + content_type_application_json

n = 'n'
s = 's'
w = 'w'
e = 'e'

def move(direction: str) -> None:
    bash = post + '-d \'{"direction": "' + direction + '"}\' ' + MOVE

    ret = os.system(bash)

    return ret


if __name__=='__main__':
    print(move(s))
