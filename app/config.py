import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
from routers import datas, users

# Load env vars from .env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")


# MongoDB connection
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# App routers
app = FastAPI()
app.include_router(users.router, tags=['Users'])
app.include_router(datas.router, tags=['Data'])