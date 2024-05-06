from sqlalchemy import Boolean, Column, ForeignKey, Integer, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore

# from sqlalchemy.ext.declarative import declarative_base # type: ignore
# Base = declarative_base()
from src.core.base_model import Base
from src.configs.database import engine

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255))
  username = Column(String(255), unique=True, index=True)
  password = Column(String(255))
  role = Column(String(50))
  # todos = relationship("Todo", back_populates="owner")
  is_active = Column(Boolean,default=False)

# create DB
Base.metadata.create_all(bind=engine)