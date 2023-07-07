from flask import render_template
from flask_login import current_user
from werkzeug.exceptions import HTTPException
from app import app


@app.errorhandler(423)
def custom400(error):
    e = "You Cant do This When you are Logged in "

    return render_template("error/error.html", title=e,
                           user=current_user)


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        e = e
    else:
        e = e
    return render_template("error/error.html", title=e,
                           user=current_user)
