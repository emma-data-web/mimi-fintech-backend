from app.models.wallet import Wallet
from app.models.user import User
from app.schemas.wallet import WalletCreate, CreditWallet
from sqlalchemy.orm import Session
from fastapi import HTTPException



def create_wallet(user: WalletCreate, db: Session):
  existing_wallet_owner = db.query(User).filter(User.id == user.user_id).first()

  if not existing_wallet_owner:
    raise HTTPException(status_code=401, detail="user not found")
  
  new_wallet = Wallet(
    user_id = user.user_id,
    balance = 0.00
  ) 


  db.add(new_wallet)
  db.commit()
  db.refresh(new_wallet)


  return new_wallet


def credit_wallet(user: CreditWallet, db: Session):
  existing_user = db.query(User).filter(User.id == user.user_id).first()

  existing_wallet = db.query(Wallet).filter(Wallet.wallet_id == user.wallet_id).first()

  if not existing_user:
    raise HTTPException(status_code=404, detail="User not found!")
  
  if not existing_wallet:
    raise HTTPException(status_code=404, detail="wallet does not exist")
  
  if user.amount <= 0:
    raise HTTPException(status_code=400, detail="you must have more than zero balance")
  
  if existing_wallet.user_id != user.user_id:
    raise HTTPException(status_code=400, detail="wallet does not belong to user")
  
  existing_wallet.balance += user.amount


  db.commit()
  db.refresh(existing_wallet)

  return existing_wallet