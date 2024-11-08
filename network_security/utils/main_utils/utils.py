import yaml
import os,sys
import numpy as np
from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging
# from network_security.utils.main_utils import read_yaml_file,write_yaml_file
import dill
import pickle

def read_yaml_file(file_path: str):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def write_yaml_file(file_path: str, content: object, replace: bool=False)-> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path))
            with open(file_path,'w') as file:
                yaml.dump(content,file)



    except Exception as e:
        raise NetworkSecurityException(e,sys)