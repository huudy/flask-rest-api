from flask import request
from flask_restful import Resource, reqparse
from security import login_required
from models.reservation import ReservationModel
from mongo import db
from bson.json_util import dumps
from bson.objectid import ObjectId

class Reservation(Resource):
    # @login_required
    def post(self):
        data = request.get_json()
       
        room = db.rooms.find({'_id':ObjectId(data['room_id'])})
        
          
        reservations = db.rooms.find({'_id':ObjectId(data['room_id']),
            'reserved':{
                '$not': {
                    '$elemMatch': {'startDate': {'$lte': data['start_date']}, 'endDate': {'$gte':data['start_date']}}
                }
             }})
        
        
        
        print('Reservations: ', dumps(reservations))


        # if reservations:
        #     return {'message':'These dates are already reserved'}

        reservation = ReservationModel(**data)
        # print('Res: ',reservation.json())
        # try:
        print('Inserting')
        mainres = db.reservations.insert_one(reservation.json()).inserted_id()
        print(ObjectId(mainres))
        db.users.update_one({'_id':ObjectId(data['user_id'])}, {'$push': {'reservations':reservation.json()}})
        # print(dumps(userres))
        db.rooms.update_one({'_id':ObjectId(data['room_id'])}, {'$push': {'reserved':reservation.json()}})

            # print('Inserted main:',dumps(mainres), ' userres: ', dumps(userres), 'roomres: ', dumps(roomres))
        # except:
        #     return {"message": "An error occurred inserting the item."}

        return {'Reserved':reservation.json()}

