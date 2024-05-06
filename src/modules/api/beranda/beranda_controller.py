from fastapi import FastAPI, Request, Response # type: ignore
from src.core import BaseController

class BerandaController(BaseController):
  def __init__(self) -> None:
    super().__init__()

  def beranda(self, req: Request):
    print(req.state.user)
    return self.response("Berhasil", True, [])

  def testing(self):
    return self.response("Berhasil Testing", True, [])