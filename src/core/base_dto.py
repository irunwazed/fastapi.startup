from dataclasses import dataclass

@dataclass
class ResponseMessage:
  status: bool
  message: str
  data: dict

@dataclass
class ResponseDataMessage:
  status: bool
  message: str
  data: list[dict]

@dataclass
class ResponseNotFound:
  status: bool
  message: str


@dataclass
class ResponseNotAuth:
  status: bool
  message: str


@dataclass
class ResponseLoginFailure:
  status: bool
  message: str


@dataclass
class Token:
  access_token: str
  token_type: str

@dataclass
class ResponseLoginSuccess:
  status: bool
  message: str
  data: Token


