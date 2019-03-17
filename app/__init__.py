#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

# codes will be executed when app-package is imported

import sys
if sys.platform == 'darwin':
    sys.path.insert(0, "/Users/chenhuming/workspace/faqrepo/venv/lib/python3.7/site-packages")
else:
    sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from logging.handlers import RotatingFileHandler
import os


# member variables of app-package
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'  # indicate which function handles login
mail = Mail(app)
bootstrap = Bootstrap(app)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/faqrepo.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('FaqRepo startup')


# place at bottom to avoid circular imports
from app import routes, models, errors
