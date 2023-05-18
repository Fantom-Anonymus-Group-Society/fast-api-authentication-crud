from datetime import datetime
from pydantic import BaseModel


class GetUserSerializer(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    is_staff: bool
    email_verified: bool
    created_at: datetime
