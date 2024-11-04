import pandas as pd
import numpy as np
import os 
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)



import certifi
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    if __name__=="__main__":
        pass