from app.my_db_models import Subscribe
from app.methods import db
from app.methods.counting_news import Counting


class SubManager:
    def __init__(self, email):
        self.email = email
        self.counting = Counting()
        self.new_subscriber = None
        self.new_sub()

    def new_sub(self):
        new_subscribe = Subscribe(email=self.email)
        self.new_subscriber = new_subscribe
        db.session.add(new_subscribe)
        self.counting.add_new_sub(sub=self.new_subscriber)
        db.session.commit()
