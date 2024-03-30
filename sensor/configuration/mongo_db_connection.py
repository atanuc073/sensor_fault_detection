import pymongo
from pymongo import MongoClient
from sensor.constant.database import DATABASE_NAME
from pymongo.server_api import ServerApi
import certifi
ca=certifi.where()
print(DATABASE_NAME)

class MongoDBClient:
    client=None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url="mongodb+srv://atanu:atanu_mongoDB@ssensor.rqglebz.mongodb.net/?retryWrites=true&w=majority&appName=ssensor"
                # MongoDBClient.client=pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
                client = MongoClient(mongo_db_url, server_api=ServerApi('1'))
            self.client=MongoDBClient.client
            self.database=self.client.get_database(database_name)
            self.database_name=database_name
        except Exception as e:
            raise e