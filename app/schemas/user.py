from pydantic import BaseModel, EmailStr



class CreateUser(BaseModel):
  first_name : str
  last_name : str
  other_name : str
  email : EmailStr
  password : str

  class Config:
    orm_mode = True



class CreateUserOut(BaseModel):
  id : int
  email: EmailStr



class UserLogin(BaseModel):
  email : EmailStr
  password : str


class UserLoginResponse(BaseModel):
  access_token: str
  token_type: str = "bearer"
