from app.models.wallet import Wallet
from app.models.user import User
from app.schemas.wallet import WalletCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException



def create_wallet(user: WalletCreate, db: Session):
  existing_wallet_owner = db.query(User).filter(User.id == user.user_id).first()

  