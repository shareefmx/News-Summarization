from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, comparative_analysis, generate_tts

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    company = request.args.get('company')
    articles = fetch_news(company)
    return jsonify(articles)

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    data = request.get_json()
    sentiment_result = analyze_sentiment(data["text"])
    return jsonify({"sentiment": sentiment_result})

@app.route('/tts', methods=['POST'])
def get_tts():
    data = request.get_json()
    generate_tts(data["text"])
    return jsonify({"message": "TTS generated successfully"})

if __name__ == '__main__':
    app.run(debug=True)
