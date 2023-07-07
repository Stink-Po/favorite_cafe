from app.methods import *
from app.my_db_models import Message


class AddNewMessage:
    """Manage Contact us and message table in mysql database"""
    def __init__(self, first_name, subject, email, message):
        self.first_name = first_name
        self.subject = subject
        self.email = email
        self.message = message
        self.new_message()

    def new_message(self):
        """
        add new message in message table in mysql database
        :return: nothing commit changes
        """
        new = Message(name=self.first_name,
                      subject=self.subject,
                      email=self.email,
                      message=self.message)
        db.session.add(new)
        db.session.commit()
