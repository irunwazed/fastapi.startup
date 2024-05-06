
from dataclasses import asdict, dataclass, make_dataclass
from jose import JWTError, jwt
from datetime import datetime, timezone, timedelta
from src.configs.config import  ALGORITHM, SECRET_KEY

class UtilsHandler:
  def __init__(self) -> None:
    pass

  def ResponData(self, MyClass):
    return make_dataclass("ResponUser", [('message', str), ("status", bool), ("data", MyClass)])
  
  def verify_password(self, plain_password, hashed_password):
    return self.pwd_context.verify(plain_password, hashed_password)

  def get_password_hash(self, password):
    return self.pwd_context.hash(password)
  
  def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
      expire = datetime.now(timezone.utc) + expires_delta
    else:
      expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
  
  def get_payload_token(self, token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    