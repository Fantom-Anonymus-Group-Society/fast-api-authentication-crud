"""create resources table

Revision ID: 46040d5a560b
Revises: 455a60e0fc2a
Create Date: 2023-05-22 16:53:14.854542

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46040d5a560b'
down_revision = '455a60e0fc2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'resources',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('link', sa.String(255), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('cost', sa.DECIMAL(precision=100, scale=2), nullable=True),
        sa.Column('payment_period', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), default=datetime.now)
    )


def downgrade() -> None:
    op.drop_table('resources')
