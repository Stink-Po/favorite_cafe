from app.my_db_models.vote_model import Vote
from app.extentions import db


class VotingManager:
    def __init__(self, user, cafe):
        self.user = user
        self.cafe = cafe
        self.voted = False
        self.votes = None
        self.check_voted()
        self.get_user_votes()

    def check_voted(self):
        if db.session.query(Vote).filter_by(user_id=self.user.id, cafe_id=self.cafe.id).first():
            self.voted = True
            return self.voted

    def get_user_votes(self):
        if self.voted:
            self.votes = db.session.query(Vote).filter_by(user_id=self.user.id, cafe_id=self.cafe.id).first()
            return self.votes

    def update_user_vote(self, coffee_score: int, wifi_score: int, power_score: int):
        self.votes = db.session.query(Vote).filter_by(user_id=self.user.id, cafe_id=self.cafe.id).first()
        if self.votes:
            try:
                self.votes.coffee_rating = coffee_score
                self.votes.wifi_rating = wifi_score
                self.votes.power_rating = power_score
                db.session.commit()

            except Exception as e:
                db.session.rollback()
                return e.args

    def add_new_vote(self, coffe_score: int, wifi_score: int, power_score: int):
        try:
            new_vote = Vote(user_id=self.user.id,
                            cafe_id=self.cafe.id,
                            coffee_rating=coffe_score,
                            wifi_rating=wifi_score,
                            power_rating=power_score)
            db.session.add(new_vote)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return e.args



