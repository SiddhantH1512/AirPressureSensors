from dataclasses import dataclass
import os
import pymongo

@dataclass
class Env:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")


env_variable = Env()

mongo_client = pymongo.MongoClient(env_variable.mongo_db_url)