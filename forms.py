from wtforms import Form, StringField, SubmitField
from flask_ckeditor import CKEditorField


class PostForm(Form):
    title = StringField('Title')
    body = CKEditorField('Body')   # <--
    submit = SubmitField('Submit')