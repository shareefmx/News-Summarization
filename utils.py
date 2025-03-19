import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS

NEWS_API_KEY = "73d71511e44e4079b4fd0ae299a66dfa"

def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    data = response.json()
    articles = []

    for item in data.get("articles", [])[:10]:  # Limit to 10 articles
        articles.append({
            "title": item.get("title", "No title"),
            "summary": item.get("description", "No summary"),
            "url": item.get("url", "#"),
            "source": item["source"].get("name", "Unknown Source")
        })
    
    return articles

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return result[0]["label"]

def comparative_analysis(articles):
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment = analyze_sentiment(article["summary"]).capitalize()  # Normalize case
        if sentiment in sentiment_count:
            sentiment_count[sentiment] += 1
        else:
            sentiment_count["Neutral"] += 1  # Default to Neutral if unknown

    return sentiment_count

def generate_tts(text, filename="output.mp3"):
    tts = gTTS(text, lang="hi")  # Convert text to Hindi
    tts.save(filename)
    return filename
