"""create user table

Revision ID: fb59eb10007c
Revises: 
Create Date: 2023-05-07 15:19:22.214994

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb59eb10007c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(255), nullable=True),
        sa.Column('last_name', sa.String(255), nullable=True),
        sa.Column('phone', sa.String(20), nullable=True, unique=True),
        sa.Column('email', sa.String(255), nullable=True, unique=True),
        sa.Column('is_staff', sa.Boolean(), default=False),
        sa.Column('email_verified', sa.Boolean(), default=False),
        sa.Column('password', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), default=datetime.now)
    )


def downgrade() -> None:
    op.drop_table('users')
