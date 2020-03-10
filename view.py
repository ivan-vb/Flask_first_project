from app import app
from flask import render_template
from models import Post
from forms import PostForm


@app.route('/create')
def create_post():
    form = PostForm()
    return render_template('create.html', form=form)


@app.route('/')
def index():
    the_post = Post.query.all()
    return render_template('index.html', the_post=the_post)
