from app import app, db
from flask import render_template, request, send_from_directory, url_for, redirect
from models import Post
from forms import PostForm
from flask_ckeditor import upload_success, upload_fail
import os


@app.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form('title')
        body = request.form('body')

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Error commit db')
        return redirect(url_for('index'))

    form = PostForm()
    return render_template('create.html', form=form)


@app.route('/')
def index():
    the_post = Post.query.all()
    return render_template('index.html', the_post=the_post)

"""@app.route('/files/<path:filename>')
def uploaded_files(filename):
    path = '../static/images'
    return send_from_directory(path, filename)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join('../static/images', f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)"""