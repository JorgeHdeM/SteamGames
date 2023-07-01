import pandas as pd
import os
import logging
from Modules.urlcreate import UrlCreate
from Modules.urlresponse import UrlResponse
from Modules.formatresponse import FormatResponse
from Modules.filehelper import FileHelper
from constants.columns import ColumnsGames

class SteamGames:
    def __init__(self):
        file = FileHelper()
        self.columns = ColumnsGames()
        self.users = file.open_file()

    def do_url(self, API_KEY, USER_ID):
        url_create = UrlCreate()
        self.url = url_create.create_url(API_KEY=API_KEY, USER_ID=USER_ID)
        return self.url
    
    def get_response(self, url):
        url_response = UrlResponse()
        self.response = url_response.get_response(url)
        return self.response 

    def format_response(self, response):
        format_response = FormatResponse()
        self.df_response = format_response.format_response(response)
        return self.df_response
    
    def concat_df(self, dfs):
        self.df_concat = pd.concat(dfs)
        self.df_concat = (self.df_concat.sort_values(self.columns.DF_PERSONAL[1], ascending=False)
                                                                            .reset_index(drop=True))
        return self.df_concat
    
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
