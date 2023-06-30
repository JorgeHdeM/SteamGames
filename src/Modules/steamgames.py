import pandas as pd
from Modules.urlcreate import UrlCreate
from Modules.urlresponse import UrlResponse
from Modules.formatresponse import FormatResponse
from Modules.filehelper import FileHelper

class SteamGames:
    def __init__(self):
        file = FileHelper()
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
        return self.df_concat