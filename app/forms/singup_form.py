from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class SingUpForm(FlaskForm):
    """flask wtf form for users sing in"""
    user_name = StringField("Username", validators=[DataRequired()])

    email = EmailField("Email", validators=[Email(), DataRequired()])

    password = PasswordField("Password", validators=[DataRequired(),

                                                     Length(min=8),

                                                     EqualTo("repeat_password",

                                                             message="passwords must mach")])

    repeat_password = PasswordField("Repeat Password", validators=[DataRequired()])
    accept_terms = BooleanField("Accept terms and Conditions", validators=[DataRequired()])

    submit = SubmitField("Sing Up")
