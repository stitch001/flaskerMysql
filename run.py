#coding:utf-8
from flask import Flask
from flask import render_template

from os import environ
from mysqlFlask import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '7777'))
    except ValueError:
        PORT = 7777
    app.run(HOST, PORT, debug=True)