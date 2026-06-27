
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask. Welcome to the Mood Tracker!"
    })

