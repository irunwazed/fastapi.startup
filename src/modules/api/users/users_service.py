from sqlalchemy.orm import Session

from .users_model import User
from .users_dto import UserCreate

class UsersService:
  def get_user(self, db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

  def get_user_by_username(self, db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

  def get_users(self, db: Session, skip:int=0, limit:int=100):
    # return db.query(User).offset(skip).limit(limit).all()
    return db.query(User).offset(skip).limit(limit).all()

  def create_user(self, db: Session, user:UserCreate):
    db_user = User(username=user.username,  password=user.password, role="admin",
                          name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user