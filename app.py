from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route("/")
def home():
    # grabs the player name from the search form, default to LeBron if nothing is searched yet
    name = request.args.get("player_name", "Lebron James")
    # this url is making the call to the api, this is where we get all of our information from for our players
    url = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={name}"
    # sends an HTTP GET request to the api and stores the response 
    player_response = requests.get(url)
    # this puts it into a json format, so that it becomes easier to work with
    data = player_response.json()

    # checks if the player exists in the api, if not then returns "player not found"
    if data["player"] is None:
        return "Player not found."

    # stores the players name, team, sport, and position
    player = data["player"][0]["strPlayer"]
    team = data["player"][0]["strTeam"]
    sport = data["player"][0]["strSport"]
    position = data["player"][0]["strPosition"]


    # this returns the render template. so it returns the players name, team, sport, and position
    return render_template("index.html", player=player, team=team, sport=sport, position=position)

if __name__ == "__main__":
    app.run(debug=True)



