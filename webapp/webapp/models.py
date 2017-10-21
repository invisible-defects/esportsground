try:
    from webapp import db
except:
    from webapp.webapp import db


class User(db.Model):
    vkid = db.Column(db.String, primary_key=True)
    steamid = db.Column(db.String, index=True, unique=True)
    score = db.Column(db.Integer)

    def __repr__(self):
        return self.vkid