from flask_pymongo import pymongo
from dotenv import dotenv_values, load_dotenv

def get_recordings_collection():
  config = dotenv_values(".env")
  CONNECTION_STRING = config["MONGO_URI"]
  client = pymongo.MongoClient(CONNECTION_STRING)
  try:
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database["textToSpeech"]
    return pymongo.collection.Collection(db, "recordings")
  except Exception as e:
    print("Could not connect to MongoDB: %s" % e)
  except pymongo.errors.ConnectionFailiure as e:
    print("Could not connect to MongoDB: %s" % e)

recordings_collection = get_recordings_collection()