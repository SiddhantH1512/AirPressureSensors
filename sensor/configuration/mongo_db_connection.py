from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
from sensor.constant.env_variable import MONGO_DB_URL_KEY
import os
from sensor.logger import logging
from sensor.exception import SensorException


load_dotenv()

class MongoClient:
    client = None
    def get_mongo_client(self, database_name:DATABASE_NAME):
        try:
            if MongoClient.client is None:
                mongo_db_url = os.getenv(MONGO_DB_URL_KEY)
                logging.info(f"MongoDb connection URL: {mongo_db_url}")
                
                if "localhost" in mongo_db_url:
                    MongoClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=certifi.where())
                
            self.client = MongoClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            logging.info(f"Error while connecting to mongoDB: {e}")
            raise 