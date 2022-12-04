from flask import Flask, render_template, request
from generate_text import get_random_quote
from werkzeug.utils import secure_filename
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
    if request.method == 'POST':
        text = request.form['text']
        f = request.files['file']
        filename = secure_filename(f.filename)

        file_path = app.config['UPLOAD_FOLDER'] + filename

        f.save(file_path)

        transcription_data = generate_statistics(text, file_path, 'google')
        
        try:
          Database.initialize()
          print(Database.insert_one("results", transcription_data))
          Database.close()
        except Exception as e:
          print("Failed to insert data to database: ", e)
        
    return render_template('index.html', text=text) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

