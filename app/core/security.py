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


  encode_jwt = jwt.encode(
    data_to_encode,
    Settings.SECRET_KEY,
    Settings.JWT_ALGORITHM
  )

  return encode_jwt


def decode_access_token(token: str):
  credentials_exception = HTTPException(

  status_code=status.HTTP_401_UNAUTHORIZED,
  detail="Could not validate credentials",
   headers={"WWW-Authenticate": "Bearer"},

  )

  try:

    payload = jwt.decode(

      token=token,
      key=Settings.SECRET_KEY,
      algorithms=[Settings.JWT_ALGORITHM]

    )

    user_id : str = payload.get("sub")

    if user_id is None:
      raise credentials_exception
    else:
      return payload
    
  except JWTError:

    raise credentials_exception
  


def reset_password_access_token(data: dict, expires_delta: timedelta | None = None):
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        
        expire = datetime.utcnow() + timedelta(minutes=Settings.RESET_PASSWORD_TOKEN_EXPIRE_MINUTE)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode, 
        Settings.SECRET_KEY, 
        algorithm=Settings.JWT_ALGORITHM
    )
    return encoded_jwt


def create_password_reset_token(user_id: int) -> str:
  
    to_encode = {"sub": str(user_id), "scope": "password_reset"}
    
    
    expires_delta = timedelta(minutes=Settings.RESET_PASSWORD_TOKEN_EXPIRE_MINUTE)
    
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, Settings.SECRET_KEY, algorithm=Settings.JWT_ALGORITHM)
    return encoded_jwt





bearer_scheme = HTTPBearer()