from app.public_views import *
from app.methods.decorators import anonymous_only


@app.route("/singup/login")
@anonymous_only
def login_sing_up_choice():

    return render_template('public/singup_or_login.html',
                           user=current_user,
                           title='Login / Sign Up')
