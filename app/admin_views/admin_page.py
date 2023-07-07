from flask_admin import expose, BaseView, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import abort, redirect, url_for
from app.my_db_models.admin_panel import NewCount, NewSubscriber, NewCafe, NewUser
from app.extentions import db


class CustomView(BaseView):
    @expose('/')
    def index(self):
        print('test')
        if current_user.is_authenticated and current_user.is_admin:
            return self.render('admin/index.html')
        else:
            return abort(403)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def is_visible(self):
        return current_user.is_authenticated and current_user.is_admin

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('public.user_login'))


class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class UserView(CustomModelView):
    column_list = ('username', 'active', 'email')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class CafeView(CustomModelView):
    column_list = ('name', 'cafe_rating', 'create_by', 'author')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        new_cafe = db.session.query(NewCafe).all()
        new_users = db.session.query(NewUser).all()
        new_subs = db.session.query(NewSubscriber).all()
        count = db.session.query(NewCount).first()
        print(count.new_sub_count)
        if current_user.is_authenticated and current_user.is_admin:
            return self.render('admin/index.html',
                               new_cafe=new_cafe,
                               new_users=new_users,
                               new_subs=new_subs,
                               count=count)
        else:
            return abort(403)
