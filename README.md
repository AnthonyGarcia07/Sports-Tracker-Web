# Sports Stats Tracker

Sports Stats Tracker is a full-stack Flask learning project that lets users search for athletes and view basic player information from TheSportsDB. It uses a simple Python/Flask backend, SQLite search history, and a responsive HTML/CSS interface.

![Sports Stats Tracker interface](Screenshot/Sports%20Tracker%20Screenshot.png)

## Live Demo

[https://sports-tracker-web.onrender.com](https://sports-tracker-web.onrender.com)

## Features

- Search for athletes across multiple sports using TheSportsDB
- Display player name, team, sport, position, and photo
- Save recent searches with SQLite
- Show the 10 most recent searches
- Show a simple message when a player is not found
- Responsive layout for desktop and mobile screens

## Tech Stack

- **Backend** — Python, Flask
- **Database** — SQLite
- **Frontend** — HTML, CSS, Jinja2
- **API** — TheSportsDB
- **Deployment** — Render

## How It Works

1. A user searches for an athlete by name.
2. Flask receives the search request from the form.
3. The app requests player data from TheSportsDB.
4. The app extracts the player's name, team, sport, position, and photo.
5. The search is saved in SQLite.
6. Flask sends the player data and recent searches to the Jinja template.
7. The browser receives the rendered HTML/CSS page.

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/AnthonyGarcia07/Sports-Tracker-Web.git
cd Sports-Tracker-Web
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install the requirements:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python app.py
```

6. Visit the local site:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Future Improvements

- Add team search
- Add additional player statistics
- Add favorites or bookmarks
- Improve API and network error handling
