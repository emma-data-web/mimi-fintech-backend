from app.core.security import create_access_token, harsh_password, verify_password
from app.models.user import User
from app.schemas.user import CreateUser, CreateUserOut, UserLogin, UserLoginResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_user(user: CreateUser, db: Session):
  exiting_user = db.query(User).filter(User.email == user.email).first()

  if exiting_user:
    raise HTTPException(status_code=400, detail="user alreeady exists")
  
  harsh_pswd = harsh_password(user.password)
  

  new_user = User(
    first_name = user.first_name,
    last_name = user.last_name,
    other_name = user.other_name,
    email = user.email,
    harsed_password = harsh_pswd
  )


  db.add(new_user)
  db.commit()
  db.refresh(new_user)




def user_login(user: UserLogin, db: Session):
  existing_user = db.query(User).filter(User.email == user.email).first()

  if not existing_user:
      raise HTTPException(status_code=401, detail="Invalid email or password")

  if not verify_password(user.password, existing_user.harsed_password):
      raise HTTPException(status_code=401, detail="Invalid email or password")

  
  access_token = create_access_token({"sub": str(existing_user.id)})

  return {
    "access_token" : access_token,
    "token_type" : "bearer" 
  }