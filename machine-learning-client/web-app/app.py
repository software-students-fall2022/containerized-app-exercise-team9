from flask import Flask, render_template, request, redirect, url_for, make_response
import pymongo
import datetime


# instantiate the app
app = Flask(__name__)

# register env
import credentials
config = credentials.get()

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
  app.debug = True

# connect to the database
app.config['MONGO_URI'] = config['MONGO_URI']
mongo = pymongo(app)

db = mongo.db

# routes
@app.route('/')
def index():
  """"
  Route for home page
  """
  return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
  """
  Route for POST requests to the recoding page
  Accepts the form submission data for a new recording
  """
  name = request.form['name']
  recording = request.form['recording']
  text = request.form['text']
  transcription = request.form['transcription']
  doc = {
    'name': name,
    'text': text,
    'recording': recording,
    'transcription': transcription,
    'created_at': datetime.datetime.utcnow()
  }
  db.recordings.insert_one(doc)
  return redirect(url_for('results'))

@app.route('/results')
def results():
  """
  Route for GET requests to the results page
  """
  docs = db.recordings.find({}).sort('created_at', -1)
  return render_template('results.html', docs=docs)

if __name__ == '__main__':
  app.run(debug = True)

