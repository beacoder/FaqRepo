#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from flask import render_template
from app import app

# view-function for mapping url to request-handler
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Huming'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
