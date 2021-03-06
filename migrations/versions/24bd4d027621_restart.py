"""Restart?

Revision ID: 24bd4d027621
Revises: 
Create Date: 2022-05-12 10:08:26.859004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24bd4d027621'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=12), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('slug', sa.String(length=250), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('folder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('slug', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('cover', sa.String(length=120), nullable=True),
    sa.Column('media', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('slug', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('body2', sa.Text(), nullable=True),
    sa.Column('body3', sa.Text(), nullable=True),
    sa.Column('body4', sa.Text(), nullable=True),
    sa.Column('body5', sa.Text(), nullable=True),
    sa.Column('cit', sa.Text(), nullable=True),
    sa.Column('cit2', sa.Text(), nullable=True),
    sa.Column('cit3', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('folder')
    op.drop_table('cit')
    op.drop_table('user')
    # ### end Alembic commands ###
