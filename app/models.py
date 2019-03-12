#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/FaqRepo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db, login
from flask_login import UserMixin
from time import time
import jwt


class User(UserMixin, db.Model):  # enable flask_login with UserMixin
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)  # index makes searching efficient
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


# flask_login use this to load user into memory
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True, unique=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # foreignkey links to user table

    def __repr__(self):
        return '<Post {}>'.format(self.body)


# class Question_Answer(db.Model):
#     __tablename__ = 'question_answers'

#     id = Column(Integer, primary_key=True)
#     question = Column(String(100), unique=True)
#     answer = Column(Text, unique=True)

#     def __init__(self, question=None, answer=None):
#         self.question = question
#         self.answer = answer

#     def __repr__(self):
#         return '<Question: %r, Answer: %r>' % (self.question) % (self.answer)


# class Question(db.Model):
#     __tablename__ = 'questions'

#     id = Column(Integer, primary_key=True)
#     question = Column(String(100), unique=True)

#     def __init__(self, question=None):
#         self.question = question

#     def __repr__(self):
#         return '<Question: %r>' % (self.question)


# # create sqlite database
# init_db()

# # operations on models, later, encapsulate into class
# def add_user(name, email):
#     # pdb.set_trace()
#     if name and email:
#         u = User.query.filter(User.name == name).first()
#         if not u:
#             u = User(name, email)
#             db_session.add(u)
#             db_session.commit()

# def update_user(name, email):
#     # pdb.set_trace()
#     if name and email:
#         u = User.query.filter(User.name == name).first()
#         if u:
#             u.email = email
#             db_session.commit()

# def add_question_answer(question, answer):
#     if question and answer:
#         q_a = Question_Answer.query.filter(Question_Answer.question == question).first()
#         if not q_a:
#             q_a = Question_Answer(question, answer)
#             db_session.add(q_a)
#             db_session.commit()
