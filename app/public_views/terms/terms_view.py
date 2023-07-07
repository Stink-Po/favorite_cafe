from app.public_views.terms import *


@app.route('/terms&Conditions')
def terms():
    return render_template("public/terms.html",
                           user=current_user,
                           title="Terms and Conditions")
