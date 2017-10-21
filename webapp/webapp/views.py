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