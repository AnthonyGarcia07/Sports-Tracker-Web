@app.route("/")
def home():
    url = "https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p=Lebron_James"
    player_response = requests.get(url)
    data = player_response.json()
    print(data)

    player = data["player"]
    print(player)
    return "PSG WILL WIN THE CHAMPIONS LEAGUE BACK TO BACK!"