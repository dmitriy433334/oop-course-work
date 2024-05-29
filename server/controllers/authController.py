import json

from flask import request
from flask_login import login_user, logout_user, login_required, current_user

from server import app
from server.controllers import role_required
from server.services.auth import log_user, create_user, delete_user


@app.route('/auth/login-user', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return json.dumps({
            "message": "parameters are not provided"
        })

    try:
        user = log_user(username, password)
        login_user(user)
        return json.dumps({
            "message": "user logged"
        })
    except Exception as e:
        return json.dumps({
            "message": f"{e}"
        })


@login_required
@app.route("/auth/logout", methods=["POST"])
def logout():
    logout_user()
    return "user logged out"


@app.route("/auth/create-user", methods=["POST"])
def create_user_route():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return json.dumps({
            "message": "parameters are not provided"
        })

    if (len(username) < 7 or len(username) > 100) or (len(password) < 7 or len(password) > 100):
        return json.dumps({
            "message": "username or password is too short or too long"
        })

    try:
        user = create_user(username, password, "usual_user")
        login_user(user)

        return json.dumps({
            "message": "user created"
        })
    except Exception as e:
        return json.dumps({
            "message": f"{e}"
        })


@app.route('/auth/delete-user', methods=['DELETE'])
@role_required("admin")
def delete_user_page():
    try:
        user_id = request.form['user_id']
        delete_user(user_id)
        return json.dumps({
            "message": 'user successfully deleted'
        })
    except:
        return json.dumps({
            "message": "user id is not privded"
        })


@app.route("/auth/is-authorized", methods=["POST"])
def is_authorized():
    isAuthorized = True
    if current_user.is_anonymous:
        isAuthorized = False
    return json.dumps({
        "isAuthorized": isAuthorized
    })
