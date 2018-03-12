from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from security import login_required
from mongo import db
from bson.json_util import dumps

class Item(Resource):

    Items = db.items

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=float,
        required=True,
        help="An item has to have a store"
    )

    def post(self, name):
        if db.items.find_one({'name':name}):
            return {'message': "An item with name '{}' already exists.".format(name)}
        # if ItemModel.find_by_name(name):
        #     return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            print(item.json())
            db.items.insert_one(item.json())
        except:
            return {"message": "An error occurred inserting the item."}

        return item.json()

    @login_required
    def get(self, name):
        item = dumps(db.items.find_one({'name':name}))
        #item = ItemModel(item[])
        print('Item: ',item)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = db.items.find_one({'name':name})
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()
        # db.items.insert_one(item.json())
        return item.json()

    @jwt_required()
    def delete(self, name):
        item = db.items.find_one({'name':name})
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        result = dumps(db.items.find())
        print(result)
        return result
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
