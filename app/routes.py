#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

# import app variable from app-module
from app import app

# view-function for mapping url to request-handler
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
