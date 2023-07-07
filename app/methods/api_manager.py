from app.my_db_models import User
from app.extentions import db
from app.my_db_models.api_key_model import APIKey


class ApiInfo:
    """Manage Website API"""

    def __init__(self):
        self.total_api_key = None
        self.total_api_call = None
        self.ret_total_api_key()

    def ret_total_api_key(self):
        try:
            self.total_api_key = len(db.session.query(APIKey).all())
        except TypeError:
            self.total_api_key = 0

        return self.total_api_key

    def ret_total_api_call(self):
        total_call = 0
        for user in db.session.query(User).all():
            total_call += user.total_api_use

        self.total_api_call = total_call
        return self.total_api_call

    @staticmethod
    def find_api_key(user_key):
        return db.session.query(APIKey).filter_by(key=user_key).first()

    @staticmethod
    def plus_api_call(api_key):
        user_id = db.session.query(APIKey).filter_by(key=api_key).first().user_id
        user = db.session.query(User).filter_by(id=user_id).first()
        user.api_use = True
        user.total_api_use += 1
        user.daily_api_call += 1
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e.args)
