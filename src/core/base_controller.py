from dataclasses import asdict, make_dataclass
from fastapi.responses import JSONResponse
from .base_dto import ResponseMessage, ResponseLoginFailure, ResponseLoginSuccess, ResponseNotFound, ResponseNotAuth
from .base_dto import Token
from fastapi import status
# from src.libraries.classes import ClassessHandler
# from ..libraries.classes import ClassessHandler

class BaseController():
  # classes_handler: ClassessHandler
  def __init__(self) -> None:
    super().__init__()
    # self.classes_handler = ClassessHandler()

  def generate_class(self, MyClass):
    return make_dataclass("ResponData", [('message', str), ("status", bool), ("data", MyClass)])
  
  def respon_data(self, MyClass, message: str, status: bool, data: dict = None):
    response = self.generate_class(MyClass)(message=message, status=status, data=data)
    return JSONResponse(asdict(response))

  def response(self, message: str, status: bool, data: dict = None) -> JSONResponse:
    # response = self.classes_handler.ResponData(dict)(message=message, status=status, data=data) #
    # response = self.generate_class(dict)(message=message, status=status, data=data)
    response = ResponseMessage(message=message, status=status, data=data)
    return JSONResponse(asdict(response))
  
  def get_token(self, access_token: str, token_type: str) -> JSONResponse:
    response = Token(access_token=access_token, token_type=token_type)
    return JSONResponse(status_code=200, content=asdict(response))
  
  def login_success(self, message: str, access_token: str, token_type: str) -> JSONResponse:
    response = ResponseLoginSuccess(message=message, status=True, data=Token(access_token=access_token, token_type=token_type))
    return JSONResponse(status_code=200, content=asdict(response))
  
  def login_failure(self, message: str) -> JSONResponse:
    response = ResponseLoginFailure(message=message, status=False)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=asdict(response))
  
  def page_not_found(self) -> JSONResponse:
    response = ResponseNotFound(message="Page Not Found", status=False)
    return JSONResponse(status_code=404, content=asdict(response))
  
  def page_not_auth(self) -> JSONResponse:
    response = ResponseNotAuth(message="Page Not Auth", status=False)
    return JSONResponse(status_code=401, content=asdict(response))