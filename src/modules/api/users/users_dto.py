from pydantic import BaseModel # type: ignore

class TodoBase(BaseModel):
  title : str
  description : str | None = None


class TodoCreate(TodoBase):
  pass


class Todo(TodoBase):
  id : int
  owner_id  : int

  class Config:
    orm_mode = True


class UserBase(BaseModel):
  name: str
  username: str
  password: str


class UserCreate(UserBase):
  pass 


class User(UserBase):
  id : int
  is_active : bool
  todos : list[Todo] = []

  class Config:
    orm_model = True