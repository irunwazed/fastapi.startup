from fastapi import FastAPI # type: ignore
from fastapi.exceptions import RequestValidationError # type: ignore
from fastapi.responses import PlainTextResponse, JSONResponse # type: ignore
from starlette.exceptions import HTTPException as StarletteHTTPException  # type: ignore

from src.core.base_dto import ResponseMessage
from .controller import Controller

class Router():
  controller: Controller
  def __init__(self, app: FastAPI) -> None:
    super().__init__()
    self._init_routes(app)
    self.controller = Controller()

  def _init_routes(self, app: FastAPI) -> None:
    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
      return self.controller.page_not_found()

    # @app.exception_handler(RequestValidationError)
    # async def validation_exception_handler(request, exc):
    #   return PlainTextResponse(str(exc), status_code=400)


