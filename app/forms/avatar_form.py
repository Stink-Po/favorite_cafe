from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField
from wtforms.validators import DataRequired


class AvatarForm(FlaskForm):
    image = FileField("Image", validators=[DataRequired()])
    submit = SubmitField("Save")
