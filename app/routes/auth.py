# app/routes/auth.py

from fastapi import APIRouter, Depends
from models.user import User
from dependencies import authenticate_user

auth_router = APIRouter()

# root diplay hello world
@auth_router.get("/")
def read_root():
    return {"message": "Hello World"}

@auth_router.post("/register")
def register(user: User):
    # Add logic to register user
    return {"message": "User registered successfully"}

@auth_router.post("/login")
def login(username: str, password: str):
    # Add logic to authenticate user
    return {"token": "fake-jwt-token"}

@auth_router.put("/profile")
def update_profile(user: User, current_user: User = Depends(authenticate_user)):
    # Add logic to update user profile
    return {"message": "Profile updated successfully"}

@auth_router.put("/tags")
def update_tags(tags: list[str], current_user: User = Depends(authenticate_user)):
    # Add logic to update user tags
    return {"message": "Tags updated successfully"}
