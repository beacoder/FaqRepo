#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/faq_repo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)  # index makes searching efficient
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


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
