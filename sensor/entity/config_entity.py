from datetime import datetime
import sensor.constant.training_pipeline as training_pipeline
import os


class training_pipeline_config:
    def __init__(self, timestamp:datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artefact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp = timestamp


class data_ingestion_config:
    def __init__(self, training_pipeline_config: training_pipeline_config):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artefact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_dir: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME)
        self.training_file_dir: str = os.path.join(self.data_ingestion_dir, training_pipeline.TRAINING_DATA)
        self.testing_file_dir: str = os.path.join(self.data_ingestion_dir, training_pipeline.TEST_DATA)
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME