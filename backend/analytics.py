from textblob import TextBlob
from backend.db import orders, reviews


def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


def sentiment_distribution():
    pipeline = [
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ]
    return list(reviews.aggregate(pipeline))


def most_demanded_food():
    pipeline = [
        {"$group": {"_id": "$food_name", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1}
    ]
    result = list(orders.aggregate(pipeline))
    return result


def avg_rating_per_food():
    pipeline = [
        {"$group": {"_id": "$food_name", "avg_rating": {"$avg": "$rating"}}}
    ]
    return list(reviews.aggregate(pipeline))


def predict_tomorrow_orders():
    total_orders = orders.count_documents({})
    total_days = len(set([o["date"] for o in orders.find()]))

    if total_days == 0:
        return 0

    return round(total_orders / total_days)