from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

# ✅ your correct 10 foods
valid_food_names = [
    "Chicken Biryani",
    "Veg Burger",
    "Margherita Pizza",
    "Masala Dosa",
    "Paneer Butter Masala",
    "Fried Rice",
    "Hakka Noodles",
    "Chicken Lollipop",
    "Gulab Jamun",
    "Chocolate Milkshake"
]

# ❌ delete everything else
result = foods.delete_many({
    "name": {"$nin": valid_food_names}
})

print("🗑 Deleted extra foods =", result.deleted_count)
print("✅ Remaining foods =", foods.count_documents({}))