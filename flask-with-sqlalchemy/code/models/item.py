# Internal representation what an item does and 
# how it looks like
# import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #precision takes care of the number after decimal point

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # going to return a JSON repr
    # of the result
    def json(self):
        return {'name': self.name, 'price': self.price}

    # Classmethod Cos it is gonna return an 
    # object of type item model instead 
    # of a dictionary
    @classmethod
    def find_by_name(cls, name):
        '''
        # now this is using sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone() # show one result only
        connection.close()

        if row: 
            # return {'item': {'name': row[0], 'price': row[1]}}
            return cls(*row) # unpacking data, better way to return the object
        '''

        # Using SQLAlchemy
        # This is a one liner of all the code which we have written above using
        # Sqlite3, it gets the whole data, but we can get the data limiting using
        # filters like, first(). Query is coming from db.Model, since ItemModel is inheriting it
        return cls.query.filter_by(name=name).first() # SELECT * from __tablename__ WHERE name=name LIMIT 1
    
    # # classmethod responsible for inserting the data
    # # No classmethod, since we are inserting 
    # # the item itself, like Item() only
    # def insert(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO items VALUES (?, ?)"
    #     cursor.execute(query, (self.name, self.price))

    #     connection.commit()
    #     connection.close()
    
    # SQLAlchemy does both the things at the same time using 
    # a single operation, so insert and update is not required individually
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    #class method which takes care of the update method
    # We cannot use Flask-RESTful update() since it doesn't
    # work for sqlite3
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
