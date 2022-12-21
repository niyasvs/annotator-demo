from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Image = db.images
Project = db.projects
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Image.create_index([("id", pymongo.ASCENDING)], unique=True)
Project.create_index([("id", pymongo.ASCENDING)], unique=True)
