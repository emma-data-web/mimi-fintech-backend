from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.db.base import base
from datetime import datetime



class Transaction(base):
  __tablename__ = "transactions"

  id = Column(Integer, primary_key=True)
  wallet_id = Column(Integer, ForeignKey("wallets.id"))
  amount = Column(Float, nullable=False)
  type(credit/debit) = Column(String)
  status = Column(String)
  reference = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)


  wallet = relationship("Wallet", back_populates="transactions",uselist=False )