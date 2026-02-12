from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import base
from datetime import datetime


class User(base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  other_name = Column(String)
  email = Column(String, unique=True, index=True)
  harsed_password = Column(String)
  is_active = Column(Boolean, default =True)
  is_verified = Column(Boolean, default = False)
  is_admin = Column(Boolean, default = False)
  created_at = Column(DateTime, default = datetime.utcnow)


  wallet = relationship("Wallet", back_populates="user")