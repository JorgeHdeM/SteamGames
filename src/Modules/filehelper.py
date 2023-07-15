import os
import pandas as pd
import logging
from constants.files import ConstantsFiles


class FileHelper:
    def __init__(self):
        logging.info(f"\n########## Opening users file ##########")
        pass

    def open_file(self):
        keys = []
        users = []
        names = []
        try:
            df_names = pd.read_csv('users.csv')
            for name in df_names[df_names.columns[0]]:
                keys.append(os.getenv(name+"Key"))
                users.append(os.getenv(name+"User"))
                names.append(name)
            users_csv = pd.DataFrame({'API_KEY':keys, 'USER_ID':users, "Name":names})
            return users_csv
        
        except:
            logging.error("No CSV file found.")