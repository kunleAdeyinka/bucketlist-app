"""empty message

Revision ID: f0f6d4087912
Revises: 7072116142b3
Create Date: 2016-12-20 06:17:23.821772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0f6d4087912'
down_revision = '7072116142b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    # ### end Alembic commands ###
