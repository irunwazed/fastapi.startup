from fastapi import FastAPI, Request, Response # type: ignore
from src.modules.controller import Controller
from src.libraries.utils import UtilsHandler


class AuthMiddleware:
  controller: Controller
  utils_handler: UtilsHandler
  def __init__(self, server: FastAPI) -> None:
    self.controller = Controller()
    self.utils_handler = UtilsHandler()
    self._add_auth_middleware(server)

  def _add_auth_middleware(self, app: FastAPI):
    @app.middleware("http")
    async def middleware(req: Request, call_back):
      token = ""
      response: Response
      # print(req.headers['Authorization'])

      except_path = [
        '', '/docs', '/openapi.json', '/token', '/login'
      ]

      if any(path == req.url.path for path in except_path):
        response = await call_back(req)
        return response

      

      status = True
      if status:
        req.state.user = {
          "id": "asdasd",
          "username": "admin"
        }
        print("req.state.user")
        print(req.state.user)
        response = await call_back(req)
      else:
        response = self.controller.page_not_auth()
      return response
