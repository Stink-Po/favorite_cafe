from app.methods import *
from app.my_db_models import User, Cafe, Reviews, APIKey
import secrets
from app.methods.time_method import Time


class UserManager:
    """Will Mange all operation onm users table(add, remove, ...)"""

    def __init__(self):
        self.api = None
        self.new_user = None
        self.pw_manager = None
        self.this_current_user = None
        self.total_cafe_added = None
        self.total_review = None

    def find_user(self, user_id: int):
        """
        find new user with user id
        :param user_id: user id saved in User class in Mysql db its primary key
        :type user_id: int
        :return: user object
        """
        self.this_current_user = db.session.query(User).filter_by(id=user_id).first_or_404()
        return self.this_current_user

    def update_password(self, new_password: str, user_id: int):
        """
        update password of the user
        :param new_password: new password of user
        :type new_password: str
        :param user_id: id of the user we want to change password
        :type user_id: int
        :return: nothing just commit changes
        """
        self.this_current_user = self.find_user(user_id=user_id)
        pw_manager = PasswordManeger(password=new_password)
        self.this_current_user.password = pw_manager.hashed_password
        db.session.commit()

    def update_email(self, new_email: str, user_id: int):
        """
        update email of the user
        :param new_email: new email we want to change
        :type new_email: str
        :param user_id: id of the user we want to change email
        :return: nothing just commit chnages
        """
        try:
            self.this_current_user = self.find_user(user_id=user_id)
            self.this_current_user.email = new_email
            self.this_current_user.confirmed = False
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def confirm_user_email(self, user_id: int):
        """
        set value of confirm to True in the given user id in User class
        and set user confirm email time
        :param user_id: id of the user we want to confirm email
        :type user_id: int
        :return: nothing just commit changes
        """
        try:
            time = datetime.utcnow()
            self.this_current_user = self.find_user(user_id=user_id)
            self.this_current_user.confirmed = True
            self.this_current_user.email_confirmed_at = time
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def active_user(self, user_id: int):
        """
        set values of active for user True
        :param user_id: id of the user we want active
        :type user_id: int
        :return: nothing just commit chnages
        """
        try:
            time = Time()
            self.this_current_user = self.find_user(user_id=user_id)
            self.this_current_user.active = True
            self.this_current_user.last_login = time.unix_time
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return e.args

    def de_active_user(self, user_id: int):
        """
        set value of active for user to False
        :param user_id: id of the user we want de active
        :type user_id: int
        :return: nothing just commit chnages
        """
        try:
            self.this_current_user = self.find_user(user_id=user_id)
            self.this_current_user.active = False
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def create_new_user(self, email, username, password, owner: bool):
        """
        create a new user in database
        :param email: email of the new user
        :type email: str
        :param username: username of the new user
        :type username: str
        :param password: password of the new user
        :type password: str hashed pw
        :param owner: if new user is owner it will be True else is False
        :type owner: bool
        :return: nothing just commit chnages
        """
        try:
            self.pw_manager = PasswordManeger(password=password)
            self.new_user = User(email=email, username=username, password=self.pw_manager.hashed_password,
                                 is_owner=owner)
            db.session.add(self.new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def create_admin_user(self, user_id: int):
        """
        this is a rule function if this is website first user it will be admin
        :param user_id: id of the user we want to check
        :type user_id: int
        :return: nothing just commit if there is a change
        """
        if user_id == 1:
            try:
                self.this_current_user = db.session.query(User).filter_by(id=user_id).first()
                self.this_current_user.is_admin = True
                self.this_current_user.confirmed = True
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return e.args

    def delete_user(self, user_id: int):
        """
        delete a user from database
        :param user_id: id of the user we want to delete
        :type user_id: int
        :return: new user
        """
        self.this_current_user = self.find_user(user_id=user_id)
        try:
            db.session.delete(self.this_current_user)
            db.session.commit()
            db.seesion.close()
            return self.this_current_user
        except Exception as e:
            db.session.rollback()
            return e.args

    def add_user_image(self, user_id: int, image_path: str):
        self.this_current_user = self.find_user(user_id=user_id)
        try:
            self.this_current_user.image = image_path
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def auth_api_request(self, api_key: str):
        if db.session.query(APIKey).filter_by(key=api_key).first():
            return True
        else:
            return False

    def find_user_by_email(self, email: str):
        """
        find a user in database with given email
        :param email: email of the user we want to check
        :type email: str
        :return: user object if exists or None if not found.
        """
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            self.this_current_user = user
            return self.this_current_user
        else:
            return None

    def find_user_activity(self, user):
        self.total_cafe_added = len(db.session.query(Cafe).filter_by(author=user).all())
        self.total_review = len(db.session.query(Reviews).filter_by(review_author=user).all())
        return self.total_cafe_added, self.total_review

    def create_api_key(self, user_id):
        api_key = secrets.token_urlsafe(24)
        have_key_before = db.session.query(APIKey).filter_by(user_id=user_id).first()
        if have_key_before:
            have_key_before.key = api_key
            try:
                db.session.commit()
                return have_key_before

            except Exception as e:
                db.session.rollback()
                return e.args
        try:
            self.api = APIKey(key=api_key, user_id=user_id)
            db.session.add(self.api)
            db.session.commit()
            return self.api

        except Exception as e:
            db.session.rollback()
            return e.args

    def find_user_api_key(self, user_id):
        self.api = db.session.query(APIKey).filter_by(user_id=user_id).first()
        if self.api:
            return self.api.key
        else:
            return None

    def find_non_active_users(self):
        mail_list = []
        current_time = int(datetime.now().timestamp())
        thirty_days_ago = current_time - (30 * 24 * 60 * 60)
        users = User.query.filter(User.last_login < thirty_days_ago, User.active != False).all()

        for user in users:
            self.de_active_user(user_id=user.id)
            mail_list.append((user.username, user.email))

        return mail_list
