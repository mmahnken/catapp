"""Seed process for cats app database."""

from model import connect_to_db, db, Cat


def seed_cats():
    """Seed cats."""

    auden = Cat(name="Auden")
    ezra = Cat(name="Ezra")
    db.session.add(auden)
    db.session.add(ezra)
    db.session.commit()

if __name__ == "__main__":
    from flask import Flask   # make fake app
    app = Flask(__name__)
    connect_to_db(app)        # connect DB to it

    db.create_all()           # make tables
    seed_cats()               # seed starter data
