import time
import logging
from Modules.steamgames import SteamGames
from constants.columns import ColumnsGames

logging.basicConfig(level=logging.INFO, format="%(message)s")
start_time = time.time()
columns = ColumnsGames()
steam = SteamGames()
users = steam.users
try:
    if users == None:
        logging.error("No CSV found.")
        quit()
except:
    pass
# Generate all URLS
urls = []
for i in range(len(users)):
    key = users.iloc[i][0]
    user = users.iloc[i][1]
    urls.append(steam.do_url(API_KEY=key, USER_ID=user))
# Get responses 
games_data = []
for url in urls:
    games_data.append(steam.get_response(url))
# Format responses
df_games = []
for game in games_data:
    df_games.append(steam.format_response(game))

df_concat = steam.concat_df(df_games)

df_counts = df_concat[columns.DF_PERSONAL[0]].value_counts().reset_index()
df_counts.columns = columns.DF_SHARED
df_counts = df_counts.sort_values(columns.DF_SHARED[1], ascending=False)

steam.export_file(df_concat, "_GamesandHours_")
steam.export_file(df_counts, "_GamesCounts_")

logging.info(f"\nRun time: {round(time.time() - start_time, 2)} seconds")