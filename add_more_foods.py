from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

# ✅ NEW REAL FOOD ITEMS (ADD MORE LIKE THIS)
new_foods = [

{
"name": "Hyderabadi Chicken Biryani",
"description": "Authentic dum biryani with rich spices",
"price": 240,
"image": "https://images.unsplash.com/photo-1633945274405-b6c8069047b9"
},

{
"name": "Paneer Tikka",
"description": "Grilled paneer cubes with spices",
"price": 190,
"image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
},

{
"name": "Butter Chicken",
"description": "Creamy tomato based chicken curry",
"price": 210,
"image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
},

{
"name": "Veg Spring Rolls",
"description": "Crispy rolls stuffed with veggies",
"price": 130,
"image": "https://images.unsplash.com/photo-1604908176997-4313d5c3b6a5"
},

{
"name": "Tandoori Chicken",
"description": "Smoky grilled chicken with spices",
"price": 260,
"image": "https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"
}

]

# ✅ INSERT ONLY IF NOT ALREADY PRESENT
for food in new_foods:
    existing = foods.find_one({"name": food["name"]})

    if not existing:
        foods.insert_one(food)
        print(f"✅ Added: {food['name']}")
    else:
        print(f"⚠️ Skipped (already exists): {food['name']}")

print("🎉 Done")