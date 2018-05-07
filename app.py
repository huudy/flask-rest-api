import os
from flask import Flask, request
from flask_restful import Api
from resources.user import *
from resources.room import Room, RoomList
from resources.reservation import Reservation
from flask_cors import CORS
from mongoengine import *

is_prod = os.environ.get('IS_HEROKU', None)

app = Flask(__name__, instance_relative_config=True)
CORS(app)


if is_prod is None:
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    connect('FlaksMongo')
    print('connected to local db')
if is_prod:
    print('connected to heroku')
    connect('FlaskMongo', host=os.environ.get('MONGODB_URI', None))





app.secret_key = os.environ.get('SECRET_KEY',app.config['SECRET_KEY'])
app.security_password_salt = os.environ.get('SECURITY_PASSWORD_SALT', None)
api = Api(app)

# ENDPOINTS

api.add_resource(Reservation, '/reserve')
api.add_resource(UserRegister, '/register')
api.add_resource(Logout, '/logout')
api.add_resource(UserLogin, '/login')
api.add_resource(ConfirmEmail, '/confirm/<string:token>')
api.add_resource(Room, '/room/<string:name>')
api.add_resource(RoomList, '/rooms')


if __name__ == '__main__':
    app.run(debug=True) # important to mention debug=True