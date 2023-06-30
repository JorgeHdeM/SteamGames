import logging

class UrlCreate:
    def __init__(self):
        logging.info("\n########## Creating URL ##########")

    def create_url(self, API_KEY, USER_ID):
        url = f"""https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={USER_ID}&include_appinfo=1&include_played_free_games=1"""
        logging.info(f"Successfully created URL: \n{url}")
        return url