from wtforms import Form, StringField, SubmitField, BooleanField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm


class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body')
    tags = StringField('Tags')
    submit = SubmitField('Submit')