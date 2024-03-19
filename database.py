
from pymongo import MongoClient

# Add logic to connect to MongoDB

client = MongoClient("mongodb://localhost:27017/")
db = client["blog_database"]
