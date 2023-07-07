from app.extentions import db


class Subscribe(db.Model):
    """A Mysql table for Storing users that's Subscribe to Our Website"""
    __tablename__ = "subscribe"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    new_sub_c = db.relationship("NewSubscriber",
                                back_populates="new_sub",
                                cascade="all, delete-orphan",
                                passive_deletes=True)

    def __repr__(self):
        """

        :return: Email of the Subscribed User
        """
        return f'<email {self.email}>'

    def __init__(self, email):
        """

        :param email: Email of the user
        :type email: str
        """
        self.email = email
