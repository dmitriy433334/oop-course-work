from functools import wraps
from flask import url_for, redirect
from flask_login import current_user


def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user or not current_user.is_authenticated:
                return redirect(url_for("index_page"))
            if current_user.role != role:
                return "You don't have permission to see this page"
            return func(*args, **kwargs)

        return wrapper

    return decorator
