"""empty message

Revision ID: 5f743191868e
Revises: 
Create Date: 2020-03-13 00:15:00.571617

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5f743191868e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=80), nullable=True))
    # ### end Alembic commands ###
