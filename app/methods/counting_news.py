from app.my_db_models.admin_panel import NewUser, NewSubscriber, NewCafe, NewCount
from app.methods import db


class Counting:
    def __init__(self):
        self.new_user = None
        self.new_sub = None
        self.new_cafe = None
        self.count = NewCount.query.first()

    def add_new_cafe(self, cafe):
        new_cafe = NewCafe(new_cafe=cafe)
        self.new_cafe = new_cafe
        db.session.add(new_cafe)
        new_count = NewCount.query.first()
        try:
            if new_count and new_count.new_cafe_count is not None:
                new_count.new_cafe_count += 1
            else:
                new_count = NewCount(new_cafe_count=1)
                db.session.add(new_count)
            db.session.commit()
            return self.new_cafe
        except Exception as e:
            db.session.rollback()
            return e.args

    def add_new_sub(self, sub):
        new_subs = NewSubscriber(new_sub=sub)
        self.new_sub = new_subs
        db.session.add(new_subs)
        new_sub_count = NewCount.query.first()
        try:
            if new_sub_count and new_sub_count.new_sub_count is not None:
                new_sub_count.new_sub_count += 1
            else:
                new_sub_count = NewCount(new_sub_count=1)
                db.session.add(new_sub_count)
            db.session.commit()
            return self.new_sub
        except Exception as e:
            db.session.rollback()
            return e.args

    def add_new_user(self, user):

        new_user = NewUser(new_user=user)
        self.new_user = new_user
        db.session.add(new_user)
        new_user_count = NewCount.query.first()
        try:
            if new_user_count and new_user_count.new_user_count is not None:
                new_user_count.new_user_count += 1
            else:
                new_user_count = NewCount(new_user_count=1)
                db.session.add(new_user_count)
            db.session.commit()
            return self.new_user
        except Exception as e:
            db.session.rollback()
            return e.args

    def clear_user_count(self):
        try:
            all_users = db.session.query(NewUser).all()
            for user in all_users:
                NewUser.query.filter_by(id=user.id).delete()

            if self.count:
                self.count.new_user_count = 0
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def clear_sub_count(self):
        try:
            all_subs = db.session.query(NewSubscriber).all()
            for sub in all_subs:
                NewSubscriber.query.filter_by(id=sub.id).delete()
            if self.count:
                self.count.new_sub_count = 0

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args

    def clear_cafe_count(self):
        try:
            all_cafe = db.session.query(NewCafe).all()
            for cafe in all_cafe:
                NewCafe.query.filter_by(id=cafe.id).delete()
            if self.count:
                self.count.new_cafe_count = 0
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return e.args
