
from dataclasses import make_dataclass

class ClassessHandler:
  def __init__(self) -> None:
    pass

  def ResponData(self, MyClass):
    return make_dataclass("ResponUser", [('message', str), ("status", bool), ("data", MyClass)])