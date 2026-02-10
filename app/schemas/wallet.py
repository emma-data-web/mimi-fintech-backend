from pydantic import BaseModel
from sqlalchemy import DateTime
from uuid import UUID

class WalletCreate(BaseModel):
  user_id : int



