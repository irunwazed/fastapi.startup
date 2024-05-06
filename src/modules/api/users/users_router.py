from fastapi import Depends, FastAPI, APIRouter # type: ignore

from .users_dto import UserCreate, User
from .users_controller import UsersController
from src.configs.database import get_db
from sqlalchemy.orm import Session
from src.core.base_dto import ResponseDataMessage
from dataclasses import asdict, dataclass, make_dataclass

# from src.libraries.classes import ClassessHandler

class UsersRouter():
  users_controller: UsersController

  def __init__(self, app: FastAPI) -> None:
    super().__init__()
    self.users_controller = UsersController()
    router = APIRouter(prefix="/api")
    self._init_routes(router)
    app.include_router(router)

  def _init_routes(self, app: APIRouter) -> None:
    @app.post("/users/",response_model=User)
    def post_user(user:UserCreate, db:Session=Depends(get_db)):
      return self.users_controller.create_users(db, user)

    @app.get("/users/", response_model=list[User])
    def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
      return self.users_controller.get_users(skip, limit, db)
