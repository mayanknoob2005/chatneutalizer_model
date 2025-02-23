#we are not using this now
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Path to your model file (where you saved it)
model_file = '/Users/model.y'

# A function to simulate model.py's behavior
def process_input(user_input):
    # Simulating the check for "bad words"
    bad_words = ['badword1', 'badword2']  # Add your own bad words
    if any(word in user_input for word in bad_words):
        with open(model_file, 'r') as file:
            lines = file.readlines()
            return lines[-1].strip()  #answer
    else:
        return user_input

@app.route('/process_input', methods=['POST'])
def get_input():
    data = request.json
    user_input = data.get('user_input')
    if user_input:
        result = process_input(user_input)
        return jsonify({'answer': result})
    return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)