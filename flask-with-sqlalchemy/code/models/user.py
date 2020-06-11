# This is the model package, and the user is there, since
# it was not a Resource and more of a modal class
import sqlite3

'''
This basically contains an object of the user 
in the form of a class for the usage in the security.py file
self is really there to interact with the class object
'''
class UserModel(object):
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