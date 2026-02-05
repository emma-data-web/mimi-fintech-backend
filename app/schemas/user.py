from pydantic import BaseModel, EmailStr
#from datetime import datetime


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