from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId

import os

load_dotenv()
MONGO = os.getenv('MONGO_REMOTE')
client = MongoClient(MONGO)


app = Flask(__name__)
db = client["textToSpeech"]

@app.route("/") 
def results_home(): 
  result = db.results.find({}).sort("_id", -1).limit(1)
  print(result[0])
  return render_template("result.html", result=result[0])


@app.route("/all")
def display_all():

  group = {"$group": {
        "_id": "null",
        "avg_time_taken": { "$avg": "$time_taken"},
        "avg_accuracy": { "$avg": "$accuracy"},
        "avg_words_spoken": { "$avg": "$words_spoken"},
        "avg_correct_spoken": { "$avg": "$correct_words_spoken"},
        "avg_total_wps": { "$avg": "$total_words_per_second"},
        "avg_correct_wps": { "$avg": "$correct_words_per_second"},
    }
  }

  agg = db.results.aggregate([group])

  data = []
  # command cursor to iterable object 
  for doc in agg: 
    for prop in doc: 
      print(prop)
      if (prop != "_id"):
        clean = (round(float(doc[prop]),2))
        data.append(clean)


  return render_template("all.html", documents = db.results.find({}).sort("_id", -1), data = data, size = db.results.count_documents({}))

@app.route("/view/<id>")
def view_details(id):
  findId = ObjectId(id)
  info = db.results.find_one({"_id": findId})
  print(info)
  return render_template("result.html", result=info)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)