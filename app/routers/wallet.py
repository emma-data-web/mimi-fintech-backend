from fastapi import APIRouter, Depends
from app.dependecies import get_db
from app.schemas.wallet import WalletCreate, CreditWallet,DebitWallet
from app.services.wallet_services import create_wallet, credit_wallet, debit_wallet
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.security import get_current_user

Wallet_router = APIRouter()

@Wallet_router.post("/create-wallet")
async def wallet_creation(user: WalletCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):

  await  create_wallet(user=user, db=db, current_user=current_user)


@Wallet_router.post("/credit-wallet")
async def  crediting_wallet(user: CreditWallet, db:AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
  return await credit_wallet(user=user,db=db,current_user=current_user)


@Wallet_router.post("/debit-wallet")
async def  crediting_wallet(user: DebitWallet, db:AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
  return await debit_wallet(user=user,db=db,current_user=current_user)