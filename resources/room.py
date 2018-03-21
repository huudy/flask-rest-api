from flask_restful import Resource
from models.room import Rooms
# from mongo import db
from bson.json_util import dumps

class Room(Resource):
    def get(self, name):
        room = dumps(RoomModel.find_one({'name':name}))
        if room:
            return room
        return {'message': 'Item not found'}, 404

class RoomList(Resource):    
    def get(self):
        return Rooms.objects().to_json()
