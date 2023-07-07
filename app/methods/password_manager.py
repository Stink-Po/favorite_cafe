from werkzeug.security import generate_password_hash


class PasswordManeger:
    def __init__(self, password):
        self.user_pw = password
        self.hashed_password = self.hash_password_generator()

    def hash_password_generator(self):
        self.hashed_password = generate_password_hash(
            password=self.user_pw,
            method='pbkdf2:sha256',
            salt_length=8
        )
        return self.hashed_password
