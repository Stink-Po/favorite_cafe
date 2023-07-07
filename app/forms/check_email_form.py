from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class CkeckEmailForm(FlaskForm):
    """flask wtf form for check users email when they forgot the password"""
    email = EmailField("Email", validators=[Email(), DataRequired()])
    submit = SubmitField("Check")
