from flask_restful import abort
from app.methods.api_manager import ApiInfo
from functools import wraps
from flask import request


def is_valid(api_key):
    api_info = ApiInfo()
    device = api_info.find_api_key(user_key=api_key)
    if device and device is not None:
        return True


def api_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if request.headers:
            api_key = request.headers['api-key']
        else:
            api_key = None
            abort(400, message='Please provide an API key')
        # Check if API key is correct and valid
        if request.method == "GET" and is_valid(api_key):
            return func(*args, **kwargs)
        else:
            abort(401, message="The provided API key is not valid")

    return decorator
