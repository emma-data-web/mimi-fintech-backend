from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import base
from datetime import datetime
import uuid
from app.models.user import User
from app.models.transaction import Transaction

class Wallet(base):
  __tablename__ = "wallets"

  wallet_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  balance = Column(Float, nullable=False)
  currency = Column(String, default= "NGN")
  created_at = Column(DateTime, default=datetime.utcnow)


  user = relationship("User", back_populates="wallet")


  transactions = relationship("Transaction", back_populates="wallet")
