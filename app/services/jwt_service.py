import jwt
import datetime
from app.models.user import User
from fastapi import HTTPException
from app.configs.environment import env


class JWTService:
    @staticmethod
    def create_token_by_user(user: User, additional_payload=None) -> str:
        if additional_payload is None:
            additional_payload = {}
        payload = {
            'sub': user.id,
            'email': user.email,
            'phone': user.phone,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=72)
        }
        payload.update(additional_payload)
        return jwt.encode(payload, env.secret_key, algorithm=env.algorithm)

    @staticmethod
    def get_payload_from_token(token: str) -> dict:
        token = token.split(' ')[1]
        try:
            return jwt.decode(token, env.secret_key, algorithms=[env.algorithm])
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token is expired")
        except jwt.exceptions.DecodeError:
            raise HTTPException(status_code=401, detail="Incorrect token type")
