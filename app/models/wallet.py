from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import base
from datetime import datetime



class Wallet(base):
  __table_name__ = "wallets"

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  balance = Column(Float, nullable=False)
  currency = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)

  transactions = relationship("Transaction", back_populates="wallets", uselist=False)
