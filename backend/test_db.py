from customer_service import get_customer, create_customer

phone = "9876543210"

user = get_customer(phone)

if user:
    print("✅ Existing customer:", user["name"])

else:
    data = {
        "name": "Jyothika",
        "phone": phone,
        "email": "jyothika@gmail.com",
        "address": "Hyderabad"
    }

    create_customer(data)
    print("🆕 New customer created")