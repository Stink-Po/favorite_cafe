from app.extentions import db
from app.methods.time_method import Time

time = Time()


class Reviews(db.Model):
    """A Mysql Tables for storing Users(Just Coffee Lovers) Reviews on café"""
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date = db.Column(db.String(100), default=time.formatted_time)
    review_author = db.relationship("User", back_populates="reviews")
    cafe_id = db.Column(db.Integer, db.ForeignKey("cafe.id", ondelete='CASCADE'))
    parent_cafe = db.relationship("Cafe", back_populates="reviews")
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'< text {self.text}>'
