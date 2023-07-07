from functools import wraps
from flask import abort
from flask_login import current_user


def confirmed_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            return abort(403)

        return f(*args, **kwargs)

    return decorated_function


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return abort(403)

        return f(*args, **kwargs)

    return decorated_function


def owner_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_owner:
            return abort(403)

        return f(*args, **kwargs)

    return decorated_function


def lover_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_owner:
            return abort(403)

        return f(*args, **kwargs)

    return decorated_function


def anonymous_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return abort(423)

        return f(*args, **kwargs)

    return decorated_function
