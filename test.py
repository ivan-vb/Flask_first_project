from app import db
from models import Post
from datetime import date

p1 = Post.query.all()
print(p1)

for p in p1:
    print(p.created.strftime("%B %d, %Y"))
    print(p.created.strftime("%B %Y"))