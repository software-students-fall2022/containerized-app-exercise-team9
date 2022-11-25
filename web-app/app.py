from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO = os.getenv('MONGO_REMOTE')
client = MongoClient(MONGO)


app = Flask(__name__)
db = client["textToSpeech"]
# relevant collection name = outputs

@app.route("/") 
def results_home(): 
  # connect to collection 
  # search for user in connection based on name entered
  # display most recent results 
 return render_template("index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)