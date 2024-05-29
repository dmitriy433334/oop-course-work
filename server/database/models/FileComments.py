from server import db
from . import UserFile


class FileComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_id = db.Column(db.Integer, db.ForeignKey("user_file.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<FileComment {}>".format(self.id)
