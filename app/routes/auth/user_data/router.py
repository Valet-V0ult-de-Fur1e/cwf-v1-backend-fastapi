from fastapi import APIRouter, Depends
from app.db.models.user.model import UserModel
from app.routes.utils import get_current_user

router = APIRouter()

@router.get("/user_data/")
async def get_user_data(user_data: UserModel = Depends(get_current_user)):
    return user_data