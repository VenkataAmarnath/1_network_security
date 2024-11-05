import pandas as pd
import numpy as np
import os 
import sys
import json

from dotenv import load_dotenv
import pymongo.mongo_client
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
        
    def csv_to_json(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def pushing_data_to_mongodb(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)

            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__=="__main__":
    FILE_PATH="network_data/NetworkData.csv"
    DATABASE="KrishNaik"
    COLLECTION="NetworkData"
    networobj = NetworkDataExtract()
    records=networobj.csv_to_json(FILE_PATH)
    print("A")
    noofrecords=networobj.pushing_data_to_mongodb(records,DATABASE,COLLECTION)
    print(noofrecords)