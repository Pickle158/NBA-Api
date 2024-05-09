import requests  # i think this means import the api library
API_KEY = "c145f1869fb84cb89dc13e26c3002bc3"  # API key from sportsdata.io, Get ur own

# Team ID for the Denver Nuggets (replace if needed, Look at README for other TEAM_IDs)
TEAM_ID = 20
from datetime import date #Get current date and format it to the needs of the API
today = date.today()
formatted_date = today.strftime("%Y-%m-%d")

def get_current_game_score():
    """Fetches the current game scores using SportsData.io API

    Returns:
        str: The current score of the desired game, or an error message.
    """

    nbaUrl = f"https://api.sportsdata.io/v3/nba/scores/json/ScoresBasic/2024-05-06?key={API_KEY}"
    response = requests.get(nbaUrl)

    if response.status_code == 200: #200 is qualified as OK
        data = response.json()
        for game in data:  #go through the games to find the one you want
            if game["HomeTeamID"] == TEAM_ID or game["AwayTeamID"] == TEAM_ID:
                for game in data:  #sift through the crappy data of the api
                    if not game["Status"] == "NotNecessary":
                        #Extract team names and scores
                        home_team = game["HomeTeam"]  
                        away_team = game["AwayTeam"]
                        home_score = game["HomeTeamScore"]
                        away_score = game["AwayTeamScore"]
                        return f"{away_team} {away_score} - {home_score} {home_team}"  
        return "No Denver Nuggets game data found.  There might not be a game today or right now." #No game today or right now
    else:
        return f"Error: API request failed with status code {response.status_code}"

if __name__ == "__main__":
    score = get_current_game_score()
    print(score)
    #print(formatted_date)
