from app.public_views import *
from app.forms.add_vote_form import VoteForm
from app.methods.cafe_vote_manager import VotingManager
from app.methods.database_methods import DataBaseInfo
from app.methods.cafe_manager import CafeManager
from app.methods.decorators import lover_only


@app.route('/vote_cafe', methods=['POST', 'GET'])
@login_required
@lover_only
def voting():
    cafe_manager = CafeManager()
    data_base_info = DataBaseInfo()
    cafe_id = int(request.args.get('cafe_id'))
    country_id = request.args.get('country_id')
    city = request.args.get('city')
    cafe = data_base_info.ret_a_cafe_with_id(cafe_id=cafe_id)
    vote_manager = VotingManager(user=current_user, cafe=cafe)
    form = VoteForm()
    print(vote_manager.voted)
    if request.method == 'POST' and form.validate_on_submit():
        if not vote_manager.voted:
            cafe_manager.calculate_new_total_scores(cafe_id=cafe_id,
                                                    user_id=current_user.id,
                                                    new_coffe_score=form.coffee_score.data,
                                                    new_wifi_score=form.wifi_score.data,
                                                    new_power_score=form.power_score.data)

            return redirect(url_for('load_cafe', cafe_id=cafe_id, country_id=country_id, city=city))
        else:
            flash(message="You Voted Before")

    return render_template('private/voting.html', user=current_user,
                           form=form,
                           vote_manager=vote_manager)
