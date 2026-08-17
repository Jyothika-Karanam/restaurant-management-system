import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

print("ROOT:", ROOT_DIR)
print("FILES IN ROOT:", os.listdir(ROOT_DIR))
import streamlit as st
import random
from backend.db import get_user, create_user
from datetime import datetime, timedelta
import smtplib


st.set_page_config(page_title="Login", layout="wide")

# ---------------- SESSION ----------------
if "user_email" not in st.session_state:
    st.session_state.user_email = None

# ---------------- AUTO LOGIN ----------------
if st.session_state.user_email:
    st.switch_page("app/customer_app.py")

# ---------------- UI ----------------
col1, col2 = st.columns(2)

with col1:
    st.image("assets/food_banner.jpg", use_column_width=True)
    st.markdown("## India’s Favourite Food Delivery 🍛")
    st.markdown("### Crave it? We deliver it fresh & fast!")

with col2:
    st.markdown("## Login with Email OTP")

    email = st.text_input("Enter your email")

    if st.button("Send OTP"):

        otp = str(random.randint(100000, 999999))
        st.session_state.otp = otp
        st.session_state.otp_expiry = datetime.now() + timedelta(minutes=2)
        st.session_state.temp_email = email

        # SEND EMAIL
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("YOUR_EMAIL@gmail.com", "APP_PASSWORD")
        server.sendmail(
            "YOUR_EMAIL@gmail.com",
            email,
            f"Your OTP is {otp}"
        )
        server.quit()

        st.success("OTP sent to your email")

    otp_input = st.text_input("Enter OTP")

    if st.button("Verify OTP"):

        if datetime.now() > st.session_state.otp_expiry:
            st.error("OTP expired")

        elif otp_input == st.session_state.otp:

            user = get_user(st.session_state.temp_email)

            if not user:
                create_user(st.session_state.temp_email)
                st.success("Welcome new user ❤️")
            else:
                st.success("Welcome back 🎉")

            st.session_state.user_email = st.session_state.temp_email
            st.switch_page("app/customer_app.py")

        else:
            st.error("Invalid OTP")