from sqlalchemy.orm import Session

import models
import schemas

User = models.User
Todo = models.Todo

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip:int=0, limit:int=100):
    # return db.query(User).offset(skip).limit(limit).all()
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user:schemas.UserCreate):
    db_user = User(email=user.email,
                          name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_todos(db: Session, skip:int=0, limit: int=100):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_user_todo(db:Session, todo:schemas.TodoCreate, user_id : int):
    db_todo = Todo(**todo.model_dump(),owner_id=user_id )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo