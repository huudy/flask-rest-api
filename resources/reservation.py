from flask import request
from flask_restful import Resource
from security import login_required
from models.reservation import ReservationModel
from bson.json_util import dumps
from bson.objectid import ObjectId
from models.room import Rooms
from models.user import User

class Reservation(Resource):
    # @login_required
    def post(self):
        data = request.get_json()
       
        room = Rooms.objects.get(id=data['room_id'])
        print('Room: ',room.json())
        
        for res in room.reserved:
            print('Reservation: ',res)
            if data['start_date'] >= res['start_date'] and data['start_date'] <= res['end_date']:
                return {'message':'These date are already reserved for this room'}
        
        # db.rooms.find_one({
        #     '_id':ObjectId(data['room_id'])}).aggregate([
        #         {'$unwind' : { "$reserved" } },
        #         {'$match': {'reserved':{ 'startDate': {'$lte': data['start_date'][:10] }, 'endDate': { '$gte':data['start_date'][:10] }}}}
        #     ])


        reservation = ReservationModel(data['start_date'][:10], data['end_date'][:10], data['user_id'], data['room_id'])
        
        # try:
        print('Inserting')
        reservation.save()
        print('ReservationID: ',reservation.id)
        User.objects(id=data['user_id']).update(add_to_set__reservations = reservation.to_json())
        Rooms.objects(id=data['room_id']).update_one(add_to_set__reserved = reservation.json())
        # made_res = db.reservations.insert_one(reservation.json())
        # print(made_res)
        # db.users.update_one({'_id':ObjectId(data['user_id'])}, {'$push': {'reservations':reservation.json()}})
        # # print(dumps(userres))
        # db.rooms.update_one({'_id':ObjectId(data['room_id'])}, {'$push': {'reserved':reservation.json()}})

            # print('Inserted main:',dumps(mainres), ' userres: ', dumps(userres), 'roomres: ', dumps(roomres))
        # except:
        #     return {"message": "An error occurred inserting the item."}

        return {'Reserved':reservation.json()}

