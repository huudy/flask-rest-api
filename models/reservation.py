from db import db

class ReservationModel(db.Model):
    #SQLAlchemy table for db    
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    start_date - db.Column(db.Date)
    end_date - db.Column(db.Date)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    #end table

     def __init__(self, _id, name, beds, reserved, images):
        self.id = _id
        self.name = name
        self.beds = beds
        self.reserved = reserved
        self.images = reserved

    def json(self):
        return {'name':self.name, 'items': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()