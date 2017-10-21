from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy

webapp = Flask(__name__, static_url_path='')
webapp.config.from_pyfile("/home/deniska/Projects/esportsground/webapp/config.py")

@webapp.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@webapp.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@webapp.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@webapp.route('/gameFiles/<path:path>')
def send_game_file(path):
    return send_from_directory('gameFiles', path)

db = SQLAlchemy(webapp)

import os

from flask_login import LoginManager
from flask_openid import OpenID

try:
    from config import basedir
except:
    from webapp.config import basedir

lm = LoginManager()
lm.init_app(webapp)
lm.login_view = 'register'
oid = OpenID(webapp, os.path.join(basedir, 'tmp'))

from webapp import views, models
