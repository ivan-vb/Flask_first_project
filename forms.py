from wtforms import Form, StringField, SubmitField, BooleanField, SelectField, FileField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm

categories_name = ('Fashion', 'Technology', 'Travel', 'Food', 'Photography', 'Sport')


class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body')
    tags = StringField('Tags')
    submit = SubmitField('Submit')
    categories = SelectField(label='Categories', choices=[(categories, categories) for categories in categories_name])
    foto = FileField('Foto')
