from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId

import os

load_dotenv()
MONGO = os.getenv('MONGODB_CONNSTRING')
client = MongoClient(MONGO)
from handler import handle


app = Flask(__name__)
db = client["textToSpeech"]

@app.route("/")
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
  name = ""

  data = []
  # command cursor to iterable object 
  for doc in agg: 
    for prop in doc: 
      if (prop != "_id"):
        clean = (round(float(doc[prop]),2))
        data.append(clean)


  return render_template("all.html", documents = db.results.find({}).sort("_id", -1), data = data, size = db.results.count_documents({}))

@app.route("/view/<id>")
def view_details(id):
  findId = ObjectId(id)
  result = db.results.find_one({"_id": findId})

  data = []

  misc = ["screen_text", "ouput_text", "_id", "time_created", "name"]
  name = ""

  for prop in result: 
    if (prop in misc):
      string = result[prop]
      data.append(string)
    else:
      num = (round(float(result[prop]),2))
      data.append(num)
    if prop == 'name':
      name = result[prop]

  idx = 0
  for point in data:
    print(idx, ": ", point)
    print()
    idx = idx+1


  return render_template("result.html", result=data, name=name)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)