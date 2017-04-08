"""Models for cats app."""

from flask_sqlalchemy import SQLAlchemy

PG_URL = "postgresql:///cats"
db = SQLAlchemy()


class Cat(db.Model):
    """Feline."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


def connect_to_db(app):
    """Connect Flask to PostgreSQL."""

    app.config.update({
        'SQLALCHEMY_DATABASE_URI': PG_URL,
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    })
    db.app = app
    db.init_app(app)
