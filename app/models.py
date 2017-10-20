from app import db

class User(db.Model):
    vkid = db.Column(db.String, primary_key=True)
    steamid = db.Column(db.String, index=True, unique=True)

    def __repr__(self):
        return self.vkid