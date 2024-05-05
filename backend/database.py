from pymongo import MongoClient

from config import DB_NAME, DB_PASSWORD, DB_USERNAME, DB_HOST, DB_PORT


DB_URL = f"mongodb://localhost:27017/fastblogger"


client = MongoClient(DB_URL)
db = client[DB_NAME]

# Add logic to close the connection

def close_connection():
    client.close()
    print("Connection closed")


