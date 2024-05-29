import json

from flask import url_for, request, render_template, redirect, send_from_directory
from flask_login import login_required, logout_user

from server import app, USER_FILES_DIRECTORY
# from server.services.users import get_all_users, get_user_info, delete_user, create_new_user
from flask_login import current_user

from server.controllers.role_required import role_required
from server.services.auth import delete_user, get_user
from server.services.user_files import get_user_files
from server.services.users import get_all_users


@app.route('/dashboard', methods=['GET'])
@role_required("admin")
def dashboard():
    users = get_all_users()
    users = [user for user in users if user.role != "admin"]
    return render_template("/admin/dashboard.html", users=users)


@app.route('/admin/user/<int:user_id>')
@role_required("admin")
def user_page(user_id):
    try:
        user = get_user(user_id)
        files = get_user_files(user_id)
        return render_template('/admin/user_page.html', user=user, files=files)
    except Exception as e:
        return json.dumps({
            "message": f"{e}"
        })
