from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ✅ Function to clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[^\w\s]", "", text)
    return text

# ✅ Function to classify sentiment
def get_sentiment(text, analyzer):
    score = analyzer.polarity_scores(str(text))["compound"]
    if score > 0.02:
        return "Positive"
    elif score < -0.02:
        return "Negative"
    else:
        return "Neutral"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded!"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file!"})

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)
    df.dropna(inplace=True)

    analyzer = SentimentIntensityAnalyzer()
    df["Cleaned_Text"] = df.iloc[:, 0].apply(clean_text)
    df["Sentiment"] = df["Cleaned_Text"].apply(lambda x: get_sentiment(x, analyzer))

    sentiment_counts = df["Sentiment"].value_counts()

    # ✅ Generate and save the sentiment graph
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Analysis of Tweets")
    plt.savefig("static/sentiment_plot.png")  # ✅ Save image for display

    return jsonify({
        "positive": int(sentiment_counts.get("Positive", 0)),
        "negative": int(sentiment_counts.get("Negative", 0)),
        "neutral": int(sentiment_counts.get("Neutral", 0)),
        "image_url": "static/sentiment_plot.png"
    })

if __name__ == "__main__":
    app.run(debug=True)
