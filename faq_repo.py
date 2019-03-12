#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/FaqRepo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from app import app

# import pdb
# from flask import Flask
# from .database import db_session
# from .models import add_user, add_question_answer, User, Question_Answer

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

# add_user('name', 'admin@localhost')

# add_question_answer('This is the first question?', 'Yes, it is.')

# @app.route('/users')
# def list_users():
#     return '-'.join([str(user) for user in  User.query.all()])

# @app.route('/questions')
# def list_users():
#     return '-'.join([str(q_a) for q_a in Question_Answer.query.all()])
