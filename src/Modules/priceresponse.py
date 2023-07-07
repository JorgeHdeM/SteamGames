import requests
import logging
import time 

class PriceResponse:
    def __init__(self):
        logging.info("\n########## Getting URL info ##########")
    
    def get_response_price(self, game_id, country):
        try:
            url = f"http://store.steampowered.com/api/appdetails?appids={game_id}&cc={country}"
            url_response = requests.get(url)
            game_info = url_response.json()
            price = game_info[list(game_info.keys())[0]]["data"]["price_overview"]["final_formatted"]
            mx_string = "Mex$ "
            time.sleep(1)
            if mx_string in price:
                price = price.replace(mx_string, "$")
                return price
            else:
                return price
        except:
            logging.error(f"FREE GAME - {game_id}")
            time.sleep(1)
            return "FREE GAME"