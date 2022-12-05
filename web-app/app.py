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

def result_to_arr(result):
  data = []
  misc = ["screen_text", "ouput_text", "_id", "time_created"]

  for ele in result: 
    for prop in ele: 
      if (prop in misc):
        string = ele[prop]
        data.append(string)
      else:
        num = (round(float(ele[prop]),2))
        data.append(num)
  return data

  
@app.route("/") 
def results_home(): 
  result = db.results.find({}).sort("_id", -1).limit(1)

  return render_template("result.html", result=result_to_arr(result))


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
      if (prop != "_id"):
        clean = (round(float(doc[prop]),2))
        data.append(clean)


  return render_template("all.html", documents = db.results.find({}).sort("_id", -1), data = data, size = db.results.count_documents({}))

@app.route("/view/<id>")
def view_details(id):
  findId = ObjectId(id)
  result = db.results.find_one({"_id": findId})
  
  result = db.results.find({}).sort("_id", -1).limit(1)
  data = []

  misc = ["screen_text", "ouput_text", "_id", "time_created"]

  for ele in result: 
    for prop in ele: 
      if (prop in misc):
        string = ele[prop]
        data.append(string)
      else:
        num = (round(float(ele[prop]),2))
        data.append(num)

  idx = 0
  for point in data:
    print(idx, ": ", point)
    print()
    idx = idx+1


  return render_template("result.html", result=data)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)