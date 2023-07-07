from app.extentions import db
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class Cafe(db.Model):
    """
    A Mysql Table Wrote With Flask SQLAlchemy for Storing
    Cafes Adding by Users it Can modified To suite Any kind
    of Jobs
    """
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(250), nullable=False, unique=True, default=generate_uuid)
    menu_id = db.Column(db.String(250), unique=True, nullable=True)
    create_by = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    cafe_rating = db.Column(db.Float, nullable=False, default=0)
    staff = db.Column(db.Integer, nullable=False)
    cafe_theme = db.Column(db.String(250), nullable=False)
    open_time = db.Column(db.String(250), nullable=False)
    close_time = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(250), nullable=False)
    coffee_score = db.Column(db.Float, nullable=False, default=0)
    wifi_score = db.Column(db.Float, nullable=False, default=0)
    power_score = db.Column(db.Float, nullable=False, default=0)
    total_vote = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.String(250), nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    about = db.Column(db.Text, nullable=True)
    followers = db.relationship("UserCafe", back_populates="cafe")
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    author = db.relationship("User", back_populates="cafe")
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    new_cafe_c = db.relationship("NewCafe",
                                 back_populates="new_cafe",
                                 cascade="all, delete-orphan",
                                 passive_deletes=True)
    reviews = db.relationship("Reviews", back_populates="parent_cafe")
    votes = db.relationship("Vote", backref=db.backref('cafe'), cascade="all, delete")

    def __repr__(self):
        return f'< Cafe {self.name}>'
