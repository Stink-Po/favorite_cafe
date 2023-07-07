from app.public_views import *
from app.methods.follow_unfollow import FollowManager
from app.forms.comment_form import AddCommentForm
from app.methods.cafe_vote_manager import VotingManager
from bleach.sanitizer import Cleaner
from app.methods.review_manager import ManageReview
from app.my_db_models.menu_model import CafeMenu


def sanitize_input(text):
    if text is None:
        return ''
    cleaner = Cleaner(tags=['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul'],
                      attributes={'a': ['href', 'title']})
    return cleaner.clean(text)


@app.route("/cafe", methods=["POST", "GET"])
def load_cafe():
    menu = CafeMenu()
    voted = False
    form = AddCommentForm()
    following = False
    data_base_info = DataBaseInfo()
    cafe_id = request.args.get('cafe_id')
    country_id = request.args.get('country_id')
    city = request.args.get('city')
    city_data = data_base_info.ret_a_city_with_name(city_name=city)
    country_data = data_base_info.ret_a_country_with_id(country_id=int(country_id))
    cafe_data = data_base_info.ret_a_cafe_with_id(cafe_id=int(cafe_id))
    try:
        menu_dict = menu.find_cafe_menu(_id=cafe_data.menu_id)
    except Exception as e:
        print(e.args)
        menu_dict = None
    if current_user.is_authenticated:
        vote_manager = VotingManager(user=current_user, cafe=cafe_data)
        follow_mng = FollowManager(user=current_user, cafe=cafe_data)
        following = follow_mng.is_following()
        voted = vote_manager.voted
        if request.method == 'POST' and form.validate_on_submit():
            if not current_user.is_owner:
                review_manager = ManageReview()
                sanitized_text = sanitize_input(form.comment_text.data)
                review_manager.add_review(text=sanitized_text,
                                          review_author=current_user,
                                          parent_cafe=cafe_data)

    return render_template('public/cafe.html',
                           user=current_user,
                           country_data=country_data,
                           cafe_data=cafe_data,
                           city_data=city_data,
                           form=form,
                           following=following,
                           voted=voted,
                           sanitize_input=sanitize_input,
                           title=cafe_data.name,
                           menu_dict=menu_dict)
