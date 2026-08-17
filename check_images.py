import os
from backend.db import get_all_foods

foods = get_all_foods()

base_path = "public"   # ⚠️ change if your images folder is elsewhere

for food in foods:

    img_path = food["image"]

    full_path = os.path.join(base_path, img_path)

    if not os.path.exists(full_path):
        print("❌ Missing:", food["name"], "→", img_path)