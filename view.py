from app import app, db
from flask import render_template, request, send_from_directory, url_for, redirect
from models import Post, Tag
from forms import PostForm
from flask_sqlalchemy import BaseQuery

from flask_ckeditor import upload_success, upload_fail
import os
""" if len(tags) > 0:
                for t in tags.split():
                    tag = Tag(tags=t)
                    db.session.add(tag)
                    db.session.commit()

                    db.session.commit()"""

@app.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tags = request.form['tags']

        #try:
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()

        if len(tags) > 0:
            for t in tags.split():
                tag_n = db.session.query(Tag).filter_by(name=title).first().name

                if t == tag_n.name:
                    k = Post.query.filter(Post.title == title).all()
                    tt = Tag.query.filter(Tag.name == t).all()
                    p = k.tags.append(tt)
                    db.session.add(p)
                    db.session.commit()
                else:
                    tag = Tag(name=t)
                    db.session.add(tag)
                    db.session.commit()
                    k = Post.query.filter(Post.title == title).all()
                    tt = Tag.query.filter(Tag.name == t).all()
                    p = k.tags.append(tt)
                    db.session.add(p)
                    db.session.commit()

        """"except:
            print('Error commit db')
        return redirect(url_for('index'))"""

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