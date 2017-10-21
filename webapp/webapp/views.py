from flask import render_template
from webapp import webapp

@webapp.route('/')
@webapp.route('/index')
@webapp.route('/profile')
def profile():
    return render_template("index.html")

@webapp.route('/register')
@webapp.route('/register.html')
def menu():
    return render_template("register.html")

@webapp.route('/games')
@webapp.route('/games.html')
def games():
    return render_template("games.html")