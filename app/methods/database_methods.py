from app.methods import *
from app.my_db_models import Cafe, BlogPost, Country, City, User, UserCafe, Reviews


class DataBaseInfo:
    def __init__(self):
        self.last_cafe = None
        self.all_cafe = None
        self.all_users = None
        self.all_country = None
        self.all_city = None
        self.all_blog = None
        self.last_posts = None
        self.coffee_lovers = None
        self.owners = None
        self.a_country_data = None
        self.a_city_data = None
        self.a_cafe_data = None
        self.all_city_in_country = None
        self.all_cafe_in_city = None
        self.a_blog_post_data = None
        self.all_following_cafe = None
        self.ret_all_cafe()
        self.ret_len_all_users()
        self.ret_all_city()
        self.ret_all_country()
        self.ret_all_users()
        self.ret_all_blog()

    def ret_all_country(self):
        self.all_country = db.session.query(Country).all()
        return self.all_country

    def ret_all_city(self):
        self.all_city = db.session.query(City).all()
        return self.all_city

    def ret_len_all_users(self):
        self.all_users = len(db.session.query(User).all())
        return self.all_users

    def ret_all_cafe(self):
        self.all_cafe = db.session.query(Cafe).all()
        return self.all_cafe

    def ret_all_blog(self):
        self.all_blog = db.session.query(BlogPost).all()

    def ret_a_blog_post_with_id(self, post_id: int):
        self.a_blog_post_data = db.session.query(BlogPost).filter_by(id=post_id).first_or_404()
        return self.a_blog_post_data

    def ret_last_posts(self):
        self.last_posts = db.session.query(BlogPost).order_by(BlogPost.id.desc())[:4]
        return self.last_posts

    def ret_last_cafe(self):
        self.last_cafe = db.session.query(Cafe).order_by(Cafe.id.asc())[:4]
        return self.last_cafe

    def ret_all_users(self):
        self.coffee_lovers = db.session.query(User).all()
        return self.coffee_lovers

    def ret_a_country_with_name(self, country_name: str):
        self.a_country_data = db.session.query(Country).filter_by(country_name=country_name).first_or_404()
        return self.a_country_data

    def ret_all_city_in_country_with_country_id_alpha(self, country_id: int):
        self.all_city_in_country = db.session.query(City).filter_by(country_id=country_id).order_by(
            City.city_name).all()
        return self.all_city_in_country

    def ret_all_city_in_country_with_country_id_pop(self, country_id: int):
        self.all_city_in_country = db.session.query(City).filter_by(country_id=country_id).order_by(
            City.population.desc()).all()
        return self.all_city_in_country

    def ret_a_city_with_name(self, city_name: str):
        self.a_city_data = db.session.query(City).filter_by(city_name=city_name).first_or_404()
        return self.a_city_data

    def ret_all_cafe_in_city_with_city_id(self, city_id: int):
        self.all_cafe_in_city = db.session.query(Cafe).filter_by(city_id=city_id).all()
        return self.all_cafe_in_city

    def ret_a_country_with_id(self, country_id: int):
        self.a_country_data = db.session.query(Country).filter_by(id=country_id).first_or_404()
        return self.a_country_data

    def ret_a_cafe_with_id(self, cafe_id: int):
        self.a_cafe_data = db.session.query(Cafe).filter_by(id=cafe_id).first_or_404()
        return self.a_cafe_data

    def get_followed_cafes(self, user_id: int):
        followed_cafes = db.session.query(UserCafe).join(Cafe).filter(UserCafe.user_id == user_id).all()
        self.all_following_cafe = [user_cafe.cafe for user_cafe in followed_cafes]
        return self.all_following_cafe

    @staticmethod
    def ret_a_country_with_iso2(iso_2: str):
        return db.session.query(Country).filter_by(iso2=iso_2).first()

    @staticmethod
    def get_city_with_show_id(show_id):
        return db.session.query(City).filter_by(show_id=show_id).first()

    @staticmethod
    def all_cafe_in_city_with_city_show_id(show_id):
        city = db.session.query(City).filter_by(show_id=show_id).first()
        if city:
            city_id = city.id
            if len(db.session.query(Cafe).filter_by(city_id=city_id).all()) != 0:
                return db.session.query(Cafe).filter_by(city_id=city_id).all()
            else:
                return 0
        else:
            return None

    @staticmethod
    def ret_review_of_cafe(cafe_id):
        data = db.session.query(Reviews).filter_by(cafe_id=cafe_id).all()
        if data:
            return data
        else:
            return None

    @staticmethod
    def get_a_cafe_with_show_id(show_id):
        data = db.session.query(Cafe).filter_by(show_id=show_id).first()
        if data:
            return data
        else:
            return None
