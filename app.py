import os
from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.room import Room, RoomList
from resources.reservation import Reservation


app = Flask(__name__, instance_relative_config=True)

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod is None:
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.secret_key = os.environ.get('SECRET_KEY',app.config['SECRET_KEY'])
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Room, '/room/<string:name>')
api.add_resource(RoomList, '/rooms')
api.add_resource(Reservation, '/reserve')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True) # important to mention debug=True