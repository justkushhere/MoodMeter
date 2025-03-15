# app.py
from flask import Flask, render_template, request
from model import get_sentiment  # Import your model function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        sentiment = get_sentiment(user_input)  # Get sentiment from model
        return render_template('index.html', input_text=user_input, result=sentiment)
    return render_template('index.html')  # Initial page load

'''
if __name__ == '__main__':
    app.run(debug=True)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True) # Change host and port