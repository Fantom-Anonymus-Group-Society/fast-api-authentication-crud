from pydantic import BaseModel


class UpdateUserSerializer(BaseModel):
    first_name: str | None
    last_name: str | None
    phone: str | None
    email: str | None
    is_staff: bool | None
    email_verified: bool | None
    password: str | None
