# This is the model package, and the user is there, since
# it was not a Resource and more of a modal class
import sqlite3
from db import db

'''
db.Model will tell the Model, that is User,
to map with the database
'''
class UserModel(db.Model):
    # This tell the SQLAlchemy about the table name
    __tablename__ = 'users'

    # This will tell SQLAlchemy about columns
    # It will look directly into the tables with those
    # columns and then fetch the data and directly insert
    # the data into the Class Object as an args
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # _id is not required, since it is already a PRIMARY KEY,
    # hence, it will auto increment whenever we create some user
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # we are not using self, but we were using classname,
    # so to write more cleaner code, @classmethod is used
    @classmethod
    def find_by_username(cls, username):
        '''
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
        '''
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        '''
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
        '''
        return cls.query.filter_by(id=_id).first()