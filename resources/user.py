import datetime
import jwt
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from models.user import User
from bson.json_util import dumps

class UserRegister(Resource):

    def post(self):
        data = request.get_json()
        print(data)
        userInDB = User.objects(email=data['email'])
        if userInDB:
            return {"message": "User with that username already exists."}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        user = User(data['email'], hashed_password)

        user.save()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):

    def post(self):
        data = request.get_json()
        user = User.objects.get(email=data['email'])
        print('ID: ',user.id)
        if user and check_password_hash(user.password, data['password']):
            token = User.generate_token(str(user.id))
            User.objects(email=data['email']).update_one(set__token = token.decode())
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'token': token.decode()
            }
            return responseObject, 201
            # return encoded_jwt = jwt.encode({'user_id': user['_id']}, app.secret_key, algorithm='HS256')
        return {'message':'Wrong user/password combination. Please verify!'}

class UserLogout(Resource):
    def post(self):
        pass