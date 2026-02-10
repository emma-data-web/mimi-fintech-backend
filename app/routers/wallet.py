from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.wallet import WalletCreate
from app.services.wallet_services import create_wallet
from sqlalchemy.orm import Session



Wallet_router = APIRouter()

@Wallet_router.post("/create-wallet")
def wallet_creation(user: WalletCreate, db: Session = Depends(get_db)):

  create_wallet(user=user, db=db)