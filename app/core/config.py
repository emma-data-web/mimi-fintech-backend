from pydantic_settings import BaseSettings



class Settings(BaseSettings):
  DATABASE_URL : str
  SECRET_KEY: str
  JWT_ALGORITHM: str
  ACESS_TOKEN_EXPIRE_MINUTE: int = 30
  RESET_PASSWORD_TOKEN_EXPIRE_MINUTE: int = 5


  class Config:
    env_file = ".env"

    

Settings = Settings()