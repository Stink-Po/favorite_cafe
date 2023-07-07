from app.public_views import *
from app.methods.change_format_methods import ChangeStringsFormation
from app.methods.cafe_manager import CafeManager


@app.route("/city/<city>")
def load_city(city):
    num = request.args.get('num')
    if num:
        num = int(num)
    else:
        num = 1
    cafe_manager = CafeManager()
    data_base_info = DataBaseInfo()
    city_data = data_base_info.ret_a_city_with_name(city_name=city)
    cafe_paginate = cafe_manager.cafe_paginate(num=num)
    country_data = data_base_info.ret_a_country_with_id(country_id=city_data.country_id)
    cafe_data = data_base_info.ret_all_cafe_in_city_with_city_id(city_id=city_data.id)
    img = GetPhoto(search_object=city)
    images = img.final
    formation = ChangeStringsFormation()
    population = formation.change_population_format(population=city_data.population)
    return render_template("public/city.html",
                           user=current_user,
                           data=city_data,
                           title=city_data.city_name,
                           images=images,
                           cafe_data=cafe_data,
                           country_data=country_data,
                           population=population,
                           cafe_paginate=cafe_paginate,
                           num=num)
