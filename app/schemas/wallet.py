from pydantic import BaseModel
from sqlalchemy import DateTime

class Transfer(BaseModel):
  user_id : int
  wallet_id : int
  sender_id : int
  sender_balance : float
  reciever_balance : float
  amount_being_transfered : float
  created_at : DateTime



class 