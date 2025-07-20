from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo import ASCENDING
import os

load_dotenv()  # Load from .env file

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["ecommerce_db"]

products_collection = db["products"]
orders_collection = db["orders"]
