"""empty message

Revision ID: 07672f9fcc7e
Revises: f0f6d4087912
Create Date: 2017-01-08 01:35:34.619714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07672f9fcc7e'
down_revision = 'f0f6d4087912'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bucketitem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('post', sa.String(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bucketitem')
    # ### end Alembic commands ###