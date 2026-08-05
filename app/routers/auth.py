from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.user import CreateUser, CreateUserOut, UserLogin,UserLoginResponse
from app.services.auth_services import create_user, user_login
from sqlalchemy.ext.asyncio import AsyncSession

Auth_router = APIRouter()

@Auth_router.post("/register")
async def register_user(user: CreateUser, db: AsyncSession = Depends(get_db)):

  return await create_user(user=user, db=db)


@Auth_router.post("/login", response_model=UserLoginResponse)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):

  return await user_login(user=user, db=db)

