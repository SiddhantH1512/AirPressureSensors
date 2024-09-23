import os

TARGET_COLUMN = "target"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
PIPELINE_SAVE_FILE = "sensor.pkl"
TRAINING_DATA = "train.csv"
TEST_DATA = "test.csv"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
FILE_NAME = "sensor.csv"


'''
DATAINGESTION CONSTANTS
'''
DATA_INGESTION_COLLECTION_NAME = "sensor"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTED_DIR = "data_ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2