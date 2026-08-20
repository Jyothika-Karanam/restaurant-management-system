from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    try:
        MONGO_URI = st.secrets["MONGO_URI"]
    except Exception:
        MONGO_URI = None

if not MONGO_URI:
    raise RuntimeError("MONGO_URI is missing")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
except Exception as e:
    raise RuntimeError(f"MongoDB connection failed: {e}")

db = client["restaurant_db"]

foods = db["foods"]
orders = db["orders"]
reviews = db["reviews"]
users = db["users"]