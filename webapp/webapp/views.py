from flask import render_template
from webapp import webapp
from config import VK_ID

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
    user = getUser(VK_ID)
    stats = user.csgo_stats

    stat_params = {
        "skill" : user.R,
        "time_played" : stats[-2],
        "hs_rate" : (str(stats[2]/stats[1]))[0:3],
        "kda" : (str(stats[1]/stats[0]))[0:3]
    }
    return render_template("games.html", stat=stat_params)