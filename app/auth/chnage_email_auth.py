from app.extentions import db
from app.my_db_models import User


class EmailAuth:
    def __init__(self, email: str):
        self.new_email = email
        self.repeated_email = False
        self.check_email()

    def check_email(self):
        all_users = db.session.query(User).all()
        for each_user in all_users:
            if each_user.email == self.new_email:
                self.repeated_email = True
