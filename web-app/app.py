from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO = os.getenv('MONGO_REMOTE')
client = MongoClient(MONGO)


app = Flask(__name__)
db = client["textToSpeech"]

@app.route("/") 
def results_home(): 
  ## not the right way to find the last result, just a test
  result = db.results.find_one({"screen_text": "This is a test"})
  return render_template("result.html", result=result)


@app.route("/all")
def display_all():
  return render_template("all.html", documents = db.results.find({}))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)