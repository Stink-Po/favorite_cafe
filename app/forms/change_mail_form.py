from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import Email, DataRequired


class ChangeEmail(FlaskForm):
    """flask wtf form for change user email"""
    email = EmailField("Email", validators=[Email(), DataRequired()])

    submit = SubmitField("Save Change")
