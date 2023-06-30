import time
import logging
from Modules.steamgames import SteamGames

logging.basicConfig(level=logging.INFO, format="%(message)s")
start_time = time.time()
steam = SteamGames()
users = steam.users
if users == None:
    logging.error("No CSV found.")
    quit()

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
print(df_concat)

logging.info(f"\nRun time: {round(time.time() - start_time, 2)} seconds")