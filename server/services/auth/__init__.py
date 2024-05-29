# describe admin user column in db
from werkzeug.security import generate_password_hash, check_password_hash

from server import db
from server.database.models.User import User


def create_user(username, password, role):
    if User.query.filter_by(username=username).first():
        raise Exception(f"the user with the username {username} already does exist")
    user = User(username=username, password=generate_password_hash(password), role=role)
    db.session.add(user)
    db.session.commit()
    return user


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        raise Exception(f"such the user with id {user_id} does not exist!")
    return user


def log_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise Exception(f"such the user {username} does not exist!")
    if not check_password_hash(user.password, password):
        raise Exception(f"incorrect parameters provided")
    return user


def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
