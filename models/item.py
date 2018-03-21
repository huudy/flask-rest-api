from mongo import db
from mongoengine import *


class ItemModel():

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price    
        self.store_id = store_id
    
    def json(self):
        return {'name':self.name, 'price':self.price}

    @classmethod
    def find_by_name(cls, name):
        return db.items.find_one({'name':name})

    def save_to_db(self):
        db.items.insert_one(self)
        

    def delete_from_db(self):
        db.items.delete_one(self)
