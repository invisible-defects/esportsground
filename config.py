import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OPENID_PROVIDERS = "http://steamcommunity.com/openid/id/"

CONSTRUCTION = """<h1>This page is also under construction</h1>
    <img src="https://i.pinimg.com/736x/00/8e/8f/008e8f7c946120650b7b254e2a72e7a4--caution-signs-construction-\
    signs.jpg" alt="Smiley face" height="500" width="500">"""