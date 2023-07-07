from app.private_views import *
from app.auth.login_auth import UserLoginAuthentication
from app.forms.password_form import PasswordForm
from app.forms.chnage_password_form import ChangePassword
from app.methods.user_manager import UserManager
from flask import url_for


@app.route("/check_password", methods=['POST', 'GET'])
@login_required
def check_pass():
    form = PasswordForm()
    if request.method == 'POST':
        auth = UserLoginAuthentication(username=current_user.username, password=form.password.data)
        if auth.check_password():
            print(auth.check_password())
            return redirect(url_for('change_pw'))

    return render_template('private/check_pass.html', user=current_user, form=form)


@app.route('/change_password', methods=['POST', 'GET'])
@login_required
def change_pw():
    form = ChangePassword()
    user_manager = UserManager()
    if request.method == 'POST' and form.validate_on_submit():
        this_user = user_manager.find_user(user_id=current_user.id)
        if this_user:
            user_manager.update_password(new_password=form.password.data, user_id=this_user.id)
            login_user(this_user, remember=True)
            user_manager.active_user(this_user.id)
            message = 'Your Password Successfully Updated'
            msg = SendForgotPasswordEmail(user_email=this_user.email, user=this_user)
            msg.send_email_to_remain_password_changed()
            return render_template("public/message.html",
                                   user=current_user,
                                   message=message)

    return render_template('private/rest_password.html',
                           user=current_user,
                           title='Rest Password',
                           form=form)
