from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.reservation import ReservationModel

class Reservation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
        type=Date,
        required=True,
        help="Specify start date"
    )
    parser.add_argument('end_date',
        type=Date,
        required=True,
        help="Please specify end date"
    )
    parser.add_argument('user_id',
        type=Integer,
        required=True,
        help="Please specify end date"
    )
    parser.add_argument('room_id',
        type=Integer,
        required=True,
        help="Please specify end date"
    )

    @jwt_required()
    def post(self, start_date, end_date):
        if ReservationModel.check_dates(start_date, end_date):
            return {'message':'These dates are already reserved'}

        data = Item.parser.parse_args()
        reservation = ReservationModel(**data)

