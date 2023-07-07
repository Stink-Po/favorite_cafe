from os.path import join, dirname, realpath
from datetime import timedelta


class Config:
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<user>:<password>@localhost/<database name>"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = 'your url'
    FLASK_ADMIN_SWATCH = 'cerulean'
    BASIC_AUTH_USERNAME = 'username'
    BASIC_AUTH_PASSWORD = 'password'
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_POOL_RECYCLE = 35  # value less than backend’s timeout
    SQLALCHEMY_POOL_TIMEOUT = 7  # value less than backend’s timeout
    SQLALCHEMY_PRE_PING = True
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 10,
                                 'pool_recycle': 60,
                                 'pool_pre_ping': True}

    IJSONFY_MIMETYPE = 'application/json'

    SECRET_KEY = "b'\xf1L\xdb5D\x96M\xe5\xd1\x9f\x16+\xf4%A\x1e\xb9\xafm\xb8g\x1ct\x0e'"
    MAIL_SERVER = "everest.pws-dns.net"
    HOST_NAME = "your host ip or domain"
    MAIL_USERNAME = "email@exampel.com"
    MAIL_PASSWORD = "password"
    MAIL_PORT = 465
    MAIL_DEBUG = False
    MAIL_USE_SSL = True
    MAIL_USE_TSL = False
    REMEMBER_COOKIE_DURATION = timedelta(days=1.0)
    UPLOADS_PATH_BLOG = join(dirname(realpath(__file__)), 'static/upload/blog/')
    UPLOADS_PATH_CAFE = join(dirname(realpath(__file__)), 'static/upload/cafe/')
    UPLOADS_PATH_USER = join(dirname(realpath(__file__)), 'static/upload/user/')
    NEWS_PATH = join(dirname(realpath(__file__)), 'static/news/')
