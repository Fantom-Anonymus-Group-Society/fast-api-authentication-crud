"""create posts table

Revision ID: 3d5d66355ca5
Revises: e313fa7e24c5
Create Date: 2023-05-22 17:16:59.980964

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5d66355ca5'
down_revision = 'e313fa7e24c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(255), unique=True, nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('video_link', sa.String(1000), nullable=True),
        sa.Column('github_repo_link', sa.String(1000), nullable=True),
        sa.Column('picture', sa.String(255), nullable=False),
        sa.Column('category_id', sa.Integer, sa.ForeignKey("category.id"), nullable=False),
        sa.Column('is_published', sa.Boolean(), default=False, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), default=datetime.now)
    )


def downgrade() -> None:
    op.drop_table('posts')
