from app.private_views.logout import *
from flask import url_for


@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for("index"))
