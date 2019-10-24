#!/usr/bin/env python
import os
from dotenv import load_dotenv
load_dotenv()

TOK = os.getenv('TOKEN')
TREASURE_HUNT = os.getenv('TREASURE_HUNT')
INIT = os.getenv('INIT')
TAKE = os.getenv('TAKE')
MOVE = os.getenv('MOVE')
AUTH = {'Authorization': f'Token {TOK}'}
CONTENT_TYPE_APPLICATION_JSON = {'Content-Type': 'application/json'}
TO_POST = {**AUTH, **CONTENT_TYPE_APPLICATION_JSON}
REVERSE = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
