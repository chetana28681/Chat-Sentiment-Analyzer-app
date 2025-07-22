from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['message']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        result = "Positive 😊"
    elif sentiment < 0:
        result = "Negative 😠"
    else:
        result = "Neutral 😐"

    return render_template('index.html', message=text, sentiment=result, score=round(sentiment, 2))

if __name__ == '__main__':
    app.run(debug=True)
