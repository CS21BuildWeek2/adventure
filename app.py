#!/usr/bin/env python

import os
from typing import Optional
import requests
from flask import Flask, jsonify

from settings import (TOK, AUTH, INIT, TO_POST, TAKE, MOVE)

def create_app():
    ''' create and configure an instance of the Flask application '''
    app = Flask(__name__)
    app.config['ENV'] = 'debug' # TODO: Change beffore deploying



    @app.route("/init")
    def view() -> str:
        response = requests.get(INIT, headers=AUTH)
        return response.json()

    @app.route('/take-item/<item>')
    def take_treasure(item: Optional[str] = None) -> str:
        # havent' verified that this works yet.
        data = {"name": item}
        print(item)
        response = requests.post(TAKE, headers=TO_POST, data=str(data))
        return str(response)

    @app.route('/move/<direction>')
    def move(direction: Optional[str] = None) -> str:
        data = {"direction", direction}
        response = requests.post(MOVE, headers=TO_POST, data=str(data))
        return response.json()

    return app

if __name__=='__main__':
    app = create_app()
    app.run()
