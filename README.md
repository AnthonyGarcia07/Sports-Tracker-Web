# Sports Stats Tracker

A full stack web application that allows users to search for any athlete and instantly retrieve their team, sport, position, and photo using TheSportDB API.

## Live Demo
https://sports-tracker-web.onrender.com

## Features
- Search any player across multiple sports including Soccer, Basketball, Baseball and much more
- Displays player name, team, sport, position, and photo
- Persistant search history powered by SQLite — shows the last 10 searches
- Error handling for players not found in the database

## Tech Stack
- **Backend** — Python, Flask
- **Database** — SQLite
- **Frontend** — HTML, CSS, Jinja2
- **API** — TheSportsDB

## How to Run Locally
1. Clone the repository
2. Create and activate the virtual enviroment
3. Install dependencies with `pip install -r requirements.txt`
4. Run the app with `python app.py`
5. Visit `http://127.0.0.1:5000` in your browser

## Future Improvements
- Add team search functionality
- Add more player statistics
- Add dark mode
- Add favorites/bookmark feature