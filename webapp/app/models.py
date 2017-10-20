from webapp.app import db

class User(db.Model):
    vkid = db.Column(db.Integer, primary_key=True)