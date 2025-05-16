from pymongo import MongoClient
from .secret import DATABASE_URL

client = MongoClient(DATABASE_URL)

db = client.todo_db

# collections
TodoCollection = db["todos"]