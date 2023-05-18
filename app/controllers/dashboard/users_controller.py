from typing import List
from app.models.user import User
from fastapi import APIRouter, Depends, status, HTTPException
from app.middlewares import jwt_staff_middleware
from app.serializers.users.create_user_serializer import CreateUserSerializer
from app.serializers.users.get_user_serializer import GetUserSerializer
from app.serializers.users.update_user_serializer import UpdateUserSerializer
from app.services.hasher_service import HasherService

router = APIRouter(
    prefix="/dashboard/users",
    tags=["dashboard_users"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[GetUserSerializer])
async def user_index(page: int = 1, user: User = Depends(jwt_staff_middleware)):
    return await User.objects.paginate(page).all()


@router.get('/{id}', response_model=GetUserSerializer)
async def user_index(id: int, user: User = Depends(jwt_staff_middleware)):
    user = await User.objects.get_or_none(pk=id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not found")
    return user


@router.post('/', response_model=GetUserSerializer, status_code=status.HTTP_201_CREATED)
async def user_store(body: CreateUserSerializer, user: User = Depends(jwt_staff_middleware)):
    return await User.objects.create(
        email=body.email,
        password=HasherService.get_password_hash(body.password),
        first_name=body.first_name,
        last_name=body.last_name,
        phone=body.phone,
    )


@router.patch("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user_update(id: int, body: UpdateUserSerializer, current_user: User = Depends(jwt_staff_middleware)):
    user = await User.objects.get_or_none(pk=id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not found")
    user.email = body.email if body.email is not None else user.email
    user.first_name = body.first_name if body.first_name is not None else user.first_name
    user.last_name = body.last_name if body.last_name is not None else user.last_name
    user.phone = body.phone if body.phone is not None else user.phone
    user.is_staff = body.is_staff if body.is_staff is not None else user.is_staff
    user.email_verified = body.email_verified if body.email_verified is not None else user.email_verified
    user.password = HasherService.get_password_hash(body.password) if body.password is not None else user.password
    await user.update()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user_destroy(id: int, current_user: User = Depends(jwt_staff_middleware)):
    user = await User.objects.get_or_none(pk=id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not found")
    await user.delete()
