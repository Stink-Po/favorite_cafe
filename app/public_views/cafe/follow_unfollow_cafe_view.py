from app.public_views import *
from app.methods.follow_unfollow import FollowManager
from flask import abort


@app.route("/follow/<int:cafe_id>", methods=["POST"])
@login_required
def follow(cafe_id):
    data_base_info = DataBaseInfo()
    country_id = request.args.get('country_id')
    city = request.args.get('city')
    if request.method == "POST":
        cafe = data_base_info.ret_a_cafe_with_id(cafe_id=cafe_id)
        follow_mng = FollowManager(user=current_user, cafe=cafe)
        follow_mng.follow()
        return redirect(url_for('load_cafe', cafe_id=cafe_id, country_id=country_id, city=city))

    else:
        abort(400)


@app.route("/unfollow/<int:cafe_id>")
@login_required
def unfollow(cafe_id):
    data_base_info = DataBaseInfo()
    country_id = request.args.get('country_id')
    city = request.args.get('city')

    cafe = data_base_info.ret_a_cafe_with_id(cafe_id=cafe_id)
    follow_mng = FollowManager(user=current_user, cafe=cafe)
    follow_mng.unfollow()
    return redirect(url_for('load_cafe', cafe_id=cafe_id, country_id=country_id, city=city))
