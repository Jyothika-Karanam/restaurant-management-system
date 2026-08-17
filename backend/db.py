from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["restaurant"]
foods = db["foods"]

foods = db["foods"]
orders = db["orders"]
reviews = db["reviews"]
users = db["users"]


# ================= ADMIN CONFIG =================
ADMIN_EMAIL = "youradminemail@gmail.com"   # 🔴 change this
ADMIN_PASSWORD = "admin123"                # 🔴 change this


# ---------------- FOOD ----------------
def get_all_foods():
    return list(foods.find())


# ---------------- ORDER ----------------
def insert_order(data):
    data["date"] = datetime.now().date().isoformat()
    return orders.insert_one(data).inserted_id


def get_user_orders(email):
    return list(orders.find({"email": email}))


# ---------------- REVIEW ----------------
def insert_review(data):
    return reviews.insert_one(data)


# ---------------- DASHBOARD ----------------
def get_orders_today():
    today = datetime.now().date().isoformat()
    return orders.count_documents({"date": today})


def get_all_orders():
    return list(orders.find())


def get_all_reviews():
    return list(reviews.find())


# ================= AUTH =================

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


# ================= FAVORITES =================

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