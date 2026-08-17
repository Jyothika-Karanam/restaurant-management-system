from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

print("🍽️ Total food items in DB =", foods.count_documents({}))