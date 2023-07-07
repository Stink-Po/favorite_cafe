from app.public_views import *


@app.route('/signin-options')
def signin_options():
    return render_template('public/signin-choice.html',
                           user=current_user,
                           title='Sign In Options')
