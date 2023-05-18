import ormar
from datetime import datetime
from app.core.base_meta import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    first_name: str = ormar.String(max_length=255, nullable=True)
    last_name: str = ormar.String(max_length=255, nullable=True)
    phone: str = ormar.String(max_length=20, unique=True, nullable=True)
    email: str = ormar.String(max_length=255, unique=True, nullable=False)
    is_staff: str = ormar.Boolean(default=False)
    email_verified: str = ormar.Boolean(default=False)
    password: str = ormar.String(max_length=255, nullable=False)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
