from app.public_views.login import *
from app.forms.login_form import LogInForm
from app.auth.login_auth import UserLoginAuthentication
from flask_login import login_user
from app.methods.user_manager import UserManager
from app.methods.decorators import anonymous_only


@app.route('/user_login', methods=["POST", "GET"])
@anonymous_only
def user_login():
    form = LogInForm()

    if request.method == "POST" and form.validate_on_submit():

        user_auth = UserLoginAuthentication(username=form.user_name.data,
                                            password=form.password.data, )

        if user_auth.login:
            login_user(user_auth.user, remember=True)
            user_manager = UserManager()
            user_manager.active_user(user_id=current_user.id)
            return redirect(url_for("index"))
        if not user_auth.login:
            flash(message="invalid username or password")
    return render_template("public/user_login.html",
                           user=current_user,
                           title="Log in",
                           form=form)

#
