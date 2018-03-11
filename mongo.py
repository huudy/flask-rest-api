from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

db = client.FlaskMongo
# Rooms = db.rooms

# room = {'name':'CosyCorner'}

# inserted = Rooms.insert_one(room).inserted_id

# Rooms.find_one()

# db.collection_names(include_system_collections=False)# lists all the collections in the db

# print('Connected to : ', db, 'and inserted some:  ', room.insert_one({'name':'Jozek'}).inserted_id())

