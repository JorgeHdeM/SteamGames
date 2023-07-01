import pandas as pd
import logging
from constants.columns import ColumnsGames

class FormatResponse:
    def __init__(self):
        pass

    def format_response(self, data):
        columns = ColumnsGames()
        response = data[columns.STEAM_RESPONSE]
        games_total = response[columns.STEAM_GAMES]

        games_name = []
        games_time = []
        for game in games_total:
            games_name.append(game[columns.STEAM_NAME])
            games_time.append(game[columns.STEAM_TIME_PLAYED])
        games = {columns.DF_PERSONAL[0]:games_name, columns.DF_PERSONAL[1]:games_time}
        df_games = pd.DataFrame(games)
        df_games[columns.DF_PERSONAL[1]] = df_games[columns.DF_PERSONAL[1]].apply(
                                                                        lambda x:round(int(x)/60,2) 
                                                                        if str(x).isdigit() else x)
        df_games = df_games.sort_values(columns.DF_PERSONAL[1], ascending=False).reset_index(drop=True)
        return df_games