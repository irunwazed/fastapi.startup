# from typing import Annotated
from fastapi import Depends, FastAPI # type: ignore
# from fastapi.responses import JSONResponse # type: ignore
from src.middlewares import cors_middleware, AuthMiddleware
from fastapi.security import APIKeyHeader # type: ignore
from fastapi.security import OAuth2PasswordBearer # type: ignore

# from src.modules.login.login_dto import User
# from src.libraries.token import TokenHandler


app = FastAPI()
# private = FastAPI(docs_url=None, redoc_url=None)
# api = FastAPI()

header_scheme = APIKeyHeader(name="x-key")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

cors_middleware(app=app)

from src.modules.login import LoginRouter
from src.modules.router import Router
from src.modules.api.api_router import ApiRouter, UsersRouter, router
# from src.modules.api.users.users_router import UsersRouter


def get_user():
  user = 'testing2'
  print(user)
  return user

Router(app)
LoginRouter(app)
UsersRouter(app)

app.include_router(
  router,
  prefix="/api/tes",
  dependencies=[Depends(get_user)]
)

ApiRouter(app)
# AuthMiddleware(api)
AuthMiddleware(app)



# token_handler = TokenHandler()

# app.mount("/api", api)
# app.mount("/private", private)

# @app.get("/items/{item_id}")
# async def read_item( current_user: Annotated[User, Depends(token_handler.get_current_active_user)], item_id: int, q: Annotated[str, None] = None):
#   return {"item_id": item_id, "q": q, "token": current_user}