"""create categories table

Revision ID: e313fa7e24c5
Revises: 46040d5a560b
Create Date: 2023-05-22 17:16:55.360207

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e313fa7e24c5'
down_revision = '46040d5a560b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(255), unique=True, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), default=datetime.now)
    )


def downgrade() -> None:
    op.drop_table('categories')
