from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import *

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./{}.db'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'log_in_page'

from . import database
from .database.models.User import User

import server.controllers

@login_manager.user_loader
def get_user_session(user_id):
    return User.query.get(int(user_id))


# create directory for files if it doesn't have
if not os.path.exists(USER_FILES_DIRECTORY):
    os.makedirs(USER_FILES_DIRECTORY)
