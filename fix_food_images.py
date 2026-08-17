from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

# ✅ canonical image dataset
image_map = {
    "chicken biryani": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f",
    "veg burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
    "margherita pizza": "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3",
    "masala dosa": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc",
    "paneer butter masala": "https://images.unsplash.com/photo-1631452180539-96aca7d48617",
    "fried rice": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
    "hakka noodles": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841",
    "gulab jamun": "https://images.unsplash.com/photo-1590080877777-9e6b3b9f1f8f",
    "samosa": "https://images.unsplash.com/photo-1601050690597-df0568f70950",
    "chocolate milkshake": "https://images.unsplash.com/photo-1572490122747-3968b75cc699",
    "french fries": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5",
    "vanilla ice cream": "https://images.unsplash.com/photo-1563805042-7684c019e1cb",
}

updated = 0

for food in foods.find():

    db_name = food["name"].strip().lower()

    if db_name in image_map:
        result = foods.update_one(
            {"_id": food["_id"]},
            {"$set": {"image": image_map[db_name]}}
        )

        if result.modified_count:
            updated += 1

print(f"✅ {updated} food images corrected automatically")