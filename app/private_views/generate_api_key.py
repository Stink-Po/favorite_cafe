from app.private_views import *
from app.methods.user_manager import UserManager
from app.methods.send_mail import EmailSender


@app.route('/request_api_key')
@login_required
def create_key():
    if current_user.confirmed:
        user_manager = UserManager()
        email_sender = EmailSender()
        key = user_manager.create_api_key(user_id=current_user.id)
        email_sender.send_api_key(key=key.key)
        return redirect(url_for('private.load_dashboard'))
    else:
        return render_template('public/message.html',
                               user=current_user,
                               message="You Must Confirm Your Email Before Request a API key")
