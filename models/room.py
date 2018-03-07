class Room():
    def __init__(self, _id, name, beds, reserved, images):
        self.id = _id
        self.name = name
        self.beds = beds
        self.reserved = reserved
        self.images = reserved

    @classmethod
    def find_by_id(cls, id):
        