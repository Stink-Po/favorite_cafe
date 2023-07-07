from app.extentions import db


class Message(db.Model):
    """A Mysql Table For Storing Users Message that will send to Contact us"""
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """

        :return: Subject of the users Messages
        """
        return f'<message {self.subject}>'

    def __init__(self, name, subject, email, message):
        """

        :param name: name of the person that sends message
        :type name: str
        :param subject: Subject of the Message
        :type subject: str
        :param email: Email of the person for Contact him if its Nessesery latere
        :type email: str
        :param message: Actual Message that send to the Website
        :type message: str
        """
        self.name = name
        self.subject = subject
        self.email = email
        self.message = message
