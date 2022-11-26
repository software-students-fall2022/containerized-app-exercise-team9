from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO = os.getenv('MONGO_REMOTE')
client = MongoClient(MONGO)


app = Flask(__name__)

@app.route("/") 
def home(): 
 return render_template("index.html")

@app.route("/record") 
def record(): 
 return render_template("record.html")

@app.route("/results") 
def results(): 
 return render_template("results.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)