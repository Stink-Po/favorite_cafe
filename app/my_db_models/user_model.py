from app.extentions import db
from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from app.methods.time_method import Time


time = Time()


class User(UserMixin, db.Model):
    """A Mysql table For Storing Users(coffee lovers $ Owners) Data"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_owner = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    reminder = db.Column(db.Boolean, nullable=False, default=False)
    image = db.Column(db.String(250), nullable=True)
    rank = db.Column(db.Integer, nullable=False, default=0)
    cafe_association = db.relationship("UserCafe", back_populates="user")
    following_cafe = association_proxy("cafe_association", "Cafe")
    joined_date = db.Column(db.String(100), default=time.formatted_time)
    last_login = db.Column(db.Integer)
    email_confirmed_at = db.Column(db.DateTime())
    api_use = db.Column(db.Boolean, nullable=False, default=False)
    total_api_use = db.Column(db.Integer, default=0)
    daily_api_call = db.Column(db.Integer, default=0)
    posts = db.relationship("BlogPost", back_populates="author")
    cafe = db.relationship("Cafe", back_populates="author")
    new_user_c = db.relationship("NewUser",
                                 back_populates="new_user",
                                 cascade="all, delete-orphan",
                                 passive_deletes=True)
    reviews = db.relationship("Reviews", back_populates="review_author")
    api_keys = db.relationship('APIKey', backref='user', lazy=True, cascade='delete')

    def __repr__(self):
        """

        :return: username of the user or owner
        """
        return f'< user {self.username}>'

    def __init__(self, email, username, password, is_owner: bool):
        """

        :param email: registered email of the user or owner
        :type email: str
        :param username: registered username of the user or owner
        :type username: str
        :param password: a Hashed password of the user
        :type password: str
        :param is_owner: a True if this user is a cafe owner
        :type is_owner: bool
        """
        self.email = email
        self.username = username
        self.password = password
        self.is_owner = is_owner
