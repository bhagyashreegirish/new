from transformers import pipeline

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_model(text)
    return result[0]['label']  # "POSITIVE", "NEGATIVE", or "NEUTRAL"
