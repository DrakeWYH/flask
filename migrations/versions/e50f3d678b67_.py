"""empty message

Revision ID: e50f3d678b67
Revises: 3ffa29982674
Create Date: 2019-12-17 10:33:03.862535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e50f3d678b67'
down_revision = '3ffa29982674'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('time_begin', sa.DateTime(), nullable=True))
    op.add_column('message', sa.Column('time_end', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'time_end')
    op.drop_column('message', 'time_begin')
    # ### end Alembic commands ###
