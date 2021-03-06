"""empty message

Revision ID: 625db4d77e8b
Revises: 52ec25eec86d
Create Date: 2021-03-24 22:53:09.091166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '625db4d77e8b'
down_revision = '52ec25eec86d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('likes', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweets', 'likes')
    # ### end Alembic commands ###
