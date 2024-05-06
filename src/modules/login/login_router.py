from fastapi import Depends, FastAPI # type: ignore
from src.core.base_dto import ResponseMessage, ResponseLoginFailure, ResponseLoginSuccess, Token
from .login_dto import RequestLogin
from fastapi.requests import Request # type: ignore
from .login_controller import LoginController
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class LoginRouter():
  auth_controller: LoginController
  def __init__(self, app: FastAPI) -> None:
    super().__init__()
    self.auth_controller = LoginController()
    self._init_routes(app)

  def _init_routes(self, app: FastAPI) -> None:
    @app.post("/login", responses={200: {"model": ResponseLoginSuccess}, 401: {"model": ResponseLoginFailure}})
    def login(request: RequestLogin):
      return self.auth_controller.login(request)
    
    @app.post("/token", responses={200: {"model": Token}, 401: {"model": ResponseLoginFailure}}, include_in_schema=False)
    def token(form_data: OAuth2PasswordRequestForm = Depends()):
      return self.auth_controller.token(form_data)
