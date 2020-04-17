"""empty message

Revision ID: 3ffa29982674
Revises: 7310178234ef
Create Date: 2019-12-17 10:32:37.631662

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3ffa29982674'
down_revision = '7310178234ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'time_begin')
    op.drop_column('message', 'time_end')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('time_end', mysql.TIME(), nullable=True))
    op.add_column('message', sa.Column('time_begin', mysql.TIME(), nullable=True))
    # ### end Alembic commands ###
