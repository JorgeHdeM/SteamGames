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
df_games = []
for i in range(len(users)):
    user_name = users.iloc[i][2]
    url = steam.do_url(API_KEY=users.iloc[i][0], USER_ID=users.iloc[i][1])
    games_data = steam.get_response(url, user_name)
    df_games.append(steam.format_response(games_data, user_name))
    i += 1

df_concat = steam.concat_df(df_games)
df_concat = df_concat.sort_values(columns.DF_PERSONAL, ascending=[True, False]).reset_index(drop=True)
df_friends = steam.shared_friends(df_concat)
df_friends_price = steam.price_response(df_friends)

steam.export_file(df_concat, "Games_PlayedTime")
steam.export_file(df_friends_price, "Friends_Price")

logging.info(f"\nRun time: {round(time.time() - start_time, 2)} seconds")