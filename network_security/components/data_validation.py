import os,sys
import pandas as pd
from scipy.stats import ks_2samp
from network_security.entity.config_entity import DataValidationConfig
from network_security.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from network_security.logger.logger import logging
from network_security.exception.exception import NetworkSecurityException
from network_security.utils.main_utils.utils import read_yaml_file,write_yaml_file
from network_security.constants.training_pipeline import SCHEMA_FILE_PATH





class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact ,data_validation_config:DataValidationConfig ):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def validate_number_of_columns(self,dataframe:pd.DataFrame) ->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            #Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)
            
            #Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"{error_message}Train dataframe does not contain all columns.\n"
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f"{error_message}Test dataframe does not contain all columns.\n"    
            #if len(error_message)>0:
                #raise Exception(error_message)



            
        except Exception as e:
            raise NetworkSecurityException(e,sys)




    
        
    
