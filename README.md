# News Summarization and Text-to-Speech Application
### Overview
A web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool should allow users to input a company name and receive a structured sentiment report along with an audio output.

### Tech Stack:
Frontend: Gradio

Backend: Flask (APIs)

NLP Models: Hugging Face transformers (Sentiment Analysis)

Text-to-Speech: gTTS (Hindi Speech)

News Extraction: NewsAPI

## Project Setup:
### Prerequisites
Python 3.8+

pip

### Clone the Repository
Clone this repository locally. In a terminal, run the following command:

```
$ git clone https://github.com/shareefmx/News-Summarization.git
$ cd news-summarization-tts
```
### Open

Open the cloned repository in your VS code.
### Install the python packages and setup the environment

Open the terminal and install the package. 
```
pip install gradio
pip install flask
pip install tensorflow
pip install torch torchvision torchaudio
pip install deep-translator
```

setup with virtual environments(.venv file) and install.
```
python -m venv env
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
OR
```
pip install requests beautifulsoup4 newspaper3k transformers torch gradio streamlit gTTS
```
### Run the Application 

Run the python file. In a terminal, run the following command:

```
$ python app.py
```
Running on local URL and click [ Ctrl + click ] the url(Access the interface at http://127.0.0.1:7860/).

## Model Details

### News Summarization

Approach: Uses the description field from NewsAPI as a summary.

Why? Avoids unnecessary processing and ensures real-time performance.

### Sentiment Analysis

Model: Hugging Face's distilbert-base-uncased-finetuned-sst-2-english
How it Works?

Takes the news summary as input.

Classifies it into Positive, Negative, or Neutral sentiment.

### Text-to-Speech (TTS)

Model: gTTS (Google Text-to-Speech)

Language: Hindi (lang="hi")

#### Workflow:

English text is translated to Hindi using deep_translator.

Hindi text is converted into speech using gTTS.

## API Endpoints

| Endpoint | Method | Description | Example |
|----------|--------|-------------|---------|
| `/news?company=Tesla` | `GET` | Fetches news articles for a company | `http://127.0.0.1:5000/news?company=Tesla` |
| `/sentiment` | `POST` | Performs sentiment analysis on text | `curl -X POST -H "Content-Type: application/json" -d '{"text": "Tesla is performing well"}' http://127.0.0.1:5000/sentiment` |
| `/tts` | `POST` | Converts text to Hindi speech | `curl -X POST -H "Content-Type: application/json" -d '{"text": "Tesla is growing fast"}' http://127.0.0.1:5000/tts` |

## Testing the APIs with Postman

### Open Postman

Test News Fetching:

GET: http://127.0.0.1:5000/news?company=Apple

### Test Sentiment Analysis:

POST: http://127.0.0.1:5000/sentiment

Body: { "text": "Apple is leading the market" }

### Test Text-to-Speech:

POST: http://127.0.0.1:5000/tts

Body: { "text": "Apple has recorded high sales this quarter" }

## Assumptions & Limitations

### Assumptions

NewsAPI provides at least 10 relevant articles per company.

Sentiment analysis works reliably for short news summaries.

Google Translator API provides accurate Hindi translations.

### Limitations

NewsAPI's free tier has a daily request limit (100 requests/day).

TTS is limited to short summaries (long texts may cause delays).

Translation quality may not be perfect for complex sentences.


