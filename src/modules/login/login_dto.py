from pydantic import BaseModel # type: ignore

class Token(BaseModel):
    access_token: str
    token_type: str

class RequestLogin(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    name: str | None = None
    username: str
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
