import requests
import logging

class UrlResponse:
    def __init__(self):
        logging.info("\n########## Getting owned games info ##########")
    
    def get_response(self, url):
        try:
            url_response = requests.get(url)
            game_data = url_response.json()
            logging.info(f"Successfully retrieved data: \n{game_data['response']['game_count']} Owned games")
            return game_data
        except:
            logging.error(f"Wrong KEY or USER ID")
            quit()