"""add user table

Revision ID: 10ea50374447
Revises: d0b4bcea2525
Create Date: 2022-10-26 17:26:51.493975

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '10ea50374447'
down_revision = 'd0b4bcea2525'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('email', sa.String, nullable=False, unique=True),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                              nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('users')
