from app.public_views.country import *


@app.route("/country/<name>", methods=['GET', 'POST'])
def load_country(name):
    select = request.args.get('select')
    data_base_info = DataBaseInfo()
    country_data = data_base_info.ret_a_country_with_name(country_name=name)
    city_data_alpha = data_base_info.ret_all_city_in_country_with_country_id_alpha(country_id=country_data.id)
    city_data_pop = data_base_info.ret_all_city_in_country_with_country_id_pop(country_id=country_data.id)
    img = GetPhoto(search_object=name)
    images = img.final
    if select == "1":
        city_data = city_data_alpha
    elif select == "2":
        city_data = city_data_pop
    else:
        city_data = city_data_alpha
        select = "0"
    print(select)
    return render_template("public/load_country.html",
                           user=current_user,
                           data=country_data,
                           title=country_data.country_name,
                           images=images,
                           city_data=city_data,
                           select=select)
