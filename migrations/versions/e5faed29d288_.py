"""empty message

Revision ID: e5faed29d288
Revises: 24b78d807d50
Create Date: 2019-12-17 10:42:36.591513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5faed29d288'
down_revision = '24b78d807d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('uid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'message', 'user', ['uid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'message', type_='foreignkey')
    op.drop_column('message', 'uid')
    # ### end Alembic commands ###