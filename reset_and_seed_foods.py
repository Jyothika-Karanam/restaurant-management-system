from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

# ⚠️ DELETE OLD DATA
deleted = foods.delete_many({})
print(f"🗑️ Deleted {deleted.deleted_count} old food items")

# ✅ FRESH DATA
food_items = [
    {"name": "Chicken Biryani","description": "Aromatic basmati rice with spicy chicken","price": 220,"image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"},
    {"name": "Veg Burger","description": "Crispy veg patty with fresh veggies","price": 120,"image": "https://images.unsplash.com/photo-1550547660-d9450f859349"},
    {"name": "Margherita Pizza","description": "Classic cheese pizza with tomato base","price": 200,"image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38"},
    {"name": "Masala Dosa","description": "South Indian dosa with potato filling","price": 90,"image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976"},
    {"name": "Paneer Butter Masala","description": "Paneer cubes in rich buttery gravy","price": 180,"image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"},
    {"name": "Fried Rice","description": "Indo-Chinese style vegetable fried rice","price": 140,"image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b"},
    {"name": "Hakka Noodles","description": "Stir fried noodles with veggies","price": 130,"image": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841"},
    {"name": "Chicken Lollipop","description": "Crispy deep fried chicken wings","price": 160,"image": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58"},
    {"name": "Gulab Jamun","description": "Soft milk-solid balls in sugar syrup","price": 80,"image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"},
    {"name": "Chocolate Milkshake","description": "Rich creamy chocolate shake","price": 110,"image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"}
]

foods.insert_many(food_items)

print("✅ Fresh food data inserted")
print("📦 Total foods now:", foods.count_documents({}))