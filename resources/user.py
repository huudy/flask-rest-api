import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from models.user import User
from mongo import db

class UserRegister(Resource):

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

        if db.users.find_one({'email':data['email']}):
            return {"message": "User with that username already exists."}, 400

        creation_date = datetime.datetime.utcnow()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        print(data)

        user = User(data['email'], hashed_password, creation_date, 0 )

        db.users.insert_one(user.json())

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):

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

        user = db.users.find_one({'email':data['email']})
        if check_password_hash(user['password'], data['password']):
            jwt.decode(encoded, 'secret', algorithms=['HS256'])
            return encoded_jwt = jwt.encode({'user_id': user['_id']}, app.secret_key, algorithm='HS256')

