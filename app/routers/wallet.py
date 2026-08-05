from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.wallet import WalletCreate
from app.services.wallet_services import create_wallet
from sqlalchemy.ext.asyncio import AsyncSession



Wallet_router = APIRouter()

@Wallet_router.post("/create-wallet")
async def wallet_creation(user: WalletCreate, db: AsyncSession = Depends(get_db)):

  await  create_wallet(user=user, db=db)

  