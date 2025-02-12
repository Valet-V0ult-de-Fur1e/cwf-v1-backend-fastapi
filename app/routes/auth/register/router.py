from app.db.models.user.interface import UserInterFace
from app.routes.auth.register.schema import SUserRegister
from app.routes.exceptions import *
from app.routes.utils import get_password_hash
from fastapi import APIRouter

router = APIRouter()

@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UserInterFace.find_one_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExistsException
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserInterFace.add(**user_dict)
    return {'message': 'user register success'}