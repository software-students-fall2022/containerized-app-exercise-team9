from flask import Flask, render_template, request
from generate_text import get_random_quote
from transcribe_audio import generate_statistics
from mongodb import Database

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"
# routes
@app.route("/")
def index():
  text = get_random_quote()
  return render_template("index.html", text=text)


@app.route('/', methods = ['GET', 'POST'])
def save_file():
    transcribed_text=''
    if request.method == 'POST':
        text = request.form['text']
        f = request.files['file']

        transcription_data = generate_statistics(text, f, 'google')
        
        try:
          Database.initialize()
          print(Database.insert_one("results", transcription_data))
          Database.close()
          transcribed_text = transcription_data['ouput_text']
        except Exception as e:
          print("Failed to insert data to database: ", e)
        
    return render_template('index.html', text=text, transcribed_text=transcribed_text) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

