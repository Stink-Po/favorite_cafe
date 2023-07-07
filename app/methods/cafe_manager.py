from app.methods import *
from app.my_db_models import Cafe, Vote


class CafeManager:
    """ Manege Every method for Cafes"""

    def __init__(self):
        self.paginate = None
        self.all_cafe = None
        self.cafe = None
        self.new_cafe = None
        self.total_vote = None
        self.vote = None
        self.error = None
        self.user_scores = None

    def cafe_paginate(self, num):
        """
        making paginate for blog page
        :param num: it's a number of the page that we are init in blog page
        :return: a paginated object from blogpost
        """
        self.paginate = Cafe.query.paginate(per_page=5, page=num, error_out=True)
        return self.paginate

    def all_cafe_in_city(self, city_id: int):
        """
        Assist the value to the self.all_cafe we can use CafeManager.all_cafe
        :param city_id: id of the city we want to get all cafe
        :type city_id: int
        :return: all cafe inside the city
        """
        self.all_cafe = db.session.query(Cafe).filter_by(city_id=city_id).all()
        return self.all_cafe

    def add_cafe(self, create_by, address: str, phone: str, cafe_theme: str, open_time, close_time,
                 can_take_calls: bool, name: str, city_id: int, author, image: str,
                 coffee_score: int = 0, wifi_score: int = 0, power_score: int = 0,
                 about: str = "", staff: int = 0, menu_id: int = None):
        self.user_scores = self.calculate_user_scores(coffee_score=coffee_score, wifi_score=wifi_score,
                                                      power_score=power_score)
        try:
            self.new_cafe = Cafe(
                create_by=create_by,
                name=name,
                menu_id=menu_id,
                address=address,
                phone=phone,
                cafe_theme=cafe_theme,
                cafe_rating=self.user_scores,
                open_time=open_time,
                close_time=close_time,
                can_take_calls=can_take_calls,
                about=about,
                city_id=city_id,
                author=author,
                image=image,
                staff=staff,
                coffee_score=coffee_score,
                wifi_score=wifi_score,
                power_score=power_score,

            )
            db.session.add(self.new_cafe)
            db.session.commit()
            return self.new_cafe

        except Exception as e:
            db.session.rollback()
            self.error = e.args
            return self.error

    def add_vote(self, user_id, cafe_id, coffee_rating, wifi_rating, power_rating):
        try:
            self.vote = Vote(user_id=user_id,
                             cafe_id=cafe_id,
                             coffee_rating=coffee_rating,
                             wifi_rating=wifi_rating,
                             power_rating=power_rating)

            db.session.add(self.vote)
            self.counting_votes(cafe_id=cafe_id)
            db.session.commit()

        except Exception as e:

            db.session.rollback()
            self.error = e.args
            return self.error

    def counting_votes(self, cafe_id):
        this_cafe = db.session.query(Cafe).filter_by(id=cafe_id).first_or_404()
        if this_cafe:
            try:
                this_cafe.total_vote = this_cafe.total_vote + 1
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                self.error = e.args
                return self.error
            return self.total_vote
        else:
            self.error = "No Cafe Found"
            return self.error

    def calculate_user_scores(self, coffee_score, wifi_score, power_score):
        self.user_scores = (coffee_score + wifi_score + power_score) / 3
        return self.user_scores

    def calculate_new_total_scores(self, cafe_id: int, user_id: int, new_coffe_score: int,
                                   new_wifi_score: int, new_power_score: int):

        try:
            self.add_vote(user_id=user_id, cafe_id=cafe_id,
                          coffee_rating=new_coffe_score,
                          wifi_rating=new_wifi_score,
                          power_rating=new_power_score)

            self.cafe = db.session.query(Cafe).filter_by(id=cafe_id).first_or_404()
            current_total_vote = self.cafe.total_vote
            current_cafe_rating = self.cafe.cafe_rating
            current_coffee_score = self.cafe.coffee_score
            current_wifi_score = self.cafe.wifi_score
            current_power_score = self.cafe.power_score
            self.cafe.coffee_score = (current_coffee_score * current_total_vote + new_coffe_score) / (
                    current_total_vote + 1)

            self.cafe.wifi_score = (current_wifi_score * current_total_vote + new_wifi_score) / (
                    current_total_vote + 1)

            self.cafe.power_score = (current_power_score * current_total_vote + new_power_score) / (
                    current_total_vote + 1)

            new_cafe_score = self.calculate_user_scores(coffee_score=new_coffe_score,
                                                        wifi_score=new_wifi_score,
                                                        power_score=new_power_score)

            self.cafe.cafe_rating = (current_cafe_rating * current_total_vote + new_cafe_score) / (
                    current_total_vote + 1)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return e.args
