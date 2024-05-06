from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from typing import Annotated
from jose import JWTError, jwt
from src.modules.login.login_dto import User, UserInDB, TokenData
from databases.fakeDB import fake_users_db

from src.configs.config import  ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(self, plain_password, hashed_password):
      return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
      return self.pwd_context.hash(password)

    def get_user(self, db, username: str):
      print("get_user")
      print(username)
      if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


    def authenticate_user(self, fake_db, username: str, password: str):
      user = self.get_user(fake_db, username)
      if not user:
        return False
      if not self.verify_password(password, user.hashed_password):
        return False
      return user


    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
      to_encode = data.copy()
      if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
      else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
      to_encode.update({"exp": expire})
      encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
      return encoded_jwt


    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
      credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
      )
      try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
          raise credentials_exception
        token_data = TokenData(username=username)
      except JWTError:
        raise credentials_exception
      user = None


      if username in fake_users_db:
        user_dict = fake_users_db[username]
        user = UserInDB(**user_dict)
      # user = self.get_user(fake_users_db, str(token_data.username))
      if user is None:
        raise credentials_exception
      return user


    async def get_current_active_user(self,
      current_user: Annotated[User, Depends(get_current_user)],
    ):
      if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
      return current_user