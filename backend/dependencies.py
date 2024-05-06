from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from models.user import User
from typing import Optional
from pymongo import MongoClient



SECRET_KEY = "divakar"
ALGORITHM = "HS256"


from models.user import User

# MongoDB connection settings
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "fastblogger"
COLLECTION_NAME = "users"

# MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db[COLLECTION_NAME]
# Add logic to fetch user from the database using username
def get_user_from_database(username: str) -> Optional[User]:
    # Query the "users" collection for the specified username
    user_data = users_collection.find_one({"username": username})
    if user_data:
        # If user data exists, create a User object and return it
        return User(**user_data)
    else:
        # If user data doesn't exist, return None
        return None

def authenticate_user(token: str ):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        # Add logic to fetch user from the database using username
        user = get_user_from_database(username)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
