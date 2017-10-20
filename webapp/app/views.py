from flask import render_template
from webapp.app import app

@app.route('/')
@app.route('/index')
@app.route('/profile')
def profile():
    return render_template("index.html")

@app.route('/games-menu')
def menu():
    return 0

@app.route('/csgo/stats')
def csgo_stats():
    return 0

@app.route('/csgo/team')
def csgo_team():
    return 0