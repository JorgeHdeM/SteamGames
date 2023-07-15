import requests
import logging


class UrlResponse:
    def __init__(self):
        logging.info("\n########## Getting URL info ##########")
    
    def get_response_games(self, url):
        try:
            url_response = requests.get(url)
            game_data = url_response.json()
            return game_data
        except:
            logging.error(f"Wrong KEY or USER ID")
            quit()