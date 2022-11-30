from flask import Flask, render_template, request
from generate_text import get_random_quote
from werkzeug.utils import secure_filename

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
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()
        
        
    return render_template('index.html', content=content) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

