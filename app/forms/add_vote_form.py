from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerRangeField
from wtforms.validators import DataRequired


class VoteForm(FlaskForm):

    coffee_score = IntegerRangeField("☕ Coffee Score", validators=[DataRequired()])

    wifi_score = IntegerRangeField("📶 Wifi Score", validators=[DataRequired()])

    power_score = IntegerRangeField("💪 Power Score", validators=[DataRequired()])

    submit = SubmitField("Submit")
