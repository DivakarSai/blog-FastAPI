
from pymongo import MongoClient

from config import get_settings

settings = get_settings()

DB_URL = f"mongodb://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@localhost:27017/{settings.DB_NAME}"

# Add logic to connect to MongoDB

client = MongoClient(DB_URL)
db = client[settings.DB_NAME]

# Add logic to close the connection

def close_connection():
    client.close()
    print("Connection closed")


