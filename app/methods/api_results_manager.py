from flask import jsonify
from app.methods.database_methods import DataBaseInfo
from app.my_db_models.menu_model import CafeMenu
from bs4 import BeautifulSoup


def remove_html_tags(input_string):
    soup = BeautifulSoup(input_string, 'html.parser')
    return soup.get_text().replace("\n", "")


class APIResult:
    def __init__(self):
        self.db_info = DataBaseInfo()

    def get_many_country(self, count: int = 10):
        all_country = self.db_info.ret_all_country()[:count]
        output = {'result': []}
        for country in all_country:
            local_dict = {
                'country-name': country.country_name,
                'capital': country.capital,
                'phone-cod': country.phone_cod,
                'iso-2': country.iso2,
                'about': country.about
            }
            output['result'].append(local_dict)

        return jsonify(output)

    def get_single_country(self, iso_cod: str):
        data = self.db_info.ret_a_country_with_iso2(iso_2=iso_cod)
        if data:
            output = {'result': [
                {
                    'country-name': data.country_name,
                    'capital': data.capital,
                    'phone-cod': data.phone_cod,
                    'iso-2': data.iso2,
                    'about': data.about
                }
            ]}
        else:
            output = {'result': [
                {
                    'Error 404 - Not Found': 'Invalid iso-2 cod'
                }
            ]
            }
        return jsonify(output)

    def get_many_city(self, iso2: str, count: int = 10):
        country_id = self.db_info.ret_a_country_with_iso2(iso_2=iso2)
        if country_id:
            all_city = self.db_info.ret_all_city_in_country_with_country_id_pop(country_id=country_id.id)[:count]
            output = {'total results': len(all_city), 'result': []}
            for city in all_city:
                local_dict = {
                    'id': city.show_id,
                    'city-name': city.city_name,
                    'population': city.population,
                    'latitude': city.lat,
                    'longitude': city.lng,
                    'about': city.about,
                    'total-cafe': len(self.db_info.ret_all_cafe_in_city_with_city_id(city_id=city.id))
                }
                output['result'].append(local_dict)

        else:
            output = {'result': [
                {
                    'Error 404 - Not Found': 'Invalid iso-2 cod'
                }
            ]
            }

        return jsonify(output)

    def get_single_city_with_show_id(self, show_id):
        data = self.db_info.get_city_with_show_id(show_id=show_id)
        if data:
            output = {'result': [
                {
                    'id': data.show_id,
                    'city-name': data.city_name,
                    'population': data.population,
                    'latitude': data.lat,
                    'longitude': data.lng,
                    'about': data.about,
                    'total-cafe': len(self.db_info.ret_all_cafe_in_city_with_city_id(city_id=data.id))
                }
            ]

            }
        else:
            output = {'result': [
                {
                    'Error 404 - Not Found': 'Invalid city id '
                }
            ]
            }

        return jsonify(output)

    def get_all_cafe_inside_a_city(self, city_show_id):
        data = self.db_info.all_cafe_in_city_with_city_show_id(show_id=city_show_id)
        if data and data != 0:
            output = {'total results': len(data), 'result': []}
            for cafe in data:
                if cafe.menu_id is not None:
                    cafe_menu = CafeMenu()
                    menu = cafe_menu.find_cafe_menu(_id=cafe.menu_id)
                else:
                    menu = []
                reviews = self.db_info.ret_review_of_cafe(cafe_id=cafe.id)
                if reviews:
                    comment_list = []
                    for comment in reviews:
                        cm_dict = {
                            'comment': comment.text
                        }
                        comment_list.append(cm_dict)
                else:
                    comment_list = []
                local_dict = {
                    'id': cafe.show_id,
                    'create_by': cafe.create_by,
                    'name': cafe.name,
                    'overall rating': f"{cafe.cafe_rating}/100",
                    'cafe_theme': cafe.cafe_theme,
                    'open_time': cafe.open_time,
                    'close_time': cafe.close_time,
                    'address': cafe.address,
                    'phone': cafe.phone,
                    'coffee_score': f"{cafe.coffee_score}/100",
                    'wifi_score': f"{cafe.wifi_score}/100",
                    'power_score': f"{cafe.power_score}/100",
                    'total_vote': cafe.total_vote,
                    'can_take_calls': cafe.can_take_calls,
                    'about': remove_html_tags(cafe.about),
                    'followers': len(cafe.followers),
                    'reviews': comment_list,
                    'cafe_menu': menu,
                }
                output['result'].append(local_dict)
        elif data or data == 0:
            output = {'result': [
                {
                    'Records- Not Found': 'We Dont have any record for cafe inside this city'
                }
            ]
            }
        else:
            output = {'result': [
                {
                    'Error 404 - Not Found': 'Invalid city id '
                }
            ]
            }

        return output

    def get_single_cafe_with_show_id(self, show_id):
        data = self.db_info.get_a_cafe_with_show_id(show_id=show_id)
        if data:
            if data.menu_id is not None:
                cafe_menu = CafeMenu()
                menu = cafe_menu.find_cafe_menu(_id=data.menu_id)
            else:
                menu = []

            reviews = self.db_info.ret_review_of_cafe(cafe_id=data.id)
            if reviews:
                comment_list = []
                for comment in reviews:
                    cm_dict = {
                        'comment': comment.text
                    }
                    comment_list.append(cm_dict)
            else:
                comment_list = []

            output = {'result': [
                {
                    'id': data.show_id,
                    'create_by': data.create_by,
                    'name': data.name,
                    'overall rating': f"{data.cafe_rating}/100",
                    'cafe_theme': data.cafe_theme,
                    'open_time': data.open_time,
                    'close_time': data.close_time,
                    'address': data.address,
                    'phone': data.phone,
                    'coffee_score': f"{data.coffee_score}/100",
                    'wifi_score': f"{data.wifi_score}/100",
                    'power_score': f"{data.power_score}/100",
                    'total_vote': data.total_vote,
                    'can_take_calls': data.can_take_calls,
                    'about': remove_html_tags(data.about),
                    'followers': len(data.followers),
                    'reviews': comment_list,
                    'cafe_menu': menu,
                }
            ]}
        else:
            output = {'result': [
                {
                    'Error 404 - Not Found': 'Invalid cafe id '
                }
            ]
            }

        return jsonify(output)
