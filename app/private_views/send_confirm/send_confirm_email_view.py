from app.private_views.send_confirm import *


@app.route('/send_confirm_email')
@login_required
def send_conformation():
    sender = EmailSender()
    sender.send_confirm_email()
    message = f"Confirm Link sending To {current_user.email} Link will Available for Next One Hour"
    return render_template("public/message.html",
                           user=current_user,
                           message=message)


@app.route("/confirm_email/<token>")
@login_required
def confirm_email(token):
    conformation = ConfirmEmail(token)
    if conformation.confirm:
        message = "Thank You For Confirming Your Email You Can Request an API key now"
        return render_template("public/message.html",
                               user=current_user,
                               message=message)
    elif not conformation.confirm:
        return render_template('public/message.html',
                               user=current_user,
                               message=conformation.message)

