"""empty message

Revision ID: 6d4c426efb4f
Revises: 
Create Date: 2016-12-14 05:20:56.087048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d4c426efb4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column(u'posts', 'author_id')
    op.drop_table('users')
    # ### end Alembic commands ###
