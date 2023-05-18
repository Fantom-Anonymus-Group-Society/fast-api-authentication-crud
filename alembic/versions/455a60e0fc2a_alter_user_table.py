"""alter user table

Revision ID: 455a60e0fc2a
Revises: fb59eb10007c
Create Date: 2023-05-07 15:19:27.612065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455a60e0fc2a'
down_revision = 'fb59eb10007c'
branch_labels = None
depends_on = None

'''
 This is an example migration for altering user table after creating the new one
'''


def upgrade() -> None:
    op.alter_column(
        'users',
        'password',
        nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        'users',
        'password',
        nullable=False
    )
