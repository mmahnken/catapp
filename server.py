"""Flask server for cats app."""

from flask import Flask, render_template
from model import Cat, connect_to_db

app = Flask(__name__)

connect_to_db(app)


@app.route("/")
def homepage():
    """Show list of cats."""

    cats = Cat.query.all()
    return render_template("cats.html",
                           cats=cats)


if __name__ == "__main__":
    app.run(debug=True)
