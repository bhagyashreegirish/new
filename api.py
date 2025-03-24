from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_articles', methods=['POST'])
def get_articles():
    company_name = request.json['company_name']
    articles = get_news_articles(company_name)
    return jsonify(articles)

@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    article_text = request.json['article_text']
    sentiment = analyze_sentiment(article_text)
    return jsonify({'sentiment': sentiment})

@app.route('/get_tts', methods=['POST'])
def get_tts():
    report_text = request.json['report_text']
    tts_filename = generate_tts_report(report_text)
    return jsonify({'tts_filename': tts_filename})

if __name__ == '__main__':
    app.run(debug=True)
