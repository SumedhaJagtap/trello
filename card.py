import uuid


class Card:
    def __init__(self, name, desc,list_id, assignee=-1):
        self.card_id = str(uuid.uuid4())
        self.name = name
        self.desc = desc
        self.assignee = assignee
        self.url = None
        self.list_id = list_id

    def assign_user(self, user_id):
        self.assignee = user_id

    def unassign_user(self):
        self.assignee = -1
