import uuid


class User:
    def __init__(self, username, email):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.is_active = True
        self.is_admin = False

    def deactivate(self):
        self.is_active = False

    def make_admin(self):
        self.is_admin = True
