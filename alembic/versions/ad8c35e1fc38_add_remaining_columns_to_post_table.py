"""add remaining columns to post table

Revision ID: ad8c35e1fc38
Revises: 54f68011ae97
Create Date: 2022-10-26 17:54:44.187285

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ad8c35e1fc38'
down_revision = '54f68011ae97'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean, server_default='True', nullable=False))
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
