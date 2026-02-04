from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status
from passlib.context import CryptContext
from fastapi.security import HTTPBearer
from app.core.config import Settings


pwd_content = CryptContext(
  schemes=["bcrypt"],
  deprecated = "auto"
)


def harsh_password(password: str):
  return pwd_content.hash(password)


def verify_password(plain_password, harshed_password):
  return pwd_content.verify(plain_password, harshed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
  data_to_encode = data.copy()

  if expires_delta:
    expire = datetime.utcnow() + expires_delta

  else:
    expire = datetime.utcnow() + timedelta(minutes=Settings.ACESS_TOKEN_EXPIRE_MINUTE)

  data_to_encode.update({"exp": expire})


