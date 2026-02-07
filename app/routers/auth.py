from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.user import CreateUser, CreateUserOut, UserLogin,UserLoginResponse
from app.services.auth_services import create_user, user_login
from sqlalchemy.orm import Session


Auth_router = APIRouter()

@Auth_router.post("/register")
def register_user(user: CreateUser, db: Session = Depends(get_db)):

  create_user(user=user, db=db)


@Auth_router.post("/login", response_model=UserLoginResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):

  return user_login(user=user, db=db)

