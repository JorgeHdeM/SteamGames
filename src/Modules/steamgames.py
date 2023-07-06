import pandas as pd
import os
import logging
from Modules.urlcreate import UrlCreate
from Modules.urlresponse import UrlResponse
from Modules.formatresponse import FormatResponse
from Modules.filehelper import FileHelper
from constants.columns import ColumnsGames
from Modules.priceresponse import PriceResponse
from Modules.countries import Countries

class SteamGames:
    def __init__(self):
        file = FileHelper()
        self.columns = ColumnsGames()
        self.users = file.open_file()

    def do_url(self, API_KEY, USER_ID):
        url_create = UrlCreate()
        self.url = url_create.create_url(API_KEY=API_KEY, USER_ID=USER_ID)
        return self.url
    
    def get_response(self, url, name):
        self.url_response = UrlResponse()
        self.response = self.url_response.get_response_games(url)
        logging.info(f"Successfully retrieved data: \n{self.response['response']['game_count']} Owned games - {name}")
        return self.response 

    def format_response(self, response, name):
        format_response = FormatResponse()
        self.df_response = format_response.format_response(response, name)
        return self.df_response
    
    def concat_df(self, dfs):
        self.df_concat = pd.concat(dfs)
        self.df_concat["TIME_PLAYED_HOURS"] = self.df_concat["TIME_PLAYED_HOURS"].astype(float)
        self.df_concat = (self.df_concat.sort_values("GAME_NAME", ascending=True)
                                                                            .reset_index(drop=True))
        return self.df_concat
    
    def shared_friends(self, df_concat):
        df_concat = df_concat.drop(columns=df_concat.columns[1:3])
        df_concat["FRIENDS_SHARED"] = df_concat.groupby("GAME_NAME")["GAME_NAME"].transform('count')
        df_concat = df_concat.sort_values(by=["FRIENDS_SHARED", "GAME_NAME"], ascending=[False, True]).reset_index(drop=True)
        df_concat = df_concat.drop_duplicates(keep="first")
        return df_concat
    
    def price_response(self, df):
        price = PriceResponse()
        countries = Countries
        df_price = df
        df_price["GAME_ID"] = df_price["GAME_ID"].apply(lambda x:str(x).strip())
        df_price["GAME_ID"] = df_price["GAME_ID"].apply(lambda x:int(x))
        for country in countries._member_names_:
            df_price[f"PRICE_{country}"] = df_price["GAME_ID"].apply(lambda x:price.get_response_price(x, country))
        return df_price

    def export_file(self, df, name):
        name = name + ".csv"
        try:
            if len(df)>1:
                output_path = os.path.abspath(os.path.join(__file__, '../../', 'Output/'+name))
                df.to_csv(output_path, index = False)
                logging.info(f"\nExported file - {name} \nExported to path - {output_path}")
                logging.info(f"Games: {len(df)}")
        except:
            logging.error(f"\nFile generation error.")
