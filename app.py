import gradio as gr
from utils import fetch_news, analyze_sentiment, comparative_analysis, generate_tts
from deep_translator import GoogleTranslator

def process(company):
    tts_text = ""
    articles = fetch_news(company)

    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
        #tts_text += f"title is {article['title']} \n summary was {article['summary']} was {article['sentiment']} news. " //the line add the summary of news in the output mp3

    sentiment_report = comparative_analysis(articles)
    tts_text += f"\n\nThe {company} has {sentiment_report['Positive']} positive, {sentiment_report['Negative']} negative, and {sentiment_report['Neutral']} neutral articles."

    tts_text_hindi = GoogleTranslator(source="en", target="hi").translate(tts_text)
    generate_tts(tts_text_hindi)

    return articles, sentiment_report, "output.mp3"

demo = gr.Interface(fn=process, inputs="text", outputs=["json", "json", "audio"])
demo.launch()
