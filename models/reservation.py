import datetime
from mongoengine import *

class ReservationModel(Document):

    start_date = StringField(required=True)
    end_date = StringField(required=True)
    user_id = StringField(required=True)
    room_id = StringField(required=True)
    reserved_at = DateTimeField(default=datetime.datetime.utcnow)

    def json(self):
        return {'start_date':self.start_date, 'end_date': self.end_date, 'user_id': self.user_id, 'room_id':self.room_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def check_dates(cls, start_date, end_date):
        print('Start: ',start_date,'  End:  ',end_date)
        return cls.query.filter(start_date>=start_date).filter(end_date<=end_date).first()
