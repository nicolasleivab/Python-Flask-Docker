from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
