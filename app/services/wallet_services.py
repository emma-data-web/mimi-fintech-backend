from app.models.wallet import Wallet
from app.models.user import User
from app.schemas.wallet import WalletCreate
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



