from server import db
from . import User


class UserFile(db.Model):
    __tablename__ = 'user_file'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(256))
    date_created = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<UserFile {}>".format(self.id)
