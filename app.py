from flask import Flask, render_template, request
from chtbot import greeting, response  # Import your chatbot functions

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response_message = response(user_message)
    return {'bot_response': response_message}

if __name__ == '__main__':
    app.run(debug=True)
