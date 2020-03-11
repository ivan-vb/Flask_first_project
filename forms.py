from wtforms import Form, StringField, SubmitField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm


class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body')   # <--
    submit = SubmitField('Submit')