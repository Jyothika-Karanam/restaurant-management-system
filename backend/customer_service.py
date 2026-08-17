from backend.db import customers

# 🔍 Check customer by phone
def get_customer(phone: str):
    return customers.find_one({"phone": phone})


# ➕ Register new customer
def create_customer(data: dict):

    customer_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address")
    }

    return customers.insert_one(customer_data)