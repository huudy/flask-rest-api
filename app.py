import os
from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, UserLogin
from resources.room import Room, RoomList
from resources.reservation import Reservation
from mongoengine import *
connect('FlaskMongo')


app = Flask(__name__, instance_relative_config=True)

#GEtting proper config for dev
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod is None:
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['MONGO_DBNAME'] = "AnguNode"
# app.config['MONGO_URI'] = "mongodb://localhost:27017"

app.secret_key = os.environ.get('SECRET_KEY',app.config['SECRET_KEY'])
api = Api(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Room, '/room/<string:name>')
api.add_resource(RoomList, '/rooms')
api.add_resource(Reservation, '/reserve')

if __name__ == '__main__':
    app.run(debug=True) # important to mention debug=True