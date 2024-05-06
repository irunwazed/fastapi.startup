
from .login_dto import RequestLogin
from databases.fakeDB import fake_users_db
from datetime import datetime, timedelta, timezone
from src.libraries.token import TokenHandler 
from src.configs.config import ACCESS_TOKEN_EXPIRE_MINUTES

class LoginService:
  token_handler: TokenHandler
  def __init__(self) -> None:
    super().__init__()
    self.token_handler = TokenHandler()
    # pass

  def check_user(self, req: RequestLogin):
    user = self.token_handler.authenticate_user(fake_users_db, req.username, req.password)
    if not user:
      return { "status": False }
      # return self.login_failure("Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = self.token_handler.create_access_token(
      data={
        "sub": user.username
      }, 
      expires_delta=access_token_expires
    )
    return {
      "status": True,
      "access_token": access_token,
      "token_type": "Bearer"
    } 