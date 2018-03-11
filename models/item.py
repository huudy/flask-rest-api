from mongo import db


class ItemModel():

    #######
    #item to store one to many

    # __tablename__ = 'items'

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(30))
    # price = db.Column(db.Float(precision=2))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')



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
