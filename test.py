from app import db
from models import Post


p1 = Post.query.all()
print(p1)

p2 = Post.query.filter(Post.title.contains('first')).all()

print(p2)