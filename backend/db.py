from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
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
    raise RuntimeError("MONGO_URI is not configured")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("✅ MongoDB connection successful")
except Exception as e:
    raise RuntimeError(f"❌ MongoDB connection failed: {e}")

db = client["restaurant_db"]

foods = db["foods"]
orders = db["orders"]
reviews = db["reviews"]
users = db["users"]


# ================= ADMIN CONFIG =================
ADMIN_EMAIL = "23091a3255@rgmcet.edu.in.com"
ADMIN_PASSWORD = "CHANGE_THIS_PASSWORD"


# ---------------- FOOD ----------------
def get_all_foods():
    return list(foods.find())


# ---------------- ORDER ----------------
def insert_order(data):
    data["date"] = datetime.now().date().isoformat()

    result = orders.insert_one(data)

    if result.acknowledged:
        print(f"✅ Order stored successfully: {result.inserted_id}")
        return result.inserted_id

    raise RuntimeError("Order insertion was not acknowledged by MongoDB")


def get_user_orders(email):
    return list(orders.find({"user_email": email}))


def get_orders_today():
    today = datetime.now().date().isoformat()
    return orders.count_documents({"date": today})


def get_all_orders():
    return list(orders.find())


# ---------------- REVIEW ----------------
def insert_review(data):
    result = reviews.insert_one(data)

    if result.acknowledged:
        print(f"✅ Review stored successfully: {result.inserted_id}")
        return result

    raise RuntimeError("Review insertion was not acknowledged by MongoDB")


def get_all_reviews():
    return list(reviews.find())


# ---------------- AUTH ----------------
def get_user(email):
    return users.find_one({"email": email})


def create_user(email):
    role = "admin" if email == ADMIN_EMAIL else "customer"

    user = {
        "email": email,
        "created_at": datetime.now(),
        "role": role,
        "favorites": []
    }

    return users.insert_one(user)


def verify_admin(email, password):
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        return True
    return False


def get_user_role(email):
    user = users.find_one({"email": email})

    if user:
        return user.get("role", "customer")

    return "customer"


# ---------------- FAVORITES ----------------
def add_favorite(email, food_id):
    return users.update_one(
        {"email": email},
        {"$addToSet": {"favorites": str(food_id)}}
    )


def remove_favorite(email, food_id):
    return users.update_one(
        {"email": email},
        {"$pull": {"favorites": str(food_id)}}
    )


def get_user_favorites(email):
    user = users.find_one({"email": email})

    if user and "favorites" in user:
        return user["favorites"]

    return []