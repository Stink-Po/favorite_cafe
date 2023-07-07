from app.extentions import db


class Analyzer(db.Model):
    __tablename__ = 'analyzer'
    id = db.Column(db.Integer, primary_key=True)
    total_view = db.Column(db.integer, default=0)
    today_view = db.Column(db.integer, default=0)
