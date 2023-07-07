from app.private_views.new_cafe import *
from app.forms.add_cafe_form import OwnerAddCafeForm, UserAddCafeForm
from app.methods.upload_photo import UploadPhoto
from app.my_db_models.menu_model import CafeMenu
from app.methods.counting_news import Counting
from flask import abort
from app.methods.decorators import confirmed_only
from flask import url_for


@app.route('/<city>/add_new_cafe', methods=["POST", "GET"])
@login_required
@confirmed_only
def add_cafe(city):
    photo = UploadPhoto()
    cafe_manager = CafeManager()
    data_base_info = DataBaseInfo()
    counting = Counting()
    img = GetPhoto('cafe')
    images = img.final
    this_city = data_base_info.ret_a_city_with_name(city_name=city)

    if not current_user.is_owner:

        cafe_form = UserAddCafeForm()

        if request.method == 'POST' and cafe_form.validate():
            cafe_image = cafe_form.image.data
            image = photo.upload_cafe_image(cafe_image)

            if cafe_form.can_take_calls.data == "Yes":
                can_take_calls = True
            else:
                can_take_calls = False
            if cafe_form.about.data:
                about = cafe_form.about.data
            else:
                about = ""
            coffee_score = cafe_form.coffee_score.data
            wifi_score = cafe_form.wifi_score.data
            power_score = cafe_form.power_score.data

            cafe_manager.add_cafe(
                name=cafe_form.name.data,
                create_by="user",
                address=cafe_form.address.data,
                phone=cafe_form.phone.data,
                open_time=cafe_form.open_time.data.strftime("%H:%M"),
                close_time=cafe_form.close_time.data.strftime("%H:%M"),
                can_take_calls=can_take_calls,
                cafe_theme=cafe_form.cafe_theme.data,
                about=about,
                city_id=this_city.id,
                author=current_user,
                image=image,
                coffee_score=coffee_score,
                wifi_score=wifi_score,
                power_score=power_score,
            )
            if cafe_manager.error:
                return abort(400, message=cafe_manager.error)

            # adding current user vote
            cafe_manager.add_vote(user_id=current_user.id, cafe_id=cafe_manager.new_cafe.id,
                                  wifi_rating=wifi_score, coffee_rating=coffee_score, power_rating=power_score)

            # add this café as a new café in admin panel
            counting.add_new_cafe(cafe=cafe_manager.new_cafe)

            return redirect(url_for('load_city', city=city))

        return render_template("private/user_add_cafe.html",
                               user=current_user,
                               cafe_form=cafe_form,
                               city=city,
                               images=images
                               )

    elif current_user.is_owner:

        cafe_form = OwnerAddCafeForm()

        if request.method == "POST" and cafe_form.validate():
            cafe_image = cafe_form.image.data
            image = photo.upload_cafe_image(cafe_image)
            if cafe_form.can_take_calls.data == "Yes":
                can_take_calls = True
            else:
                can_take_calls = False

            cafe_menu = CafeMenu()
            cafeid = cafe_menu.post_maker(menu_items=request.form.getlist('item[]'),
                                          prices=request.form.getlist('price[]'))
            cafe_manager.add_cafe(
                name=cafe_form.name.data,
                create_by="owner",
                menu_id=cafeid,
                address=cafe_form.address.data,
                phone=cafe_form.phone.data,
                open_time=cafe_form.open_time.data.strftime("%H:%M"),
                close_time=cafe_form.close_time.data.strftime("%H:%M"),
                can_take_calls=can_take_calls,
                cafe_theme=cafe_form.cafe_theme.data,
                city_id=this_city.id,
                author=current_user,
                staff=cafe_form.staff.data,
                image=image
            )
            counting.add_new_cafe(cafe=cafe_manager.new_cafe)
            return redirect(url_for('load_city', city=city))

        return render_template("private/owner_add_cafe.html",
                               user=current_user,
                               cafe_form=cafe_form,
                               city=city,
                               images=images,
                               )
