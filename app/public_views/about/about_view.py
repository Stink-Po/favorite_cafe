from app.public_views.about import *


@app.route('/about-us')
def about():
    return render_template('public/about.html',
                           user=current_user,
                           title='About Favorite Cafe')