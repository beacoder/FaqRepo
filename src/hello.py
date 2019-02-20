#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

import pdb
from flask import Flask
from database import db_session, init_db
from models import User


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def add_user(name, email):
    init_db()
    # pdb.set_trace()
    if name and email:
        u = User.query.filter(User.name == name).first()
        if not u:
            u = User(name, email)
            db_session.add(u)
            db_session.commit()

add_user('name', 'admin@localhost')
