import os
import sys

db_name = 'app'
default_admin_username = 'admin'  # this is first username/password of admin when you're logged
default_admin_password = 'admin'

SECRET_KEY = 'secret key fff'  # it's secret key for admin authorization and static salt for password in db

PROJECT_ROOT = sys.path[0]
PERMITTED_FILE_EXTENSIONS = ['application/pdf']
USER_FILES_DIRECTORY = os.path.join(PROJECT_ROOT, "files")
