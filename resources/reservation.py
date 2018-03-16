from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.reservation import ReservationModel

class Reservation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
        type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
        required=True,
        help="Specify start date"
    )
    parser.add_argument('end_date',
        type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
        required=True,
        help="Please specify end date"
    )
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="Please specify end date"
    )
    parser.add_argument('room_id',
        type=int,
        required=True,
        help="Please specify end date"
    )

    @jwt_required()
    def post(self, room_id):
        data = request.get_json()
        reservations = db.rooms.find({'_id':room_id,
            'reserved':{
                '$not': {
                    '$elemMatch': {'startDate': {'$lte': data['start_date']}, 'endDate': {'$gte':data['end_date']}}
                }
             }})
        
        if reservations:
            return {'message':'These dates are already reserved'}

        reservation = ReservationModel(**data)
        try:
            reservation.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return reservation.json()

