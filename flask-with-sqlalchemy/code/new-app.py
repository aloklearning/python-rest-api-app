#from flask import Flask, request
from flask import Flask
#ignore import error cos we this is not defined in our global Python Library list
#from flask_restful import Resource, Api, reqparse
from flask_restful import Api
#from flask_jwt import JWT, jwt_required #JSON Web Token(JWT), allows us to decode, verify and generate JWT
from flask_jwt import JWT

from security import identity, authenticate
from resources.user import UserRegister
from resources.item import ItemList, Item

app = Flask(__name__)
# Turning the Flask Sqlalchemy track off explicitely, since 
# SQLAlchemy has it's own Track Modification. By Track 
# Modification we mean that Whatever operation we do
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# This is an entity to identify
# that the this is authenticated for encryption 
# identification. The secret key to be complicated when 
# an API is in production
app.secret_key = 'alok'
api = Api(app) # this will allow very easily add resources to it, for any sort of operation PUT, POST, DELETE

'''
jwt takes app, identity and autheticate
combined to autheticate the user
gives out the token, and which will be used
as a decorator as @jwt_required(), which will not allow the user
to pass perform the operation unless verified
'''

'''
It has to be there before we initialise the jwt 

==> To change the by default url of /auth to something else, 
like /login, do this => app.config['JWT_AUTH_URL_RULE'] = '/login'

==> config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

==> config JWT auth key name to be 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
'''
jwt = JWT(app, authenticate, identity) # /auth is the url which JWT provides

# items = []

# This adds the Resource to the api Class 
# and route will be mentioned here only
# It helps in saving time for doing @app.route(URL)
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/item_name
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register') # this is coming from the user.py file

# This ensures that the app file is created
# in the same file, and not imported from 
# some other file. Best Practise
if __name__ == "__main__":
    # circular import
    from db import db
    db.init_app(app)
    # debug=true gives out a detailed desc of 
    # what went wrong in the server side
    # auto refresh the server when making changes
    app.run(port=5000, debug=True)

    
