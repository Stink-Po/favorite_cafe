from app.methods.database_methods import DataBaseInfo


class UserSingUpAuthentication:
    """New User Sing in Authentication"""

    def __init__(self, username, email):
        """
        get new user username and password and check if we have them in our database or not
        :param username: new user username entry
        :type username: str
        :param email: new user email entry
        :type email: str
        """
        self.username = username
        self.email = email
        self.database_info = DataBaseInfo()  # instance of Database information
        self.sing_up = True
        self.repeated_username = False
        self.repeated_email = False
        self.check_user()

    def check_user(self):
        """
        check new users' data
        :return: set sing_up to False in we already have the user with this information in database
        and if we have set repeated_username if we have the username to True
        or repeated_email to true if we have the email

        """
        if self.database_info.ret_all_users():
            for user in self.database_info.ret_all_users():
                if user.username == self.username:
                    self.repeated_username = True
                    self.sing_up = False
                if user.email == self.email:
                    self.repeated_email = True
                    self.sing_up = False
