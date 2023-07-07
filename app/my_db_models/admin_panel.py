from app.extentions import db


class NewUser(db.Model):
    __tablename__ = "newuser"
    id = db.Column(db.Integer, primary_key=True)
    new_user = db.relationship("User", back_populates="new_user_c")
    new_user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))


class NewCafe(db.Model):
    __tablename__ = "newcafe"
    id = db.Column(db.Integer, primary_key=True)
    new_cafe = db.relationship("Cafe", back_populates="new_cafe_c")
    new_cafe_id = db.Column(db.Integer, db.ForeignKey("cafe.id", ondelete="CASCADE"))


class NewSubscriber(db.Model):
    __tablename__ = "newsubscriber"
    id = db.Column(db.Integer, primary_key=True)
    new_sub = db.relationship("Subscribe", back_populates="new_sub_c")
    new_sub_id = db.Column(db.Integer, db.ForeignKey("subscribe.id", ondelete="CASCADE"))


class NewCount(db.Model):
    __tablename = "newcount"
    id = db.Column(db.Integer, primary_key=True)
    new_user_count = db.Column(db.Integer)
    new_cafe_count = db.Column(db.Integer)
    new_sub_count = db.Column(db.Integer)
