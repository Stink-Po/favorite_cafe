from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class ChangePassword(FlaskForm):
    """flask wtf form for users change password"""
    password = PasswordField("Password", validators=[DataRequired(),

                                                     Length(min=8),

                                                     EqualTo("repeat_password",

                                                             message="passwords must mach")])

    repeat_password = PasswordField("Repeat Password", validators=[DataRequired()])

    submit = SubmitField("Save Change")
