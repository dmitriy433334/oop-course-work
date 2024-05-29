from datetime import datetime

from flask_login import UserMixin

from server import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    dateRegistered = db.Column(db.String(120), default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.id)