from typing import Annotated
from fastapi import Request, Depends, FastAPI, APIRouter # type: ignore
# from fastapi.exceptions import RequestValidationError # type: ignore
# from fastapi.responses import PlainTextResponse, JSONResponse # type: ignore
# from starlette.exceptions import HTTPException as StarletteHTTPException  # type: ignore

from src.core.base_dto import ResponseMessage
from .beranda import BerandaController
from src.modules.login.login_dto import User
from src.libraries.token import TokenHandler
# from .controller import Controller

from .users.users_router import UsersRouter

from fastapi.security import APIKeyHeader
api_key_header = APIKeyHeader(name="X-API-Key")

def get_user():
  user = 'testing'
  print(user)
  return user


class ApiRouter():
  beranda_controller: BerandaController
  token_handler: TokenHandler
  def __init__(self, app: FastAPI) -> None:
    super().__init__()
    self.token_handler = TokenHandler()
    self.beranda_controller = BerandaController()
    router = APIRouter(prefix="/api")
    self._init_routes(router)
    app.include_router(router)

  def _init_routes(self, app: APIRouter) -> None:

    # app.include_router(prefix="/api/v1")
    @app.get("/beranda", responses={200: {"model": ResponseMessage}})
    def beranda(req: Request, user: dict = Depends(get_user)):
      return self.beranda_controller.beranda(req)
    
    # @app.get("/testing", responses={200: {"model": ResponseMessage}}, include_in_schema=True)
    # def testing(current_user: Annotated[User, Depends(self.token_handler.get_current_active_user)]):
    #   return self.beranda_controller.testing()


router = APIRouter()
    
@router.get("/")
async def get_testroute():
  return "OK"

