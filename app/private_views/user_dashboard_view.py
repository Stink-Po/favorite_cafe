from app.private_views import *
from app.methods.user_manager import UserManager
from app.forms.avatar_form import AvatarForm
from app.methods.upload_photo import UploadPhoto


@app.route("/dashboard", methods=['POST', 'GET'])
@login_required
def load_dashboard():
    form = AvatarForm()
    upload_photo = UploadPhoto()
    user_manager = UserManager()
    if request.method == 'POST' and form.validate_on_submit():
        upload_photo.upload_user_image(form.image.data, user_id=current_user.id)
        path = upload_photo.image_path
        user_manager.add_user_image(current_user.id, image_path=path)
    user_manager.find_user_activity(user=current_user)
    total_cafe_added = user_manager.total_cafe_added
    total_review = user_manager.total_review
    user_api_key = user_manager.find_user_api_key(user_id=current_user.id)
    return render_template("private/dashboard.html", user=current_user,
                           total_review=total_review,
                           total_cafe_added=total_cafe_added,
                           form=form,
                           api_key=user_api_key,
                           title=f'{current_user.username} Dashboard')
