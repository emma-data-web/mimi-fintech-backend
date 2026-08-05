from app.core.security import create_access_token, harsh_password, verify_password
from app.models.user import User
from app.schemas.user import CreateUser, CreateUserOut, UserLogin, UserLoginResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select


async def create_user(user: CreateUser, db: AsyncSession):
  exiting_user = (await db.execute(select(User).where(User.email == user.email))).scalar_one_or_none()

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
  await db.commit()
  await db.refresh(new_user)
  return new_user




async def user_login(user: UserLogin, db: AsyncSession):
  existing_user = (await db.execute(select(User).where(User.email == user.email))).scalar_one_or_none()

  if not existing_user:
      raise HTTPException(status_code=401, detail="Invalid email or password")

  if not verify_password(user.password, existing_user.harsed_password):
      raise HTTPException(status_code=401, detail="Invalid email or password")

  
  access_token = create_access_token({"sub": str(existing_user.id)})

  return {
    "access_token" : access_token,
    "token_type" : "bearer" 
  }