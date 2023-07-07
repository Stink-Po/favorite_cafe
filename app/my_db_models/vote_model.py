from app.extentions import db


class Vote(db.Model):
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafe.id', ondelete='CASCADE'), nullable=False)
    coffee_rating = db.Column(db.Integer, nullable=False)
    wifi_rating = db.Column(db.Integer, nullable=False)
    power_rating = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', backref=db.backref('votes', cascade="all, delete-orphan"))

    def __init__(self, user_id, cafe_id, coffee_rating, wifi_rating, power_rating):
        self.user_id = user_id
        self.cafe_id = cafe_id
        self.coffee_rating = coffee_rating
        self.wifi_rating = wifi_rating
        self.power_rating = power_rating
