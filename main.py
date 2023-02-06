import flask
app = flask.Flask(__name__)


@app.route("/")
def main():
    return flask.render_template("index.html", text="hello world!")


app.run()
