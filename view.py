from app import app
from flask import render_template
from models import Post


@app.route('/')
def index():
    the_post = Post.query.all()
    return render_template('index.html', the_post=the_post)
