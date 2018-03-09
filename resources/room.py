from flask_restful import Resource
from flask_jwt import jwt_required
from models.room import RoomModel

class Room(Resource):

    def get(self, name):
        room = RoomModel.find_by_name(name)
        if room:
            return room.json()
        return {'message': 'Item not found'}, 404

class RoomList(Resource):
    
    def get(self):
        return {'rooms': [room.json for room in RoomModel.query.all()]}
