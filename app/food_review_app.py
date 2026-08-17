import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from backend.db import orders  # new collection for orders
from backend.customer_service import get_customer

# ---------------------------
# STEP 1: Ensure user is logged in
# ---------------------------
if "customer" not in st.session_state or st.session_state.customer is None:
    st.warning("Please login first on the Customer Login page.")
    st.stop()

customer = st.session_state.customer
st.title(f"🍽 Welcome {customer['name']}! Order & Review Food")

# ---------------------------
# STEP 2: Food Selection Form
# ---------------------------
with st.form("food_review_form"):

    # Food items (example, can be extended)
    food_items = ["Biryani", "Pizza", "Idli", "Dosa", "Pulihora", "Sweets"]
    food_choice = st.selectbox("Select Food Item", food_items)

    # Rating
    rating = st.slider("Rate the Food (1-5)", min_value=1, max_value=5, value=5)

    # Review text
    review = st.text_area("Write your review")

    submit = st.form_submit_button("Submit Review")

# ---------------------------
# STEP 3: Handle submission
# ---------------------------
if submit:

    if not review.strip():
        st.error("Please enter a review before submitting!")
    else:
        order_data = {
            "customer_phone": customer['phone'],
            "food_item": food_choice,
            "rating": rating,
            "review": review,
            "timestamp": datetime.now()
        }

        # Save to MongoDB orders collection
        orders.insert_one(order_data)

        st.success(f"Your review for {food_choice} has been submitted ✅")
        st.balloons()