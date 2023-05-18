from fastapi import FastAPI
from app.core.base_meta import database
from app.controllers.dashboard import (
    users_controller as dash_users_controller
)
from app.services.connection_service import ConnectionService

app = FastAPI(title="FastApi app")

# Set WebSocket service
connection_service = ConnectionService()

app.include_router(dash_users_controller.router)

@app.get('/')
async def root():
    # create a dummy entry
    try:
        from app.models.user import User
        from app.services.hasher_service import HasherService
        await User.objects.get_or_create(
            email="admin@gmail.com",
            is_staff=True,
            password=HasherService.get_password_hash('admin'),
            first_name="admin",
            last_name="maxima",
            phone="228",
        )
    except:
        pass
    return {'detail': 'Root'}


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
