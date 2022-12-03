from pymongo import MongoClient
from bson.json_util import dumps, loads
from dotenv import dotenv_values


class Database(object):

    config = dotenv_values(".env")
    url = config["MONGO_URI"]
    database=None
    client=None
    
    @staticmethod
    def initialize():
        connection=MongoClient(Database.url)
        try:
            Database.client=connection
            Database.database = connection["textToSpeech"]
            print(' *', 'Connected to MongoDB!') 
        except Exception as e:
            print(' *', "Failed to connect to MongoDB at")
            print('Database connection error:', e)

    @staticmethod
    def insert_one(collection, data):
        return Database.database[collection].insert_one(data)

    @staticmethod
    def close():
        Database.client.close()