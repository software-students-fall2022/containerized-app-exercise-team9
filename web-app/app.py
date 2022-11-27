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
  agg = db.results.aggregate([
    {
      "$group": {
        "_id": "null",
        "avg_time_taken": { "$avg": "$time_taken"},
        "avg_accuracy": { "$avg": "$accuracy"},
        "avg_words_spoken": { "$avg": "$words_spoken"},
        "avg_correct_spoken": { "$avg": "$correct_words_spoken"},
        "avg_total_wps": { "$avg": "$total_words_per_second"},
        "avg_correct_wps": { "$avg": "$correct_words_per_second"},
      }
    }
  ])

  # command cursor to iterable object 
  # definitely a better way to do this
  for doc in agg: 
    data=doc


  return render_template("all.html", documents = db.results.find({}), data = data, size = db.results.count_documents({}))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)