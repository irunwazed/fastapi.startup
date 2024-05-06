from src.core import BaseController

from sqlalchemy.orm import Session

from .users_service import UsersService
from dataclasses import asdict
from fastapi.encoders import jsonable_encoder

class UsersController(BaseController):
  users_service: UsersService

  def __init__(self) -> None:
    super().__init__()
    self.users_service = UsersService()

  def create_users(self, db, user):
    db_user = self.users_service.get_user_by_username(db, username=user.username)
    if db_user:
      return self.response("User sudah ada!", False, [])
    return self.response("Berhasil mengambil data", True, jsonable_encoder(self.users_service.create_user(db=db,user=user)))
  
  def get_users(self, skip, limit, db):
    users = self.users_service.get_users(db,skip=skip,limit=limit)
    return self.response("Berhasil mengambil data", True, jsonable_encoder(users))
    # return users
  
  def get_user(self, db,user_id):
    db_user = self.users_service.get_user(db,user_id =user_id )
    if db_user is None:
      return self.response("User tidak ditemukan", False, [])
    return self.response("Berhasil mengambil data", True, jsonable_encoder(db_user))
    return db_user

    

  # def get_user(db: Session, user_id: int):
  #   return db.query(User).filter(User.id == user_id).first()

  # def get_user_by_email(db: Session, email: str):
  #   return db.query(User).filter(User.email == email).first()

  # def get_users(db: Session, skip:int=0, limit:int=100):
  #   # return db.query(User).offset(skip).limit(limit).all()
  #   return db.query(User).offset(skip).limit(limit).all()

  # def create_user(db: Session, user:UserCreate):
  #   db_user = User(email=user.email,
  #                         name=user.name)
  #   db.add(db_user)
  #   db.commit()
  #   db.refresh(db_user)
  #   return db_user
