from app import app, db
from flask import render_template, request, send_from_directory, url_for, redirect
from models import Post, Tag
from forms import PostForm
from flask_sqlalchemy import BaseQuery
import sqlalchemy


title = 'Как поколение Y управляет вами'

tags = 'human, dog'


if len(tags) > 0:
    for t in tags.split(','):
        tag_n = db.session.query(Tag.name).filter(Tag.name == t).first()


        if tag_n == None:
            tag = Tag(name=t)

            """db.session.add(tag)
            db.session.commit()"""
            k = Post.query.filter(Post.title == title).all()
            tt = db.session.query(Tag).filter(Tag.name == t).first()
            print(str(tt), '1111')
            """p = k.tags.append(tt)
            db.session.add(p)
            db.session.commit()"""
        else:
            k = Post.query.filter(Post.title == title).all()
            tt = Tag.query.filter(Tag.name == t).all()
            print('hi')
            """p = k.tags.append(tt)
            db.session.add(p)
            db.session.commit()"""

