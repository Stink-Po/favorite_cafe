from app.public_views import *
from app.methods.sub_manager import SubManager


@app.route("/subs", methods=["GET", "POST"])
def sub():
    if request.method == "POST":
        sub_email = request.form.get('femail')
        if sub_email:
            SubManager(email=sub_email)

    return redirect(url_for('index'))
