import os
import sys
import pandas as pd
import numpy as np

from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.artifact_entity import DataIngestionArtifact

import pymongo
from typing import List

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

class DataIngestion:
    def __init__(self):
        pass

    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)               