from sensor.utils import send_data_files_to_mongodb

if __name__ == "__main__":
    file_path_train:str = "/Users/siddhant/Desktop/Sensors/AirPressureSensors/Data/aps_failure_training_set.csv"
    database_name:str = "APSensors"
    collections_name:str = "AirPressure"

    send_data_files_to_mongodb(file_path_train, database_name, collections_name)