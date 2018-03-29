from flask_restful import Resource
from flask import jsonify, Response
from models.room import Rooms
import json
# from mongo import db
from bson.json_util import dumps

class Room(Resource):
    def get(self, name):
        room = Rooms.objects.get(id=name).to_json()
        if room:
            return room
        return {'message': 'Item not found'}, 404

class RoomList(Resource):    
    def get(self):
        print('Getting rooms')
        roomList = Rooms.objects().to_json()
                # print(roomList)
        return roomList
