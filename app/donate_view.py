from app import app
from flask import render_template
from flask_login import current_user


@app.route("/donate")
def donate():
    return render_template('public/donate.html',
                           user=current_user,
                           title='Donate Us')
