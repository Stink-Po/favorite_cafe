from app.public_views.singin import *
from app.forms.singup_form import SingUpForm
from app.auth.sinup_auth import UserSingUpAuthentication
from flask_login import login_user
from app.methods.user_manager import UserManager
from app.methods.decorators import anonymous_only
from app.methods.counting_news import Counting
from app.methods.send_mail import EmailSender


@app.route('/user-sing-in', methods=["GET", "POST"])
@anonymous_only
def user_sing_in():
    counting = Counting()
    email_sender = EmailSender()
    user_manager = UserManager()
    form = SingUpForm()
    if request.method == "POST":
        print(form.validate_on_submit())
        if form.validate_on_submit():
            auth = UserSingUpAuthentication(username=form.user_name.data,
                                            email=form.email.data)

            if auth.sing_up:
                user_manager.create_new_user(username=form.user_name.data,
                                             email=form.email.data,
                                             password=form.password.data,
                                             owner=False)

                login_user(user_manager.new_user, remember=True)
                email_sender.send_welcome_email()
                user_manager.create_admin_user(user_id=current_user.id)
                user_manager.active_user(user_id=current_user.id)
                counting.add_new_user(user=current_user)
                return redirect(url_for("index"))
            if not auth.sing_up:
                if auth.repeated_username:
                    flash(message="This username is already is use")
                elif auth.repeated_email:
                    flash(message="This email already in use")

    return render_template("public/user_singup.html",
                           user=current_user,
                           form=form,
                           title='Sing up')


@app.route('/owner-sing-in', methods=["GET", "POST"])
@anonymous_only
def owner_sing_in():
    counting = Counting()
    email_sender = EmailSender()
    user_manager = UserManager()
    form = SingUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            auth = UserSingUpAuthentication(username=form.user_name.data,
                                            email=form.email.data)

            if auth.sing_up:
                user_manager.create_new_user(username=form.user_name.data,
                                             email=form.email.data,
                                             password=form.password.data,
                                             owner=True)
                login_user(user_manager.new_user, remember=True)
                email_sender.send_welcome_email()
                counting.add_new_user(user=current_user)
                return redirect(url_for("index"))
            if not auth.sing_up:
                if auth.repeated_username:
                    flash(message="This username is already is use")
                elif auth.repeated_email:
                    flash(message="This email already in use")

    return render_template("public/owner_singup.html",
                           user=current_user,
                           form=form,
                           title='Sing up')
