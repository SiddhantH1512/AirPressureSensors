import pandas as pd
import numpy as np
import json
from sensor.config import mongo_client

def send_data_files_to_mongodb(file_path:str, database_name:str, collections_name:str)->None:
    try:
        df = pd.read_csv(file_path)
        df.reset_index(drop=True, inplace=True)
        json_records = list(json.loads(df.T.to_json()).values())
        mongo_client[database_name][collections_name].insert_many(json_records)
    
    except Exception as e:
        print(e)