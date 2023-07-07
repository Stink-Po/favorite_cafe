from app import mail
from flask import url_for, render_template
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, TimestampSigner
from app.methods.get_image import GetPhoto
from app.config import Config
from flask_login import current_user
from datetime import datetime
from app.methods.database_methods import DataBaseInfo
from app.methods.user_manager import UserManager


class EmailSender:
    """Sending Confirmation Email To user Email"""

    def __init__(self):
        self.mail = mail
        self.mail.connect()
        self.image_manager = GetPhoto(search_object='cafe')
        self.serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        self.timestamp = TimestampSigner(Config.SECRET_KEY)
        self.site_mail = Config.MAIL_USERNAME

    def send_welcome_email(self) -> None:
        message = "Welcome To Favorite Cafe\n" \
                  "Our cafe-focused website is a place where café owners and enthusiasts come together to share " \
                  "information about cafés around the world. Our platform includes a Restful API for easy access to " \
                  "user-generated reviews, cafe listings, and helpful rankings. Join our global community of coffee " \
                  "lovers and café owners. Discover new cafés, rank your favorites, and share your experiences "
        user_email = current_user.email
        confirm_link = url_for("index", _external=True)
        confirm_link = str(confirm_link.replace('127.0.0.1:5478', 'favoritecafe.ir'))


        msg = Message('Welcome to Favorite Cafe', sender=self.site_mail, recipients=[user_email])
        msg.body = render_template('email/welcome.html',
                                   user=current_user,
                                   link=confirm_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/welcome.html',
                                   user=current_user,
                                   link=confirm_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)

    def send_confirm_email(self) -> None:
        """
        Send an email with email address we config in config.py file to user email
        :return: None
        """
        message = "Please Confirm your Email address with the link blow"
        user_email = current_user.email
        token = self.serializer.dumps(user_email, salt="email_confirm")
        confirm_link = url_for("confirm_email", token=token, _external=True)
        print(confirm_link)
        confirm_link = str(confirm_link.replace('127.0.0.1:5478', 'favoritecafe.ir'))
        print(confirm_link)
        msg = Message('Confirm', sender=self.site_mail, recipients=[user_email])
        msg.body = render_template('email/singel-news.html',
                                   user=current_user,
                                   link=confirm_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/singel-news.html',
                                   user=current_user,
                                   link=confirm_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)

    def send_api_key(self, key) -> None:
        pass
        message = f'Your API Key is successfully Created\n' \
                  f'Your Key is :\n' \
                  f'<strong> {key} </strong>\n' \
                  f'You can Read API Documents'
        user_email = current_user.email
        link = url_for('main_doc', _external=True)
        msg = Message('API Key', sender=self.site_mail, recipients=[user_email])
        msg.body = render_template('email/api_key.html',
                                   user=current_user,
                                   link=link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/api_key.html',
                                   user=current_user,
                                   link=link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)


class ConfirmEmail:

    def __init__(self, token):
        """
        confirm User Email if the token in the reqest header is valid
        :param token: URLSafeTimedSerializer token
        :type token: str
        """
        self.serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        self.timestamp = TimestampSigner(Config.SECRET_KEY)
        self.time = datetime.utcnow()
        self.token = token
        self.confirm = False
        self.message = None
        self.confirm_email()

    def confirm_email(self):
        """
        check token is vailed or not
        :return: user object if valed and error message in str if not
        """
        try:

            self.serializer.loads(self.token, salt="email_confirm", max_age=3600)
            self.confirm = True
            user_manager = UserManager()
            user_manager.confirm_user_email(user_id=current_user.id)

        except Exception as e:
            self.confirm = False
            print(e.args[0])
            self.message = f"Error {e.args[0]} Request a New Link to activating Your Email Please"
            return self.message


class SendGroupMail:

    def __init__(self, new_post):
        """
        Make a list from all website users email to send them an email
        :param new_post: a mysql BlogPost object
        """
        self.recipients = []
        self.mail = mail
        self.database_info = DataBaseInfo()
        self.image = GetPhoto(search_object='cafe')
        self.new_post = new_post
        self.make_recipient()

    def make_recipient(self):
        """
        loop into the User class in Mysql database table
        :return: a list with all of users emails
        """
        for user in self.database_info.ret_all_users():
            self.recipients.append(user.email)

    def send(self) -> None:
        """
        send an email with new blog post title and link to the new blog post
        :return: None
        """
        message = f"We have a New post\n" \
                  f" {self.new_post.title}\n" \
                  f"in Favorite Cafe"
        link = url_for("load_blog_post", post_id=self.new_post.id, _external=True)
        link = str(link.replace('127.0.0.1:5478', 'favoritecafe.ir'))
        site_mail = Config.MAIL_USERNAME
        msg = Message("New Blog Post", sender=site_mail, recipients=self.recipients)
        msg.body = render_template('email/group_email.html',
                                   link=link,
                                   image=self.image.final,
                                   message=message,
                                   new_post=self.new_post
                                   )
        msg.html = render_template("email/group_email.html",
                                   link=link,
                                   image=self.image.final,
                                   message=message,
                                   new_post=self.new_post
                                   )
        self.mail.send(msg)


class SendForgotPasswordEmail:
    def __init__(self, user_email, user):
        """
        Sending an Email with Rest password link
        :param user_email: user email
        :type user_email: str
        :param user: user that fogot the password or want to  change password.
        :type user: User object
        """
        self.mail = mail
        self.user = user
        self.user_email = user_email
        self.image_manager = GetPhoto(search_object='cafe')
        self.serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        self.timestamp = TimestampSigner(Config.SECRET_KEY)
        self.site_mail = Config.MAIL_USERNAME

    def send_email(self) -> None:
        """
        send Rest password link to user email
        :return: None
        """
        message = "You Can Rest You Password With the link blow\n" \
                  "if You Dont Request for this link Just avoid this Email"
        token = self.serializer.dumps(self.user_email, salt="forgot_password")
        rest_link = url_for("rest_user_password", user_id=self.user.id, token=token, _external=True)
        print(rest_link)
        rest_link = str(rest_link.replace('127.0.0.1:5478', 'favoritecafe.ir'))
        msg = Message('Rest Password', sender=self.site_mail, recipients=[self.user_email])
        msg.body = render_template('email/fogot_password.html',
                                   user=self.user,
                                   link=rest_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/fogot_password.html',
                                   user=self.user,
                                   link=rest_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)

    def send_email_to_remain_password_changed(self) -> None:
        """
        send a reminder email to user for recently changed password
        :return: None
        """
        message = "Your Password hase Successfully changed if You Dont Do This" \
                  "Please Go to the website and request to Rest your Password again with the link Blow"
        rest_link = url_for("check_user_email", _external=True)
        rest_link = str(rest_link.replace('127.0.0.1:5478', 'favoritecafe.ir'))
        msg = Message('Rest Password', sender=self.site_mail, recipients=[self.user_email])
        msg.body = render_template('email/fogot_password.html',
                                   user=self.user,
                                   link=rest_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/fogot_password.html',
                                   user=self.user,
                                   link=rest_link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)


class AuthForgotPassword:
    def __init__(self, token):
        """
        check the user link from the email for check if the token is valed or not
        :param token: URLSafeTimedSerializer
        :type token: str
        """
        self.serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        self.timestamp = TimestampSigner(Config.SECRET_KEY)
        self.time = datetime.utcnow()
        self.token = token
        self.rest = False
        self.message = None
        self.auth()

    def auth(self):
        """
        auth the user token
        :return: self.Rest to true if the token if vailed and return a message in str if not
        """
        try:

            self.serializer.loads(self.token, salt="forgot_password", max_age=3600)
            self.rest = True

        except Exception as e:
            self.rest = False
            print(e.args[0])
            self.message = f"Error {e.args[0]} Request a New Link to Rest Your Password Please"
            return self.message


class SendEmailtononActiveMembers:
    def __init__(self, email, username):
        self.user_email = email
        self.username = username
        self.mail = mail
        self.image_manager = GetPhoto(search_object='cafe')
        self.site_mail = Config.MAIL_USERNAME

    def send_email(self):
        message = "We Check Our Active Users on Favorite Cafe\n" \
                  "and its look you not using your account\n" \
                  "in last month we hope you are safe and happy\n" \
                  "and if you have any problem in website please\n" \
                  "contact us"
        link = url_for('index', _external=True)
        msg = Message('Activity Reminder', sender=self.site_mail, recipients=[self.user_email])
        msg.body = render_template('email/reminder.html',
                                   user=self.username,
                                   link=link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )

        msg.html = render_template('email/reminder.html',
                                   user=self.username,
                                   link=link,
                                   image=self.image_manager.final,
                                   message=message,
                                   )
        self.mail.send(msg)

