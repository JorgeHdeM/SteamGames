import os
import pandas as pd
import logging
from constants.files import ConstantsFiles

class FileHelper:
    def __init__(self):
        logging.info(f"\n########## Opening users file ##########")
        self.files = os.listdir(os.getcwd())

    def open_file(self):
        for file in self.files:
            if file.endswith(ConstantsFiles.csv):
                try:
                    users_csv = pd.read_csv(file, low_memory=False)
                    users_csv = users_csv.astype(str)
                    logging.info(f"Successfully opened users file - {file}")
                    return users_csv
                except:
                    continue