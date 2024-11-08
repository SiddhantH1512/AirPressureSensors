from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd 
import os,sys
from sensor.entity.config_entity import data_ingestion_config
from sensor.entity.artefacts import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData

class DataIngestion:
    def __init__(self, data_ingestion_config: data_ingestion_config):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)
    
    def export_data_to_feature_store(self):
        
        try:
            logging.info("Exporting data from mongodb to feature store")

            sensor_data = SensorData()

            dataframe = sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            
            feature_store_file_path = self.data_ingestion_config.feature_store_dir            

            logging.info(f"Saving the feature store file: [{feature_store_file_path}]")

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        
        except  Exception as e:
            raise  SensorException(e,sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info("Performed train test split on the dataframe")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_dir)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file.")

            train_set.to_csv(self.data_ingestion_config.training_file_dir, index=False, header=True)

            test_set.to_csv(self.data_ingestion_config.testing_file_dir, index=False, header=True)

            logging.info(f"Exported train and test file.")
        except Exception as e:
            raise SensorData(e,sys)
    
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_data_to_feature_store()

            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_dir,test_file_path=self.data_ingestion_config.testing_file_dir)

            return data_ingestion_artifact
        
        except Exception as e:
            raise SensorException(e,sys)

