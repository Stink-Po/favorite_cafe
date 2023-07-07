from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateBlogPostForm(FlaskForm):
    """flask wtf form for create new blog post"""
    title = StringField("Blog Post Title", validators=[DataRequired()])

    subtitle = StringField("Subtitle", validators=[DataRequired()])

    body = CKEditorField("Blog Content", validators=[DataRequired()])

    submit = SubmitField("Submit Post")
