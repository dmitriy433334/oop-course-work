import os

from .models.User import User
from .models.UserFile import UserFile
from .models.FileComments import FileComment
from server import db, app, db_name, default_admin_username, default_admin_password, PROJECT_ROOT
from server.services.auth import create_user

if not os.path.exists(os.path.join(PROJECT_ROOT, f"instance/{db_name}.db")):
    with app.app_context():
        # create tables and admin user
        db.create_all()
        create_user(default_admin_username, default_admin_password, "admin")