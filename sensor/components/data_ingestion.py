from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from pandas import DataFrame
import os,sys
from utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.data_access.sensor_data import SensorData

class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e,sys)
        
    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export Mongo DB Collecction record as data frame into feaature
    
        """

        try :
            logging.info("Exporting data from mongodb into feature")
            sensor_data =SensorData()
            dataframe=sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
        
            # Creating the folder
            dir_path
