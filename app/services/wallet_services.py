from app.models.wallet import Wallet
from app.models.user import User
from app.schemas.wallet import WalletCreate, CreditWallet, DebitWallet
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from sqlalchemy import select
from app.core.security import get_current_user



async def create_wallet(user: WalletCreate, db: AsyncSession, current_user: User = Depends(get_current_user)):
  existing_wallet_owner = (await db.execute(select(User).where(User.id == user.user_id))).scalar_one_or_none()


  if not existing_wallet_owner:
    raise HTTPException(status_code=401, detail="user not found")

  if user.user_id != current_user.id:
    raise HTTPException(status_code=403, details="not authorized")
  
  new_wallet = Wallet(
    user_id = user.user_id,
    balance = 0.00
  ) 


  db.add(new_wallet)
  await db.commit()
  await db.refresh(new_wallet)


  return new_wallet


async def credit_wallet(user: CreditWallet, db: AsyncSession, current_user: User = Depends(get_current_user)):
  existing_user =(await db.execute(select(User).where(User.id == user.user_id))).scalar_one_or_none()

  existing_wallet = (await db.execute(select(Wallet).where(Wallet.wallet_id == user.wallet_id))).scalar_one_or_none()

  if not existing_user:
    raise HTTPException(status_code=404, detail="User not found!")
  
  if not existing_wallet:
    raise HTTPException(status_code=404, detail="wallet does not exist")

  if user.user_id != current_user.id:
    raise HTTPException(status_code=403, detail="not allowed")
  
  if user.amount <= 0:
    raise HTTPException(status_code=400, detail="you must have more than zero balance")
  
  if existing_wallet.user_id != user.user_id:
    raise HTTPException(status_code=400, detail="wallet does not belong to user")
  
  existing_wallet.balance += user.amount


  await db.commit()
  await db.refresh(existing_wallet)

  return existing_wallet


async def debit_wallet(user: DebitWallet, db: AsyncSession):
  existing_user = (await db.execute(select(User).where(User.id == user.user_id))).scalar_one_or_none()

  existing_wallet = (await db.execute(select(Wallet).where(Wallet.wallet_id == user.wallet_id))).scalar_one_or_none()

  if not existing_user: 
    raise HTTPException(status_code=404, detail="user not found")
  
  if not existing_wallet:
    raise HTTPException(status_code=404, detail="wallet does not exist")
  
  if existing_wallet.balance <= user.amount_to_be_transfered:
    raise HTTPException(status_code=403, detail="insufficient balance!")
  
  existing_wallet.balance -= user.amount_to_be_transfered

  await db.commit()
  await db.refresh()
