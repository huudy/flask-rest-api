from db import db

class RoomModel(db.Model):
    #SQLAlchemy table for db    
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    beds = db.Column(db.Integer)
    img = db.Column(db.LargeBinary)
    reservations = db.relationship('ReservationModel', lazy='dynamic')
    #end table

    def __init__(self, name, beds, img):
        self.name = name
        self.beds = beds
        self.img = img

    @classmethod
    def find_by_id(cls, id):

    def json(self):
        return {'name':self.name, 'beds': self.beds, 'image':self.img }
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()