# Mood Tracker App BACKEND

## Overview
The Mood Tracker Backend is built with Python & Flask
It provides API endpoints that allow the React frontend to:
- Save mood entries
- Retrieve all saved moods
Mood data is stored locally in an "updates.json" file

### API Endpoints
GET/
- Returns a welcome message from the backend
GET/moods
- Returns all saved mood entries
POST/save
- Saves a new mood entry

#### Running the App
1. Start the Flask server:
python app.py
2. Run the backend app:
flask run
http://127.0.0.1:5000
