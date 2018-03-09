from db import db

class ReservationModel(db.Model):
    #SQLAlchemy table for db    
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    user = db.relationship('User')
    room = db.relationship('RoomModel')
    #end table

    def __init__(self, start_date, end_date, user_id, room_id):
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
        self.room_id = room_id

    def json(self):
        return {'start_date':self.start_date, 'end_date': self.end_date, 'user_id': self.user_id, 'room_id':self.room_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def check_dates(cls, start_date, end_date):
        return cls.query.filter_by(start_date>=start_date).filter_by(end_date<=end_date).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()