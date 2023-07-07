from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail


class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True
        options["pool_recycle"] = 60
        options["pool_size"] = 10


db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
ckeditor = CKEditor()
user_login_manager = LoginManager()
user_login_manager.login_view = 'public.user_login'
migrate = Migrate()





