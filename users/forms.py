from wtforms import Form, StringField, PasswordField


class UserForm(Form):
    email = StringField('Email')
    password = PasswordField('Password')
