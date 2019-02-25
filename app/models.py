#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
if sys.platform != 'darwin':
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from sqlalchemy import Column, Integer, String, Text
from .database import Base, db_session, init_db


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Question_Answer(Base):
    __tablename__ = 'question_answers'

    id = Column(Integer, primary_key=True)
    question = Column(String(100), unique=True)
    answer = Column(Text, unique=True)

    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Question: %r, Answer: %r>' % (self.question) % (self.answer)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String(100), unique=True)

    def __init__(self, question=None):
        self.question = question

    def __repr__(self):
        return '<Question: %r>' % (self.question)


# create sqlite database
init_db()

# operations on models, later, encapsulate into class
def add_user(name, email):
    # pdb.set_trace()
    if name and email:
        u = User.query.filter(User.name == name).first()
        if not u:
            u = User(name, email)
            db_session.add(u)
            db_session.commit()

def update_user(name, email):
    # pdb.set_trace()
    if name and email:
        u = User.query.filter(User.name == name).first()
        if u:
            u.email = email
            db_session.commit()

def add_question_answer(question, answer):
    if question and answer:
        q_a = Question_Answer.query.filter(Question_Answer.question == question).first()
        if not q_a:
            q_a = Question_Answer(question, answer)
            db_session.add(q_a)
            db_session.commit()
