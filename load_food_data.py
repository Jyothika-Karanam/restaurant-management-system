from pymongo import MongoClient

MONGO_URI = "mongodb+srv://restaurant_admin:restaurant_admin@cluster0.osikles.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
foods = db["foods"]

food_items = [

# ✅ YOUR ORIGINAL 10
{
"name": "Chicken Biryani",
"description": "Aromatic basmati rice with spicy chicken",
"price": 220,
"image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
},
{
"name": "Veg Burger",
"description": "Crispy veg patty with fresh veggies",
"price": 120,
"image": "https://images.unsplash.com/photo-1550547660-d9450f859349"
},
{
"name": "Margherita Pizza",
"description": "Classic cheese pizza with tomato base",
"price": 200,
"image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38"
},
{
"name": "Masala Dosa",
"description": "South Indian dosa with potato filling",
"price": 90,
"image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976"
},
{
"name": "Paneer Butter Masala",
"description": "Paneer cubes in rich buttery gravy",
"price": 180,
"image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7"
},
{
"name": "Fried Rice",
"description": "Indo-Chinese style vegetable fried rice",
"price": 140,
"image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b"
},
{
"name": "Hakka Noodles",
"description": "Stir fried noodles with veggies",
"price": 130,
"image": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841"
},
{
"name": "Chicken Lollipop",
"description": "Crispy deep fried chicken wings",
"price": 160,
"image": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58"
},
{
"name": "Gulab Jamun",
"description": "Soft milk-solid balls in sugar syrup",
"price": 80,
"image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
},
{
"name": "Chocolate Milkshake",
"description": "Rich creamy chocolate shake",
"price": 110,
"image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"
},

# ✅ ADDITIONAL 55 ITEMS

{"name":"Idli","description":"Soft steamed rice cakes","price":40,"image":"https://images.unsplash.com/photo-1589302168068-964664d93dc0"},
{"name":"Medu Vada","description":"Crispy fried urad dal vada","price":50,"image":"https://images.unsplash.com/photo-1630383249896-424e482df921"},
{"name":"Sambar Vada","description":"Vada soaked in hot sambar","price":60,"image":"https://images.unsplash.com/photo-1626074353765-517a681e40be"},
{"name":"Rava Dosa","description":"Thin crispy semolina dosa","price":85,"image":"https://images.unsplash.com/photo-1610192244261-3f33de3f55e4"},
{"name":"Set Dosa","description":"Soft thick dosa set of three","price":80,"image":"https://images.unsplash.com/photo-1668236543090-82eba5ee5976"},
{"name":"Pongal","description":"Creamy rice and moong dal dish","price":60,"image":"https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"},
{"name":"Upma","description":"Savory semolina breakfast","price":50,"image":"https://images.unsplash.com/photo-1626074353765-517a681e40be"},
{"name":"Poori Bhaji","description":"Fluffy poori with potato curry","price":80,"image":"https://images.unsplash.com/photo-1626700051175-6818013e1d4f"},
{"name":"Curd Rice","description":"Comforting tempered curd rice","price":60,"image":"https://images.unsplash.com/photo-1631452180519-c014fe946bc7"},
{"name":"Tomato Rice","description":"Tangy tomato flavored rice","price":70,"image":"https://images.unsplash.com/photo-1596797038530-2c107229654b"},
{"name":"Lemon Rice","description":"Zesty lemon tempered rice","price":65,"image":"https://images.unsplash.com/photo-1596797038530-2c107229654b"},
{"name":"Veg Biryani","description":"Aromatic basmati with vegetables","price":120,"image":"https://images.unsplash.com/photo-1563379091339-03246963d96c"},
{"name":"Paneer Biryani","description":"Fragrant rice with paneer cubes","price":160,"image":"https://images.unsplash.com/photo-1601050690597-df0568f70950"},
{"name":"Jeera Rice","description":"Cumin tempered basmati rice","price":90,"image":"https://images.unsplash.com/photo-1596797038530-2c107229654b"},
{"name":"Egg Fried Rice","description":"Fried rice with scrambled egg","price":130,"image":"https://images.unsplash.com/photo-1603133872878-684f208fb84b"},
{"name":"Chicken Fried Rice","description":"Fried rice with chicken pieces","price":150,"image":"https://images.unsplash.com/photo-1603133872878-684f208fb84b"},
{"name":"Veg Noodles","description":"Stir fried vegetable noodles","price":100,"image":"https://images.unsplash.com/photo-1612929633738-8fe44f7ec841"},
{"name":"Chicken Noodles","description":"Noodles tossed with chicken","price":140,"image":"https://images.unsplash.com/photo-1612929633738-8fe44f7ec841"},
{"name":"Dal Makhani","description":"Slow cooked buttery black dal","price":140,"image":"https://images.unsplash.com/photo-1626074353765-517a681e40be"},
{"name":"Rajma Masala","description":"Kidney beans in rich gravy","price":130,"image":"https://images.unsplash.com/photo-1626074353765-517a681e40be"},
{"name":"Chole Masala","description":"Spicy chickpea curry","price":130,"image":"https://images.unsplash.com/photo-1626074353765-517a681e40be"},
{"name":"Butter Naan","description":"Soft naan with butter","price":40,"image":"https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"},
{"name":"Garlic Naan","description":"Naan topped with garlic","price":50,"image":"https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"},
{"name":"Tandoori Roti","description":"Whole wheat tandoor roti","price":35,"image":"https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"},
{"name":"Veg Manchurian","description":"Fried veg balls in sauce","price":120,"image":"https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"},
{"name":"Chicken Manchurian","description":"Chicken tossed in Manchurian sauce","price":160,"image":"https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"},
{"name":"Paneer 65","description":"Spicy deep fried paneer cubes","price":150,"image":"https://images.unsplash.com/photo-1631452180519-c014fe946bc7"},
{"name":"Chicken 65","description":"South Indian spicy chicken starter","price":170,"image":"https://images.unsplash.com/photo-1601050690117-64b6d8b8a3c1"},
{"name":"Gobi 65","description":"Crispy cauliflower fry","price":120,"image":"https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"},
{"name":"Samosa","description":"Crispy pastry with potato filling","price":25,"image":"https://images.unsplash.com/photo-1601050690597-df0568f70950"},
{"name":"Mirchi Bajji","description":"Stuffed chilli fritters","price":30,"image":"https://images.unsplash.com/photo-1626700051175-6818013e1d4f"},
{"name":"Aloo Bonda","description":"Fried potato dumplings","price":30,"image":"https://images.unsplash.com/photo-1626700051175-6818013e1d4f"},
{"name":"Veg Cutlet","description":"Crispy vegetable patties","price":35,"image":"https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"},
{"name":"French Fries","description":"Golden salted potato fries","price":90,"image":"https://images.unsplash.com/photo-1541592106381-b31e9677c0e5"},
{"name":"Cheese Sandwich","description":"Grilled cheese sandwich","price":80,"image":"https://images.unsplash.com/photo-1528735602780-2552fd46c7af"},
{"name":"Chicken Burger","description":"Juicy chicken patty burger","price":120,"image":"https://images.unsplash.com/photo-1550547660-d9450f859349"},
{"name":"Farmhouse Pizza","description":"Pizza with fresh veggies","price":220,"image":"https://images.unsplash.com/photo-1594007654729-407eedc4fe24"},
{"name":"Rasgulla","description":"Spongy syrupy delight","price":60,"image":"https://images.unsplash.com/photo-1625242661767-0a1f0c5d0b9c"},
{"name":"Jalebi","description":"Crispy spiral sweet","price":70,"image":"https://images.unsplash.com/photo-1630409346824-4f0e7b080087"},
{"name":"Kaju Katli","description":"Premium cashew sweet","price":90,"image":"https://images.unsplash.com/photo-1601050690597-df0568f70950"},
{"name":"Rasmalai","description":"Soft paneer in sweet milk","price":80,"image":"https://images.unsplash.com/photo-1625242661767-0a1f0c5d0b9c"},
{"name":"Badam Halwa","description":"Rich almond dessert","price":90,"image":"https://images.unsplash.com/photo-1601050690597-df0568f70950"},
{"name":"Chocolate Ice Cream","description":"Creamy chocolate scoop","price":70,"image":"https://images.unsplash.com/photo-1497034825429-c343d7c6a68f"},
{"name":"Vanilla Ice Cream","description":"Classic vanilla scoop","price":60,"image":"https://images.unsplash.com/photo-1563805042-7684c019e1cb"},
{"name":"Strawberry Milkshake","description":"Fresh strawberry shake","price":90,"image":"https://images.unsplash.com/photo-1589308078059-be1415eab4c3"},
{"name":"Mango Milkshake","description":"Sweet mango blended shake","price":100,"image":"https://images.unsplash.com/photo-1625943553852-781c6dd46faa"}

]

foods.insert_many(food_items)

print("✅ 65 Food items inserted successfully")
print(client.list_database_names())