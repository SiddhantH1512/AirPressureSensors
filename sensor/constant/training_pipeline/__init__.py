import os

TARGET_COLUMN = "target"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
PIPELINE_SAVE_FILE = "sensor.pkl"
TRAINING_DATA = "/Users/siddhant/Desktop/Sensors/AirPressureSensors/Data/aps_failure_training_set.csv"
TEST_DATA = "/Users/siddhant/Desktop/Sensors/AirPressureSensors/Data/aps_failure_test_set.csv"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
FILE_NAME = "sensor.csv"


'''
DATA INGESTION CONSTANTS
'''
DATA_INGESTION_COLLECTION_NAME = "sensor"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTED_DIR = "data_ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

'''
DATA VALIDATION CONSTANTS
'''
DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_INVALID_DIR = "invalid"
DATA_VALIDATION_VALID_DIR = "valid"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"

'''
DATA TRANSFORMATION CONSTANTS
'''
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

'''
MODEL TRAINER CONSTANTS
'''
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05