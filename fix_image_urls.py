from backend.db import foods

for food in foods.find():

    img = food.get("image", "")

    # Fix broken Unsplash URL (if missing width)
    if "unsplash.com" in img and "?w=" not in img:
        new_url = img + "?w=500"

        foods.update_one(
            {"_id": food["_id"]},
            {"$set": {"image": new_url}}
        )

print("✅ Image URLs fixed")