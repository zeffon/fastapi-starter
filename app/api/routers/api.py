from fastapi import APIRouter
from app.api.routers.user import user_router

router = APIRouter(prefix="/api")

router.include_router(user_router)
