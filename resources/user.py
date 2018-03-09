import sqlite3
import datetime
from flask_restful import Resource, reqparse
from models.user import User

class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_email(data['email']):
            return {"message": "User with that username already exists."}, 400

        creation_date = datetime.datetime.utcnow()
        print(data)
        user = User(data['email'], data['password'], creation_date, 0 )
        user.save_to_db()

        return {"message": "User created successfully."}, 201