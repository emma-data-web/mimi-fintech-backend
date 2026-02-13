from pydantic import BaseModel
from sqlalchemy import DateTime


class WalletCreate(BaseModel):
  user_id : int


class CreditWallet(BaseModel):
  user_id : int
  wallet_id : str
  balance: float
  amount: float


class DebitWallet(BaseModel):
  user_id : int
  wallet_id : str
  balance : float
  amount_to_be_transfered: float
  reciever_wallet : str
  reciever_wallet_balance: float
