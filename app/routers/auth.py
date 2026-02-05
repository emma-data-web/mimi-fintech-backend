from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.user import CreateUser, CreateUserOut
from app.services.auth_services import create_user
from sqlalchemy.orm import Session


Auth_router = APIRouter()

Auth_router.post("/register")
def register_user(user: CreateUser, db: Session = Depends(get_db)):

  create_user(user=user, db=db)