from flask import render_template
from webapp import webapp, db, lm, oid
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User


@webapp.route('/')
@webapp.route('/index')
@webapp.route('/profile')
def profile():
    return render_template("index.html")

@webapp.route('/register')
def menu():
    return render_template("register.html")

@webapp.route('/csgo/stats')
def csgo_stats():
    return """<h1>This page is under construction</h1>
    <img src="https://i.pinimg.com/736x/00/8e/8f/008e8f7c946120650b7b254e2a72e7a4--caution-signs-construction-\
    signs.jpg" alt="Smiley face" height="500" width="500">"""

@webapp.route('/csgo/team')
def csgo_team():
    return """<h1>This page is also under construction</h1>
    <img src="https://i.pinimg.com/736x/00/8e/8f/008e8f7c946120650b7b254e2a72e7a4--caution-signs-construction-\
    signs.jpg" alt="Smiley face" height="500" width="500">"""

    from flask import render_template, flash, redirect, session, url_for, request, g




@app.route('/templates/register', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
      return redirect(url_for("templates/register"))
  form = LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for = ['steam_id'])
  return render_template('templates/register.html', 
      title = 'Sign In',
      form = form,
      providers = webapp.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.steam_id is None or resp.steam_id == "":
        flash('Invalid steam_id. Please try again.')
        return redirect(url_for('register'))
    user = User.query.filter_by(steamid = resp.steam_id).first()
    if user is None:
        user = User.steamid=steam_id
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('register'))