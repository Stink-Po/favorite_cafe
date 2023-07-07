from app.private_views import *
from app.methods.decorators import anonymous_only
from app.forms.check_email_form import CkeckEmailForm
from app.forms.chnage_password_form import ChangePassword
from app.methods.user_manager import UserManager
from app.methods.send_mail import SendForgotPasswordEmail, AuthForgotPassword
from flask import url_for

"""this Routes will handel the forgot password auth the token send email ..."""


@app.route('/check-email', methods=['POST', 'GET'])
@anonymous_only
def check_user_email():
    user_manager = UserManager()
    form = CkeckEmailForm()

    if request.method == 'POST' and form.validate_on_submit():

        user_object = user_manager.find_user_by_email(email=form.email.data)

        if user_object:

            email_sender = SendForgotPasswordEmail(user_email=user_object.email, user=user_object)
            email_sender.send_email()
            message = f"Rest Password  Link  Successfully send To {form.email.data} Link will Available for Next " \
                      f"One Hour "
            return render_template("public/message.html",
                                   user=current_user,
                                   message=message)
        else:

            flash(message=f"Sorry We dont have any user with {form.email.data} Email ")

    return render_template('public/check_email.html',
                           user=current_user,
                           title="Recover Account",
                           form=form)


@app.route('/rest-password/<token>')
@anonymous_only
def rest_user_password(token):
    auth = AuthForgotPassword(token=token)

    if auth.rest:

        user_manager = UserManager()
        user_id = int(request.args.get('user_id'))
        user_object = user_manager.find_user(user_id=user_id)
        return redirect(url_for('private.rest', user_id=user_object.id))

    else:

        message = auth.message
        return render_template("public/message.html",
                               user=current_user,
                               message=message)


@app.route('/rest-user-password/<int:user_id>', methods=['POST', 'GET'])
@anonymous_only
def rest(user_id):
    form = ChangePassword()

    if request.method == "POST" and form.validate_on_submit():

        new_password = form.password.data
        user_manager = UserManager()
        this_user = user_manager.find_user(user_id=user_id)

        if this_user:

            user_manager.update_password(new_password=new_password, user_id=this_user.id)
            login_user(this_user, remember=True)
            user_manager.active_user(this_user.id)
            message = 'Your Password Successfully Updated'
            msg = SendForgotPasswordEmail(user_email=this_user.email, user=this_user)
            msg.send_email_to_remain_password_changed()

            return render_template("public/message.html",
                                   user=current_user,
                                   message=message)

        else:

            flash(message="invalid Request Please Request a New Link")

    return render_template('private/rest_password.html',
                           user=current_user,
                           title='Rest Password',
                           form=form)
