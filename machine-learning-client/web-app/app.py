from flask import Flask, render_template
from generate_text import get_random_quote

app = Flask(__name__)

# routes
@app.route("/")
def index():
  text = get_random_quote()
  
  return render_template("index.html", text=text)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

