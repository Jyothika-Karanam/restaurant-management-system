import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# ✅ ADD PROJECT ROOT TO PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.db import get_all_orders, get_all_reviews


def run():   # ✅ WRAPPED INSIDE FUNCTION

    # ---------------- PAGE CONFIG ----------------
    st.set_page_config(page_title="Admin Dashboard", layout="wide")

    # ---------------- CACHE ----------------
    @st.cache_data
    def load_data():
        orders = get_all_orders()
        reviews = get_all_reviews()
        return pd.DataFrame(orders), pd.DataFrame(reviews)

    orders_df, reviews_df = load_data()

    # ---------------- CUSTOM CSS ----------------
    st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3 {
        color: black !important;
    }
    .metric-card {
        background: linear-gradient(135deg, #1f4037, #99f2c8);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: black;
        font-weight: bold;
        font-size: 18px;
    }
    .section {
        background-color: #161A25;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- TITLE ----------------
    st.title("📊 AI Smart Restaurant — Admin Analytics")

    # ---------------- TOP METRICS ----------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='metric-card'>🧾 Total Orders<br>{len(orders_df)}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-card'>⭐ Total Reviews<br>{len(reviews_df)}</div>",
            unsafe_allow_html=True
        )

    if not orders_df.empty:
        most_ordered = orders_df["food_name"].value_counts().idxmax()
    else:
        most_ordered = "N/A"

    with col3:
        st.markdown(
            f"<div class='metric-card'>🔥 Most Ordered<br>{most_ordered}</div>",
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------- FOOD DEMAND ----------------
    colA, colB = st.columns(2)

    with colA:
        #st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("🍽 Food Demand Analytics")

        if not orders_df.empty:
            chart = orders_df["food_name"].value_counts().reset_index()
            chart.columns = ["Food", "Orders"]

            fig = px.bar(
                chart,
                x="Food",
                y="Orders",
                color="Orders",
                text="Orders",
                template="plotly_dark"
            )
            fig.update_layout(height=350)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No order data available")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- CUSTOMER SATISFACTION ----------------
    with colB:
        #st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("⭐ Customer Satisfaction")

        if not reviews_df.empty:
# Convert star rating to numeric before calculating mean
            reviews_df["rating"] = reviews_df["rating"].str.count("⭐")

            avg_rating = (
            reviews_df
            .groupby("food_name")["rating"]
            .mean()
            .reset_index()
)
            fig2 = px.bar(
                avg_rating,
                x="food_name",
                y="rating",
                color="rating",
                text="rating",
                template="plotly_dark"
            )
            fig2.update_layout(height=350)

            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No review data available")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SENTIMENT ----------------
    colC, colD = st.columns(2)

    with colC:
        #st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("😊 Sentiment Distribution")

        if not reviews_df.empty:
            sentiment_chart = reviews_df["sentiment"].value_counts().reset_index()
            sentiment_chart.columns = ["Sentiment", "Count"]

            fig3 = px.pie(
                sentiment_chart,
                names="Sentiment",
                values="Count",
                hole=0.6,
                template="plotly_dark"
            )
            fig3.update_layout(height=350)

            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No sentiment data available")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- RECENT REVIEWS ----------------
    with colD:
        #st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("📝 Recent Customer Reviews")

        if not reviews_df.empty:
            st.dataframe(
                reviews_df[["food_name", "rating", "review", "sentiment"]],
                use_container_width=True,
                height=350
            )
        else:
            st.info("No reviews yet")

        st.markdown("</div>", unsafe_allow_html=True)