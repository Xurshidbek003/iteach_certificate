from fastapi import APIRouter
from routes.login import login_router
from routes.users import users_router
from routes.certificate import certificate_router


api = APIRouter()

api.include_router(certificate_router)
api.include_router(users_router)
api.include_router(login_router)
