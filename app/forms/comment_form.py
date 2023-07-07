from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class AddCommentForm(FlaskForm):
    """flask wtf form for comment for cafes"""
    comment_text = CKEditorField("Comment", validators=[DataRequired()])

    submit = SubmitField("Submit")
