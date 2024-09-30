# from sensor.utils import send_data_files_to_mongodb
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    # file_path_train:str = "/Users/siddhant/Desktop/Sensors/AirPressureSensors/Data/aps_failure_training_set.csv"
    # database_name:str = "APSensors"
    # collections_name:str = "AirPressure"

    # send_data_files_to_mongodb(file_path_train, database_name, collections_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()