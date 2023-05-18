from pydantic import BaseModel


class CreateUserSerializer(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
