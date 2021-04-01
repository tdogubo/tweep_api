"""empty message

Revision ID: a3ec1fedd51f
Revises: 4de35200d913
Create Date: 2021-03-26 14:41:42.005361

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a3ec1fedd51f'
down_revision = '4de35200d913'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('likes', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('likes', sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###