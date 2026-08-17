import sys
import os
import time
import streamlit as st
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.db import (
    get_user_orders,
    get_all_foods,
    insert_order,
    insert_review,
    add_favorite,
    remove_favorite,
    get_user_favorites,
    get_user,
    create_user,
    get_all_orders,
    get_all_reviews,
    get_orders_today
)

from backend.analytics import get_sentiment
from app import admin_app

st.set_page_config(page_title="Foodie SaaS", layout="wide")

ADMIN_EMAIL = "23091a3255@rgmcet.edu.in"
ADMIN_PASSWORD = "jyovirat18"

# ---------------- STYLES ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#fff1f2,#ffffff);
    font-family: 'Segoe UI', sans-serif;
    color:black;
}
.header {
    font-size:40px;
    font-weight:800;
    background: linear-gradient(90deg,#ff4b2b,#ff416c);
    -webkit-background-clip:text;
    color:transparent;
}
.black-header {
    font-size:32px;
    font-weight:700;
    color:black;
}
.black-label {
    color:black;
    font-weight:600;
}
.review-label {
    color:black;
    font-weight:600;
}
.capsule {
    display:inline-block;
    background:linear-gradient(90deg,#ffe5e9,#fff7f8);
    color:#d6336c;
    padding:6px 14px;
    border-radius:50px;
    font-size:12px;
    font-weight:700;
    margin-bottom:6px;
}
.food-img {
    border: 3px solid #ffc2d1;
    border-radius: 15px;
    padding: 6px;
}
div.stButton > button:first-child {
    background-color: white;
    color: black;
    border: 1px solid #ddd;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg,#ff7a18,#ff4b2b);
    color: white;
    border: none;
    font-weight: 600;
}
div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg,#ff6a00,#ff3c00);
    color: white;
}
.place-order button {
    background: linear-gradient(90deg,#38b000,#70e000) !important;
    color: white !important;
    border: none !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
for key, val in {
    "user_email": None,
    "page": "login",
    "food": None,
    "order_id": None,
    "favorites": [],
    "is_admin": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ---------------- DATA ----------------
@st.cache_data
def load_foods():
    return get_all_foods()

foods = load_foods()
food_lookup = {f["name"]: f for f in foods}
food_lookup_by_id = {str(f["_id"]): f for f in foods}

# ---------------- LOGIN ----------------
if st.session_state.page == "login":

    col1, col2 = st.columns(2)
    col1.image("assets/food_banner.jpg", use_container_width=True)

    with col2:
        st.markdown("<div class='header'>Foodie 🍴</div>", unsafe_allow_html=True)
        email = st.text_input("Enter your email")

        if email and email.lower() == ADMIN_EMAIL:
            password = st.text_input("Enter Admin Password", type="password")

            if st.button("Login as Admin"):
                if password == ADMIN_PASSWORD:
                    st.session_state.user_email = email.lower()
                    st.session_state.is_admin = True
                    st.session_state.page = "home"
                    st.success("Admin Login Successful")
                    st.rerun()
                else:
                    st.error("Incorrect Admin Password")

        elif st.button("Continue", type="secondary") and email:
            email = email.lower()

            if not get_user(email):
                create_user(email)

            st.session_state.user_email = email
            st.session_state.favorites = get_user_favorites(email)
            st.session_state.is_admin = False
            st.session_state.page = "home"
            st.rerun()

# ---------------- HOME ----------------
elif st.session_state.page == "home":

    st.session_state.favorites = get_user_favorites(st.session_state.user_email)

    if st.session_state.is_admin:
        c1, c2, c3 = st.columns([8,1,1])
    else:
        c1, c2 = st.columns([9,1])

    with c1:
        st.markdown("<div class='header'>Home</div>", unsafe_allow_html=True)

    with c2:
        if st.button("👤"):
            st.session_state.page = "profile"
            st.rerun()

    if st.session_state.is_admin:
        with c3:
            if st.button("📊"):
                st.session_state.page = "admin"
                st.rerun()

    orders = get_user_orders(st.session_state.user_email)

    st.subheader(f"Welcome {st.session_state.user_email} ❤️")
    st.subheader("🧠 You may also like")

    ordered_names = [o["food_name"] for o in orders]
    most_common = [name for name, _ in Counter(ordered_names).most_common()]
    recommended = [f for f in foods if f["name"] not in most_common][:4]

    if recommended:
        cols = st.columns(4)
        for i, food in enumerate(recommended):
            with cols[i % 4]:
                st.markdown(f"<div class='capsule'>{food.get('description','')}</div>", unsafe_allow_html=True)
                #st.markdown("<div class='food-img'>", unsafe_allow_html=True)
                st.image(food["image"], use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.write(food["name"])
                st.write(f"₹{food['price']}")

    st.subheader("Explore Menu")

    search = st.text_input("🔍 Search food")
    filtered = [f for f in foods if search.lower() in f["name"].lower()] if search else foods

    cols = st.columns(4)

    for i, food in enumerate(filtered):
        desc = food.get("description", "Chef Special 😋")

        with cols[i % 4]:
            st.markdown(f"<div class='capsule'>{desc}</div>", unsafe_allow_html=True)
            #st.markdown("<div class='food-img'>", unsafe_allow_html=True)
            st.image(food["image"], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.subheader(food["name"])
            st.write(f"₹{food['price']}")

            fav = str(food["_id"]) in st.session_state.favorites

            if st.button("❤️" if fav else "🤍", key=f"fav{food['_id']}"):
                if fav:
                    remove_favorite(st.session_state.user_email, food["_id"])
                else:
                    add_favorite(st.session_state.user_email, food["_id"])
                    st.toast("Added to favourites ❤️")
                st.session_state.favorites = get_user_favorites(st.session_state.user_email)
                st.rerun()

            if st.button("View", key=str(food["_id"]), type="primary"):
                st.session_state.food = food
                st.session_state.page = "details"
                st.rerun()

# ---------------- DETAILS PAGE ----------------
elif st.session_state.page == "details":

    food = st.session_state.food
    gst = round(food["price"] * 0.05, 2)
    total = food["price"] + gst

    st.markdown("<div class='header'>Food Details</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown("<div class='food-img'>", unsafe_allow_html=True)
        st.image(food["image"], width=250)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.subheader(food["name"])
        st.write(f"Price: ₹{food['price']}")
        st.write(f"GST (5%): ₹{gst}")
        st.write(f"Total: ₹{total}")

        st.markdown('<div class="place-order">', unsafe_allow_html=True)
        if st.button("Place Order 🛒"):
            st.session_state.page = "order_form"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ORDER FORM ----------------
elif st.session_state.page == "order_form":

    if st.button("⬅ Back to Details"):
        st.session_state.page = "details"
        st.rerun()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("<div class='header'>Enter Delivery Details</div>", unsafe_allow_html=True)

    st.markdown("<div class='black-label'>Full Name</div>", unsafe_allow_html=True)
    name = st.text_input(" ", key="name")

    st.markdown("<div class='black-label'>Mobile Number</div>", unsafe_allow_html=True)
    mobile = st.text_input(" ", key="mobile")

    st.markdown("<div class='black-label'>Address</div>", unsafe_allow_html=True)
    address = st.text_area(" ", key="address")

    if st.button("Submit Order"):

        insert_order({
            "user_email": st.session_state.user_email,
            "food_name": st.session_state.food["name"],
            "price": st.session_state.food["price"],
            "customer_name": name,
            "mobile": mobile,
            "address": address
        })

        st.success("🎉 Thanks for placing the order!")
        time.sleep(2)

        st.session_state.page = "review"
        st.rerun()

# ---------------- REVIEW PAGE ----------------
elif st.session_state.page == "review":

    if st.button("⬅ Back to Order Form"):
        st.session_state.page = "order_form"
        st.rerun()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("<div class='black-header'>Rate & Review</div>", unsafe_allow_html=True)

    st.markdown("<div class='review-label'>Select Rating</div>", unsafe_allow_html=True)
    rating = st.radio(
        "",
        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        horizontal=True
    )

    st.markdown("<div class='review-label'>Write your feedback</div>", unsafe_allow_html=True)
    feedback = st.text_area("")

    if st.button("Submit Review"):

        sentiment = get_sentiment(feedback)

        insert_review({
            "user_email": st.session_state.user_email,
            "food_name": st.session_state.food["name"],
            "rating": rating,
            "feedback": feedback,
            "sentiment": sentiment
        })

        if sentiment == "positive":
            st.success("💖 Thank you for your positive feedback!")
        else:
            st.markdown("<div style='background-color:#fff3cd;padding:10px;border-radius:8px;color:#856404;font-weight:600;'>🙏 Thank you! We will improve based on your feedback.</div>", unsafe_allow_html=True)

        time.sleep(2)
        st.session_state.page = "home"
        st.rerun()

# ---------------- PROFILE ----------------
elif st.session_state.page == "profile":

    st.markdown("<div class='header'>My Profile</div>", unsafe_allow_html=True)

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.subheader("📦 Previous Orders")

    user_orders = get_user_orders(st.session_state.user_email)

    if user_orders:
        order_cols = st.columns(4)
        for i, order in enumerate(user_orders):
            food_name = order.get("food_name")
            food = food_lookup.get(food_name)
            if food:
                with order_cols[i % 4]:
                    #st.markdown("<div class='food-img'>", unsafe_allow_html=True)
                    st.image(food["image"], use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.write(food["name"])
                    st.write(f"₹{food['price']}")
    else:
        st.info("No previous orders found.")

    st.subheader("❤️ My Favourite Items")

    favorites = get_user_favorites(st.session_state.user_email)

    if favorites:
        fav_cols = st.columns(4)
        for i, fav_id in enumerate(favorites):
            food = food_lookup_by_id.get(str(fav_id))
            if food:
                with fav_cols[i % 4]:
                    #st.markdown("<div class='food-img'>", unsafe_allow_html=True)
                    st.image(food["image"], use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.write(food["name"])
                    st.write(f"₹{food['price']}")

                    if st.button("Remove ❌", key=f"remove{fav_id}"):
                        remove_favorite(st.session_state.user_email, fav_id)
                        st.toast("Removed from favourites")
                        st.rerun()
    else:
        st.info("No favourite items added yet.")

# ---------------- ADMIN ----------------
elif st.session_state.page == "admin":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    admin_app.run()