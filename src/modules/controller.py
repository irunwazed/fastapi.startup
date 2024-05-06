from src.core import BaseController


class Controller(BaseController):

  def __init__(self) -> None:
    super().__init__()

  def not_auth(self):
    return self.page_not_auth()

  def not_found(self):
    return self.page_not_found()