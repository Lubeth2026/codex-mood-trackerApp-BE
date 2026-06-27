
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask. Welcome to the Mood Tracker!"
    })

@app.route("/save", methods=["POST"])
def save():
    # GET the json sent from React
    data = request.get_json()
    # Open the json file and READ contents
    with open("updates.json", "r") as file:
        moods = json.load(file)
    # ADD new mood to the list
    moods.append(data)
    # Save the updated list back into the json file
    with open("updates.json", "w") as file:
        json.dump(moods, file, indent=4)
    # Send a response back to React    
    return jsonify({
        "message": "Mood Saved Successfully!"
    })

@app.route("/moods", methods=["GET"])
def get_moods():

    with open("updates.json", "r") as file:
        moods = json.load(file)

    return jsonify(moods)
