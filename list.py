import uuid


class List:
    def __init__(self, name, board_id,cards=[]):
        self.list_id = str(uuid.uuid4())
        self.name = name
        self.board_id = board_id
        self.cards = cards
        self.url = None
