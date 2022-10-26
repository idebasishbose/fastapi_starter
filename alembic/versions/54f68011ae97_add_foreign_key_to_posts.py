"""add foreign-key to posts

Revision ID: 54f68011ae97
Revises: 10ea50374447
Create Date: 2022-10-26 17:41:22.575322

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '54f68011ae97'
down_revision = '10ea50374447'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_id_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts_users_id_fk', 'posts')
    op.drop_column('posts', 'owner_id')

