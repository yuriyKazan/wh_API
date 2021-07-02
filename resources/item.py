from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='The field can\'t be empty')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Each item has to have store id')
    parser.add_argument('quantity',
                        type=int,
                        required=False,
                        help='Each item has to have store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except Exception as error:
            print(error)
            return {'message': 'An error occurred inserting item'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        else:
            return {'message': 'The item was not find'}
        return {'message': 'The item deleted'}, 202

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            if data['quantity']:
                item.quantity = data['quantity']
            else:
                item.quantity = 0
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
