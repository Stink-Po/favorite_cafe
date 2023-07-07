from app.extentions import db
from app.methods.time_method import Time


class BlogPost(db.Model):
    """
    A Mysql Table Wrote With Flask SQLAlchemy for Storing Blog Website Posts
    """
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_path = db.Column(db.String(250), nullable=False)
    create_date = db.Column(db.String(100), default=Time.now_formatted_time)

    def __repr__(self):
        return f'<title {self.title}>'
