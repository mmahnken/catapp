"""Flask server for cats app."""

from flask import Flask, render_template
from model import Cat, connect_to_db

app = Flask(__name__)

connect_to_db(app)


@app.route("/")
def homepage():
    """Simple greeting."""

    return "This is the cat app."


@app.route("/cats")
def cats():
    """Show list of cats."""

    cats = Cat.query.all()
    return render_template("cats.html",
                           cats=cats)


@app.route("/err")
def raise_err():
    """Route that throws error; just for testing."""

    raise Exception("Oh no! A contrived error!")


if __name__ == "__main__":
    app.run()   # NOTE: not in debug mode!
