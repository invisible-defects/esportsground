from flask_wtf import Form
from flask_inputs import validators
from wtforms import PasswordField, StringField
from webapp.models import User


class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField("Passwor")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

