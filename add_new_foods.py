from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

new_foods = [

{
"name": "Paneer Tikka",
"description": "Grilled paneer cubes with spices",
"price": 190,
"image": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0"
},

{
"name": "Butter Chicken",
"description": "Creamy tomato based chicken curry",
"price": 240,
"image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
},

{
"name": "Chole Bhature",
"description": "Spicy chole with fluffy bhature",
"price": 130,
"image": "https://images.unsplash.com/photo-1626132647523-66f5bf75d3b6"
},

{
"name": "Cold Coffee",
"description": "Chilled coffee with ice cream",
"price": 120,
"image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735"
},

{
"name": "White Sauce Pasta",
"description": "Creamy Italian pasta",
"price": 180,
"image": "https://images.unsplash.com/photo-1521389508051-d7ffb5dc8f70"
}

]

for food in new_foods:
    if not foods.find_one({"name": food["name"]}):
        foods.insert_one(food)
        print("✅ Added:", food["name"])
    else:
        print("⏩ Already exists:", food["name"])