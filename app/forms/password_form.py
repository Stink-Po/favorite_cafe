from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class PasswordForm(FlaskForm):
    """flask wtf form for users change password"""
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    submit = SubmitField("Check")
