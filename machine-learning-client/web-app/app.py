from flask import Flask, render_template, request, redirect, url_for, make_response
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv
import os

from record import record
from results import results

# load_dotenv()
# MONGO = os.getenv('MONGO_URI')
# client = MongoClient(MONGO)

app = Flask(__name__)
# db = client["textToSpeech"]

# routes
@app.route("/") 
def index(): 
  return render_template("index.html")

app.add_url_rule('/results', methods=["GET"], view_func=results)
app.add_url_rule('/record', methods=["POST", "GET"], view_func=record)

# def record():
#   """
#   Route for POST requests to the recoding page
#   Accepts the form submission data for a new recording
#   """
#   name = request.form['name']
#   recording = request.form['recording']
#   text = request.form['text']
#   transcription = request.form['transcription']
#   doc = {
#     'name': name,
#     'text': text,
#     'recording': recording,
#     'transcription': transcription,
#     'created_at': datetime.datetime.utcnow()
#   }
#   db.recordings.insert_one(doc)
#   return redirect(url_for('results.html'))

# @app.route('/results')
# def results():
#   """
#   Route for GET requests to the results page
#   """
#   docs = db.recordings.find({}).sort('created_at', -1)
#   return render_template('results.html', docs=docs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

