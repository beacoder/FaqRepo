#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

# codes will be executed when app-package is imported

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/faq_repo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# member variables of app-package
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# place at bottom to avoid circular imports
from app import routes, models
