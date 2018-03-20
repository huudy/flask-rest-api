import datetime

class ReservationModel():
    def __init__(self, start_date, end_date, user_id, room_id, *reserved_at):
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
        self.room_id = room_id
        self.reserved_at = datetime.datetime.utcnow()

    def json(self):
        return {'start_date':self.start_date, 'end_date': self.end_date, 'user_id': self.user_id, 'room_id':self.room_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def check_dates(cls, start_date, end_date):
        print('Start: ',start_date,'  End:  ',end_date)
        return cls.query.filter(start_date>=start_date).filter(end_date<=end_date).first()
