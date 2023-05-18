from app.models.user import User
from fastapi import Header
from app.middlewares.base_jwt_auth_middleware import BaseJWTAuthMiddleware


class StaffMiddleware(BaseJWTAuthMiddleware):
    async def authenticate(self, authorization: str | None = Header(default=None)) -> User:
        payload = self.validate_payload_(authorization)
        if not payload.get('is_staff'):
            raise self.forbidden_error
        return await self.get_and_validate_user_(payload)
