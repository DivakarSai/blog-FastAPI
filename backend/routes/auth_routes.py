from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from database import db
from passlib.context import CryptContext
from datetime import datetime, timedelta, UTC
from pydantic import BaseModel
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dependencies import authenticate_user

auth_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "divakar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    username: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(UTC)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@auth_router.get("/")
def read_root():
    return {"message": "Hello World"}

@auth_router.post("/register")
async def register(user_data: User):
    try:
        users_collection = db["users"]
        existing_user = users_collection.find_one({"$or": [{"username": user_data.username}, {"email": user_data.email}]})
        if existing_user:
            raise HTTPException(status_code=400, detail="Username or email already exists")

        # Hash the password before storing
        hashed_password = pwd_context.hash(user_data.password)
        new_user = user_data.model_dump()
        new_user["password"] = hashed_password
        result = users_collection.insert_one(new_user)

        return {"message": "User registered successfully", "user_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@auth_router.post("/login", response_model=AccessToken)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        users_collection = db["users"]
        existing_user = users_collection.find_one({"username": form_data.username})
        if not existing_user or not pwd_context.verify(form_data.password, existing_user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# @auth_router.put("/profile")
# def update_profile(user: User, current_user: User = Depends(authenticate_user)):
#     # Add logic to update user profile
#     return {"message": "Profile updated successfully"}

# @auth_router.put("/tags")
# def update_tags(tags: list[str], current_user: User = Depends(authenticate_user)):
#     try:
#         users_collection = db["users"]
#         users_collection.update_one({"username": current_user.username}, {"$set": {"tags": tags}})
#         return {"message": "Tags updated successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")
