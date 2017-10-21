from flask import Flask
from flask_sqlalchemy import SQLAlchemy

webapp = Flask(__name__)
webapp.config.from_object("config")

db = SQLAlchemy(webapp)

import os

from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(webapp)
lm.login_view = 'register'
oid = OpenID(webapp, os.path.join(basedir, 'tmp'))

from webapp import views, models
