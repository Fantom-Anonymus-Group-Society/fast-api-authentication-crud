from typing import Optional, Union

import ormar
from datetime import datetime
from app.core.base_meta import BaseMeta
from app.models.category import Category


class Post(ormar.Model):
    class Meta(BaseMeta):
        tablename = "posts"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255, nullable=False)
    slug: str = ormar.String(max_length=255, unique=True, nullable=False)
    description: str = ormar.Text(nullable=True)
    video_link: str = ormar.String(max_length=1000, nullable=True)
    github_repo_link: str = ormar.String(max_length=1000, nullable=True)
    is_published: str = ormar.Boolean(default=False)
    picture: str = ormar.String(max_length=255, nullable=False)
    category: Optional[Union[Category, dict]] = ormar.ForeignKey(Category, related_name="posts", ondelete="RESTRICT")
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
