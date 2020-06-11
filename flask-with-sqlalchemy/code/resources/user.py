# This file will now interact with sqlite
import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse

# This is to take care of creating the user
# And to get the url we have to do this
class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username is required")
    parser.add_argument('password', type=str, required=True, help="Password is required")
    
    def post(self):
        # data for passing into the execute query
        data = UserRegister.parser.parse_args()

        # checking for any duplicate user exists
        # in DB already
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)" # NULL is for auto increment, it will suffice

        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
