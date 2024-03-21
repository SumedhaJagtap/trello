import uuid


class Board:
    def __init__(self, name, privacy='PUBLIC', members=[]):
        self.board_id = str(uuid.uuid4())
        self.name = name
        self.privacy = privacy
        self.url = None
        self.members = members

    def add_members(self, user_id):
        self.members.append(user_id)
