import os
import sys

from network_security.exception.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.pipeline.training_pipeline import TrainingPipeline

def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

if __name__=='__main__':
    model_trainer=TrainingPipeline()
    model_trainer.run_pipeline()

