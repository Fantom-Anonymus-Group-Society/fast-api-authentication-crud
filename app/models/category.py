import ormar
from datetime import datetime
from app.core.base_meta import BaseMeta


class Category(ormar.Model):
    class Meta(BaseMeta):
        tablename = "categories"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255, nullable=False)
    slug: str = ormar.String(max_length=255, unique=True, nullable=False)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
