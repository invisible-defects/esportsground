from flask import render_template, flash, redirect, session, url_for, request, g
try:
    from webapp import webapp, db, oid
except:
    from webapp.webapp import webapp, db, oid

from flask_login import login_user, logout_user, current_user, login_required

try:
    from webapp.models import User
except:
    from webapp.webapp.models import User

try:
    from config import CONSTRUCTION
except:
    from webapp.config import CONSTRUCTION


from openid.extensions import pape


@webapp.route('/')
@webapp.route('/index')
@webapp.route('/profile')
def profile():
    return render_template("index.html")

@webapp.route('/register')
def menu():
    return render_template("register.html")

@webapp.route('/games')
def games():
    return render_template("games.html")

@webapp.before_request
def before_request():
    g.user = None


@webapp.route('/register_redirect', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None:
      return redirect(oid.get_next_url())

  else:
      openid = "http://steamcommunity.com/openid"
      if openid:
          pape_req = pape.Request([])
          return oid.try_login(openid, ask_for=['email', 'nickname'],
                               ask_for_optional=['fullname'],
                               extensions=[pape_req])
  return render_template('/templates/register.html', next=oid.get_next_url(),
                         error=oid.fetch_error())



@oid.after_login
def after_login(resp):
    identity_url = resp.identity_url
    identity = str(identity_url).split("/")[-1]
    user = User(vkid=101592050, steamid=identity)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("/games"))
