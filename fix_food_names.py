from backend.db import foods

# 🔥 KEYWORDS IN IMAGE URL → CORRECT FOOD NAME
food_map = {

    "biryani": "Chicken Biryani",
    "burger": "Veg Burger",
    "pizza": "Margherita Pizza",
    "dosa": "Masala Dosa",
    "paneer": "Paneer Butter Masala",
    "fried": "Fried Rice",
    "noodle": "Hakka Noodles",
    "lollipop": "Chicken Lollipop",
    "samosa": "Samosa",
    "milkshake": "Chocolate Milkshake",
    "idli": "Idli",
    "vada": "Medu Vada",
    "pongal": "Pongal",
    "upma": "Upma",
    "poori": "Poori Bhaji",
    "curd": "Curd Rice",
    "lemon": "Lemon Rice",
    "tomato": "Tomato Rice",
    "naan": "Butter Naan",
    "roti": "Tandoori Roti",
    "manchurian": "Veg Manchurian",
    "ice": "Vanilla Ice Cream",
    "fries": "French Fries",
    "sandwich": "Cheese Sandwich"
}

updated = 0

for food in foods.find():

    image_url = food.get("image", "").lower()

    for keyword in food_map:

        if keyword in image_url:
            foods.update_one(
                {"_id": food["_id"]},
                {"$set": {"name": food_map[keyword]}}
            )
            updated += 1
            break

print(f"✅ {updated} food names corrected automatically")