from app.private_views import *
from app.forms.change_mail_form import ChangeEmail
from app.methods.user_manager import UserManager
from app.auth.chnage_email_auth import EmailAuth


@app.route('/change_email', methods=['POST', 'GET'])
@login_required
def change_email():
    form = ChangeEmail()
    user_manager = UserManager()
    if request.method == 'POST' and form.validate_on_submit():
        check_email = EmailAuth(email=form.email.data)

        if not check_email.repeated_email:
            user_manager.update_email(user_id=current_user.id, new_email=form.email.data)
            message = "Your Email Change Successful"
            return render_template('public/message.html', user=current_user, message=message)

        elif check_email.repeated_email:
            flash("This Email Is Taken")

    return render_template('private/change_email.html',
                           user=current_user,
                           form=form)
