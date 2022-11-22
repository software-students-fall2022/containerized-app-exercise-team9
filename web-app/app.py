from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO = os.getenv('MONGO_REMOTE')
client = MongoClient(MONGO)

app = Flask(__name__)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)