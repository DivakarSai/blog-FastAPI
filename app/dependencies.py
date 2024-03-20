# app/dependencies.py

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(token: str = Depends(oauth2_scheme)):
    # Add logic to authenticate user using token
    # Example:
    # user = decode_token(token)
    # if not user:
    #     raise HTTPException(status_code=401, detail="Invalid credentials")
    # return user
    return User(username="example_user", email="user@example.com", password="password")
