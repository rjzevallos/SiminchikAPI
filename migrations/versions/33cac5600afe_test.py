"""test

Revision ID: 33cac5600afe
Revises: 
Create Date: 2021-02-23 13:08:28.791283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33cac5600afe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=False),
    sa.Column('old_password', sa.String(length=100), nullable=True),
    sa.Column('wrong_login_attempt', sa.Integer(), nullable=True),
    sa.Column('today_login_attempt', sa.Integer(), nullable=True),
    sa.Column('is_now_login', sa.Integer(), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('type_doc_id', sa.Integer(), nullable=False),
    sa.Column('num_doc', sa.String(length=50), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('dialect_id', sa.Integer(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('num_doc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('blacklist_tokens')
    op.drop_table('account')
    # ### end Alembic commands ###