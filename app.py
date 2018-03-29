import os
from flask import Flask, request
from flask_restful import Api
from resources.user import UserRegister, UserLogin, ConfirmEmail
from resources.room import Room, RoomList
from resources.reservation import Reservation
from flask_cors import CORS
from mongoengine import *
connect('FlaskMongo')


app = Flask(__name__, instance_relative_config=True)
CORS(app)

#GEtting proper config for dev
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod is None:
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

app.secret_key = os.environ.get('SECRET_KEY',app.config['SECRET_KEY'])
api = Api(app)

# ENDPOINTS
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ConfirmEmail, '/confirm/<string:token>')
api.add_resource(Room, '/room/<string:name>')
api.add_resource(RoomList, '/rooms')
api.add_resource(Reservation, '/reserve')


if __name__ == '__main__':
    app.run(debug=True) # important to mention debug=True