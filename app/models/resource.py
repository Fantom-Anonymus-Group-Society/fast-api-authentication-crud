import ormar
from datetime import datetime
from app.core.base_meta import BaseMeta


# Entity for controlling each resource, like:
'''
Digital ocean
link.to.digital-ocean.com
Some data for description (VPS which has core api, front-end and etc)
$6.00 per/month
'''


class Resource(ormar.Model):
    class Meta(BaseMeta):
        tablename = "resources"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255, nullable=False)
    link: str = ormar.String(max_length=255, nullable=True)
    description: str = ormar.Text(nullable=True)
    cost: str = ormar.Decimal(precision=100, scale=2, default="0.00")
    payment_period: str = ormar.String(max_length=255, nullable=False)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
