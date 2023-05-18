from app.models.user import User
from app.services.jwt_service import JWTService
from fastapi import Header, HTTPException


class BaseJWTAuthMiddleware:
    def __init__(self):
        self.no_token_error = HTTPException(status_code=401, detail="No Authorization header is provided")
        self.incorrect_token_error = HTTPException(status_code=401, detail="Incorrect token type")
        self.forbidden_error = HTTPException(status_code=403, detail="You are not permitted to use this source")

    def validate_payload_(self, authorization: str) -> dict:
        if authorization is None:
            raise self.no_token_error
        return JWTService.get_payload_from_token(authorization)

    async def get_and_validate_user_(self, payload: dict) -> User:
        user = await User.objects.get_or_none(id=payload.get('sub'))
        if not user or user.email != payload.get('email'):
            raise self.incorrect_token_error
        return user

    async def authenticate(self, authorization: str | None = Header(default=None)) -> User:
        payload = self.validate_payload_(authorization)
        return await self.get_and_validate_user_(payload)
