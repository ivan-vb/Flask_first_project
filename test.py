from app import db
from models import Post, Tag
from datetime import date


"""contents = ['1="animals"', '2="human"', '3="people"', '4="cat"', '5="dog"', '6="nature"', '7="leave"', '8="food"' ]

con_post = [
title='A Loving Heart is the Truest Wisdom',
body='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.',
url_image='../static/images/image_1.jpg',
categories='Travel',
description='A small river named Duden flows by their place and supplies it with the necessary regelialia.',
num_comments='5'

title='Great Things Never Came from Comfort Zone',
body='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.',
url_image='../static/images/image_2.jpg',
categories='Travel',
description='A small river named Duden flows by their place and supplies it with the necessary regelialia.',
num_comments='3'

title='Paths Are Made by Walking',
body='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.',
url_image='../static/images/image_3.jpg',
categories='Lifestyle',
description='A small river named Duden flows by their place and supplies it with the necessary regelialia.',
num_comments='4'
]
"""
"""p1 = Tag.query.all()
print(p1)"""

"""for p in p1:
    print(p.created.strftime("%B %d, %Y"))
    print(p.created.strftime("%B %Y"))"""