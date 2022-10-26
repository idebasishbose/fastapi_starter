"""add content column in  posts table

Revision ID: d0b4bcea2525
Revises: fbb83e2400f7
Create Date: 2022-10-26 17:16:02.255149

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd0b4bcea2525'
down_revision = 'fbb83e2400f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
