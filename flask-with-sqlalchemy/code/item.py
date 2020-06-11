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

        # using the classmethod to find the name
        # if found, store it into the variable
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
        
        # to check for the errors [If any]
        try: self.insert(item)
        except: return {"message": "An error occured while inserting the item"}, 500 # Internal Server Error

        return item, 201 #flask_restful way of sending status 201 which is for CREATED STATUS

    # classmethod responsible for inserting the data
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    # This is for HTTP DELETE
    def delete(self, name):
        # global items # This is to define that this is from the outer scope of this method
        # # Returns the item exept the item which has the name passed using lambda
        # items = list(filter(lambda x: x['name'] != name, items))

        # Using sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': f'{name} has been successfully deleted'}

    # This is for HTTP PUT i.e., CREATE/UPDATE
    def put(self, name):
        data = Item.parser.parse_args()

        # item = next(filter(lambda x: x['name'] == name, items), None)
        item = self.find_by_name(name) # searching for the item if exists or not
        updated_item = {'name': name, 'price': data['price']} # created for updated item data
        # if item is not found, then create a new item
        if item is None:
            #items.append(item) # old operation
            try:
                self.insert(updated_item) # this will be stored as a new item only, if item is none
            except:
                return {"message": "An error occured while inserting"}, 500
        else:
            #item.update(data) # updates the item with the data received, if found
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured while updating"}, 500
        return updated_item

    #class method which takes care of the update method
    # We cannot use Flask-RESTful update() since it doesn't
    # work for sqlite3
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):
        # return {'items': items} # old operation
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []

        # row is nothing but getting the 
        # dictionary from the list of the result 
        # obtained from the item list in the DB
        for row in result:
            # row comes in tuple format, so we have to extract the 
            # the value like row[0], row[1] to pass in dictionary
            # since items consists of array of dicts
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'items': items} # always in dictionary format