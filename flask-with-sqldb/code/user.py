# This file will now interact with sqlite
import sqlite3
from flask_restful import Resource, reqparse

'''
This basically contains an object of the user 
in the form of a class for the usage in the security.py file
self is really there to interact with the class object
'''
class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # we are not using self, but we were using classname,
    # so to write more cleaner code, @classmethod is used
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE username=?"
        
        # the value always have to be a tuple
        # single value tuple has this format only (value,)
        result = cursor.execute(query, (username,))
        row = result.fetchone() # to fetch single result from result

        # positional args, auto get the row pos wise row[0], row[1], row[2]
        if row: user = cls(*row) # creating user object for more usage inside the method
        else: user = None

        # no connection.commit() is rquired since, we are not creating something to be saved
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE id=?"
        
        # the value always have to be a tuple
        # single value tuple has this format only (value,)
        result = cursor.execute(query, (_id,))
        row = result.fetchone() # to fetch single result from result

        # positional args, auto get the row pos wise row[0], row[1], row[2]
        if row: user = cls(*row) # creating user object for more usage inside the method
        else: user = None

        # no connection.commit() is rquired since, we are not creating something to be saved
        connection.close()
        return user

# This is to take care of creating the user
# And to get the url we have to do this
class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username is required")
    parser.add_argument('password', type=str, required=True, help="Password is required")
    
    def post(self):
        # data for passing into the execute query
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)" # NULL is for auto increment, it will suffice

        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
