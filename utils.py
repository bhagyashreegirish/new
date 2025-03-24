from collections import Counter

def comparative_sentiment_analysis(sentiments):
    sentiment_count = Counter(sentiments)
    total_articles = len(sentiments)
    analysis = {
        'Positive': sentiment_count.get('POSITIVE', 0) / total_articles,
        'Negative': sentiment_count.get('NEGATIVE', 0) / total_articles,
        'Neutral': sentiment_count.get('NEUTRAL', 0) / total_articles,
    }
    return analysis
