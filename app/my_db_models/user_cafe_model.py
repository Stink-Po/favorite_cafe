from app.extentions import db


class UserCafe(db.Model):
    """An Mysql table for manage Users following and unfollowing Cafe"""
    __tablename__ = "usercafe"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    cafe_id = db.Column("cafe_id", db.Integer, db.ForeignKey("cafe.id", ondelete="CASCADE"))
    user = db.relationship("User", back_populates="cafe_association")
    cafe = db.relationship("Cafe", back_populates="followers")
