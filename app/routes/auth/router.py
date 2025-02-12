from fastapi import APIRouter
from .login import router_login
from .logout import router_logout
from .register import router_register
from .user_data import router_user_data

router = APIRouter(prefix='/auth', tags=['Auth'])
router.include_router(router_login)
router.include_router(router_logout)
router.include_router(router_register)
router.include_router(router_user_data)