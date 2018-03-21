from mongoengine import *

class Rooms(Document):
    name = StringField(max_length=30)
    beds = IntField(min_value=1)
    img = ImageField()
    reserved = ListField()
    meta = {'strict': False}


    # def __init__(self, name, beds, img):
    #     self.name = name
    #     self.beds = beds
    #     self.img = img

    def json(self):
        return {'name':self.name, 'beds': self.beds, 'image':self.img }
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()