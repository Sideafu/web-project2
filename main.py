import flask
app = flask.Flask(__name__)

@app.route("/")
def main.py():
  return render_template("html.html", text="hello world!")

app.run()
