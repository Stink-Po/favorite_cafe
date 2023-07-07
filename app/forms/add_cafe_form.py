from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, FileField, TimeField, IntegerField, IntegerRangeField
from wtforms.validators import DataRequired


class UserAddCafeForm(FlaskForm):
    """flask wtf from that's manage users add a new café"""
    name = StringField("Name", validators=[DataRequired()])

    cafe_theme = SelectField("Theme",
                             choices=[
                                 "Rustic and cozy",
                                 "Industrial chic",
                                 "Modern greenery",
                                 "Beach vibes",
                                 "Coastal Beach"
                                 "Traditional European",
                                 "Vintage Retro",
                                 "Garden Oasis",
                                 "Artistic Vibes",
                                 "Industrial Chic",
                                 "Library Cafe",
                                 "Scandinavian Minimalism",
                                 "Parisian Bistro",
                                 "Oriental Zen",
                                 "Sports Lounge",
                                 "Others",
                             ],
                             validators=[DataRequired()])

    open_time = TimeField("Open Time", validators=[DataRequired()])

    close_time = TimeField("Close Time", validators=[DataRequired()])

    image = FileField("Image", validators=[DataRequired()])

    can_take_calls = SelectField("Can take Call ?",
                                 choices=["Yes", "No"],
                                 validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])

    phone = StringField("Phone Number", validators=[DataRequired()])

    coffee_score = IntegerRangeField("☕ Coffee Score", validators=[DataRequired()])

    wifi_score = IntegerRangeField("📶 Wifi Score", validators=[DataRequired()])

    power_score = IntegerRangeField("💪 Power Score", validators=[DataRequired()])

    about = CKEditorField("About Cafe")

    submit = SubmitField("Submit")


class OwnerAddCafeForm(FlaskForm):
    """flask wtf from that's manage café owners add a new café"""
    name = StringField("Name", validators=[DataRequired()])

    cafe_theme = SelectField("Theme",
                             choices=[
                                 "Rustic and cozy",
                                 "Industrial chic",
                                 "Modern greenery",
                                 "Beach vibes",
                                 "Traditional European",
                                 "Others"
                             ],
                             validators=[DataRequired()])

    open_time = TimeField("Open Time", validators=[DataRequired()])

    close_time = TimeField("Close Time", validators=[DataRequired()])

    image = FileField("Image", validators=[DataRequired()])

    staff = IntegerField("Staff", validators=[DataRequired()])

    can_take_calls = SelectField("Can take Call ?",
                                 choices=["Yes", "No"],
                                 validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])

    phone = StringField("Phone Number", validators=[DataRequired()])

    submit = SubmitField("Submit")
