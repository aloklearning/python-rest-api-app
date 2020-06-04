from flask import Flask, request
#ignore import error cos we this is not defined in our global Python Library list
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required #JSON Web Token(JWT), allows us to decode, verify and generate JWT

from security import identity, authenticate

app = Flask(__name__)
# This is an entity to identify
# that the this is authenticated for encryption 
# identification. The secret key to be complicated when 
# an API is in production
app.secret_key = 'alok'
api = Api(app) # this will allow very easily add resources to it, for any sort of operation PUT, POST, DELETE

# jwt takes app, identity and autheticate
# combined to autheticate the user
# gives out the token, and which will be used
# as a decorator as @jwt_required(), which will not allow the user
# to pass perform the operation unless verified
jwt = JWT(app, authenticate, identity) # /auth is the url which JWT provides

items = []

# Every resources has to be a class, which will inherit the Resource
class Item(Resource):
    # this get method is from resource, which represents the GET method
    # jwt will autheticate and then get the data here
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # for the above, we are going to use filter(), 
        # which the same job, but in a more cleaner way
        # next() is use to return the first item returned
        # from multiple items, and None to avoid breaking 
        # of code when the list is empty
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404 #flask_restful way of sending the status code with the null data

    # this handles the post request, this is simplified using flask_restful only
    def post(self, name):
        # check if the item already exits 
        # to avoid duplicacy via name
        if next(filter(lambda x: x['name'] == name, items), None):
            # 400 Status code for Bad Request
            return {'message': "The item is already there with the name '{ }'.".format(name)}, 400
        
        # for JSON payload data get request.get_json()
        # silent=True or force=True are the params use to ignore the 
        # the Header Content-Type, if it is not being passed by the user 
        data = request.get_json() 
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #flask)restful way of sending status 201 which is for CREATED STATUS

    # This is for HTTP DELETE
    def delete(self, name):
        global items # This is to define that this is from the outer scope of this method
        # Returns the item exept the item which has the name passed using lambda
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'The item has been successfully deleted'}


class ItemList(Resource):
    def get(self):
        return {'items': items}

# This adds the Resource to the api Class 
# and route will be mentioned here only
# It helps in saving time for doing @app.route(URL)
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/item_name
api.add_resource(ItemList, '/items')

# debug=true gives out a detailed desc of 
# what went wrong in the server side
# auto refresh the server when making changes
app.run(port=5000, debug=True)

    
