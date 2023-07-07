from flask import Flask
from .extentions import db, ckeditor, mail, migrate, bootstrap, user_login_manager
from app.my_db_models import *
from app.config import Config
from flask_pymongo import PyMongo
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_gravatar import Gravatar
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect


def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)
    db.init_app(application)
    bootstrap.init_app(application)
    ckeditor.init_app(application)
    mail.init_app(application)
    migrate.init_app(application, db)
    return application


app = create_app()
csrf = CSRFProtect(app)
api = Api(app)
mongo_client = PyMongo(app=app)
mongo_db = mongo_client.db

#from app.error_handeler import handle_exception
from app.admin_views.admin_page import CustomModelView, CustomView, UserView, MyHomeView, CafeView

user_login_manager.init_app(app=app)


@user_login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user


from app.public_views import *
from app.private_views import *
from app.blog_views import *
from app.donate_view import donate
from app.admin_views.admin_view import clear_new_cafe, clear_subs, clear_users
from app.api import AllCountries, GetsingelCountry, main_doc

admin = Admin(app, index_view=MyHomeView(), template_mode='bootstrap4')
admin.add_view(UserView(User, db.session))
admin.add_view(CafeView(Cafe, db.session))
admin.add_link((MenuLink(name='logout', category='', url='/logout')))
admin.add_link((MenuLink(name='Home', category='', url='/')))

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

with app.app_context():
    db.create_all()
