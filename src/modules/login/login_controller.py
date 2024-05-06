from src.core import BaseController

from .login_dto import RequestLogin
from .login_service import LoginService


class LoginController(BaseController):
  login_service: LoginService

  def __init__(self) -> None:
    super().__init__()
    self.login_service = LoginService()

  def login(self, req: RequestLogin):
    check_user = self.login_service.check_user(req)
    if check_user["status"] == False:
      return self.login_failure("Incorrect username or password")
    return self.login_success("Berhasil", check_user["access_token"], check_user["token_type"]) 

  def token(self, req: RequestLogin):
    check_user = self.login_service.check_user(req)
    if check_user["status"] == False:
      return self.login_failure("Incorrect username or password")
    return self.get_token(check_user["access_token"], check_user["token_type"])
  
  
  