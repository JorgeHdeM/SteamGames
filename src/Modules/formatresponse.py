import pandas as pd
import logging

class FormatResponse:
    def __init__(self):
        logging.info("\n########## Formatting information ##########")

    def format_response(self, data):
        response = data["response"]
        games_total = response["games"]

        games_name = []
        games_time = []
        for game in games_total:
            games_name.append(game["name"])
            games_time.append(game['playtime_forever'])
        games = {"Game_name":games_name, "Played_time_hours":games_time}
        df_games = pd.DataFrame(games)
        df_games["Played_time_hours"] = df_games["Played_time_hours"].apply(
                                                                        lambda x:round(int(x)/60,2) 
                                                                        if str(x).isdigit() else x)
        df_games = df_games.sort_values("Played_time_hours", ascending=False).reset_index(drop=True)
        logging.info(f"Successfully retrieved information")
        return df_games