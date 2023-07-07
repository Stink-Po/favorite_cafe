from flask_restful import Resource
from flask import request
from app.api.auth_key import api_required
from app import api
from app.methods.api_results_manager import APIResult
from app.methods.api_manager import ApiInfo


class AllCountries(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        api_result = APIResult()
        count = request.args.get('count')
        if count:
            try:
                count = int(count)
            except ValueError:
                return {'error': 'Cod must be an integer'}, 406
            return api_result.get_many_country(count=count)
        return api_result.get_many_country()


class GetsingelCountry(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        cod = request.args.get('iso_cod')
        if cod:
            api_result = APIResult()
            return api_result.get_single_country(iso_cod=cod)
        else:
            return {'error': 'Please provide an iso-2'}, 406


class GetManyCity(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        api_result = APIResult()
        cod = request.args.get('iso_cod')
        if cod:
            count = request.args.get('count')
            if count:
                try:
                    count = int(count)
                except ValueError:
                    return {'error': 'Cod must be an integer'}, 406

                return api_result.get_many_city(iso2=cod, count=count)

            return api_result.get_many_city(iso2=cod)
        else:
            return {'error': 'Please provide an iso-2'}, 406


class GetSingelCity(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        api_result = APIResult()
        show_id = request.args.get('id')
        if show_id:
            return api_result.get_single_city_with_show_id(show_id=show_id)
        else:
            return {'error': 'Please provide an city id'}, 406


class GetAllCafeinCity(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        api_result = APIResult()
        show_id = request.args.get('id')
        if show_id:
            return api_result.get_all_cafe_inside_a_city(city_show_id=show_id)
        else:
            return {'error': 'Please provide an city id'}, 406


class GetSingelCafe(Resource):
    @api_required
    def get(self):
        api_info = ApiInfo()
        api_key = request.headers['api-key']
        api_info.plus_api_call(api_key=api_key)
        api_result = APIResult()
        show_id = request.args.get('id')
        if show_id:
            return api_result.get_single_cafe_with_show_id(show_id=show_id)
        else:
            return {'error': 'Please provide an cafe id'}, 406


# Add the resource to the API with the custom RequestParser
api.add_resource(AllCountries, '/api/v1.0/country/all')
api.add_resource(GetsingelCountry, '/api/v1.0/country/single')
api.add_resource(GetManyCity, '/api/v1.0/city/all')
api.add_resource(GetSingelCity, '/api/v1.0/city/single')
api.add_resource(GetAllCafeinCity, '/api/v1.0/cafe/all')
api.add_resource(GetSingelCafe, '/api/v1.0/cafe/single')
from app.api.api_routes import main_doc
