from fastapi import Header
from app.middlewares.staff_middleware import StaffMiddleware
from app.middlewares.base_jwt_auth_middleware import BaseJWTAuthMiddleware


async def jwt_authentication_middleware(authorization: str | None = Header(default=None)):
    return await (BaseJWTAuthMiddleware()).authenticate(authorization)


async def jwt_staff_middleware(authorization: str | None = Header(default=None)):
    return await (StaffMiddleware()).authenticate(authorization)
