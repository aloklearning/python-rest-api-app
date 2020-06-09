import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

# Every resources has to be a class, which will inherit the Resource
class Item(Resource):
    # reqparser to be used for parsing the form data, also
    # if some other data was passed in the JSON form data
    # it ignores and takes only the specified param from the request
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='Price cannot be left empty!')
    
    # this get method is from resource, which represents the GET method
    # jwt will autheticate and then get the data here
    @jwt_required()
    def get(self, name):
        '''
        for item in items:
            if item['name'] == name:
                return item
        for the above, we are going to use filter(), 
        which the same job, but in a more cleaner way
        next() is use to return the first item returned
        from multiple items, and None to avoid breaking 
        of code when the list is empty
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404 #flask_restful way of sending the status code with the null data
        '''

        item = self.find_by_name(name)

        if item:
            return item
        return {'message': 'Item not found'}, 404

    
    @classmethod
    def find_by_name(cls, name):
        # now this is using sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone() # show one result only
        connection.close()

        if row: 
            return {'item': {'name': row[0], 'price': row[1]}}

    # this handles the post request, this is simplified using flask_restful only
    def post(self, name):
        # check if the item already exits 
        # to avoid duplicacy via name
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     # 400 Status code for Bad Request
        #     return {'message': "The item is already there with the name '{ }'.".format(name)}, 400

        # This is for sqlite check operation
        if self.find_by_name(name):
            # 400 Status code for Bad Request
            return {'message': "The item is already there with the name '{ }'.".format(name)}, 400
        
        '''
        for JSON payload data get request.get_json()
        silent=True or force=True are the params use to ignore the 
        the Header Content-Type, if it is not being passed by the user 
        '''
        data = Item.parser.parse_args() # data = {"price": 15.99}, data['price'] = 15.99

        item = {'name': name, 'price': data['price']}
        #items.append(item)
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201 #flask_restful way of sending status 201 which is for CREATED STATUS

    # This is for HTTP DELETE
    def delete(self, name):
        global items # This is to define that this is from the outer scope of this method
        # Returns the item exept the item which has the name passed using lambda
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'The item has been successfully deleted'}

    # This is for HTTP PUT i.e., CREATE/UPDATE
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        # if item is not found, then create a new item
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data) # updates the item with the data received, if found
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}