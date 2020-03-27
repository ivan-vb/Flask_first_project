from app import app, db
from flask import render_template, request, send_from_directory, url_for, redirect
from models import Post, Tag
from forms import PostForm
from flask_sqlalchemy import BaseQuery
import sqlalchemy

from flask_ckeditor import upload_success, upload_fail
import os


@app.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tags = request.form['tags']
        categories = request.form['categories']


        try:
            str_body = str(body)
            if str_body.find('src=') is not -1:
                start = str_body.find('src=')
                end = str_body.find('"', start+7)
                url_image = str_body[start+5:end]
            else:
                url_image = '../static/images/image_1.jpg'

            post = Post(title=title, body=body, url_image=url_image)
            db.session.add(post)
            db.session.commit()
            if len(tags) > 0:
                for t in tags.split(', '):
                    tag_n = db.session.query(Tag).filter(Tag.name == t).first()
                    if tag_n is not None:
                        post_tags_id = db.session.query(Post).filter(Post.title == title).first()
                        if tag_n not in post_tags_id.tags:
                            tag = db.session.query(Tag).filter(Tag.name == t).first()
                            post.tags.append(tag)
                            db.session.commit()
                    else:
                        tag = Tag(name=t)
                        db.session.add(tag)
                        post.tags.append(tag)
                        db.session.commit()
        except:
            print('Error commit db')
        return redirect(url_for('index'))

    form = PostForm()
    bb = '<p>Foto2</p><p><img alt="" src="/files/0122266.jpg" style="height:1200px; width:1600px" /></p>'
    dd = 'dog, cat'
    return render_template('create.html', form=form, bb=bb, dd=dd)


@app.route('/')
def index():
    the_post = Post.query.all()
    return render_template('index.html', the_post=the_post)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

@app.route('/files/<path:filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg', 'mp3']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)
