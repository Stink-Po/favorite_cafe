from app.extentions import db
from app.my_db_models import User
from werkzeug.security import check_password_hash


class UserLoginAuthentication:
    """Check users username and password and set login equal to True in information was correct"""
    def __init__(self, username, password):
        """
        take a username and password and check with Mysql User table
        :param username: user enter for username
        :type username: str
        :param password: user entry for password
        :type password: str
        """
        self.username = username
        self.password = password
        self.user = None
        self.login = False
        self.check_user_login()

    def check_user_login(self):
        """
        check user log in
        :return: True if information was correct False if not
        """
        if db.session.query(User).filter_by(username=self.username).first():
            self.user = db.session.query(User).filter_by(username=self.username).first()
            if self.check_password():
                self.login = True
                return self.user

    def check_password(self):
        """
        check user entry password hash it and check with hashed password in user row if username was correct
        :return: True if information is correct and False if not
        """
        return check_password_hash(pwhash=self.user.password, password=self.password)
