from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("player_name", "Lebron James")
    url = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={name}"
    player_response = requests.get(url)
    data = player_response.json()

    if data["player"] is None:
        return "Player not found."

    player = data["player"][0]["strPlayer"]
    team = data["player"][0]["strTeam"]
    sport = data["player"][0]["strSport"]
    position = data["player"][0]["strPosition"]

    print(player)
    print(team)
    print(sport)
    print(position)

    return render_template("index.html", player=player, team=team, sport=sport, position=position)

if __name__ == "__main__":
    app.run(debug=True)



