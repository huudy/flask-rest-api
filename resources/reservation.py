from flask import request
from flask_restful import Resource
from security import login_required
from models.reservation import ReservationModel
from bson.json_util import dumps
from bson.objectid import ObjectId
from models.room import Rooms
from models.user import User
from werkzeug.exceptions import BadRequest


class Reservation(Resource):
    @login_required
    def post(self, user_id):
        data = request.get_json()
        room = Rooms.objects.get(id=data['room'])
        # isBooked = False        
        for res in room.reserved:
            isBooked = False
            if data['startDate'] >= res['start_date'] and data['startDate'] <= res['end_date']:
                e = BadRequest('These dates are already booked for this room!')
                e.data = {'title':'Not Available'}
                raise e

        reservation = ReservationModel(data['startDate'][:10], data['endDate'][:10], user_id, data['room'])
        
        # try:
        print('Inserting')
        reservation.save()
        print('ReservationID: ',reservation.id)
        User.objects(id=user_id).update(add_to_set__reservations = reservation.json())
        Rooms.objects(id=data['room']).update_one(add_to_set__reserved = reservation.json())

        return {'Reserved':reservation.json()}

