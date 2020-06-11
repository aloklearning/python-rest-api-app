# Internal representation what an item does and 
# how it looks like
import sqlite3

class ItemModel(object):
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
        # now this is using sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone() # show one result only
        connection.close()

        if row: 
            return {'item': {'name': row[0], 'price': row[1]}}
    
    # classmethod responsible for inserting the data
    # No classmethod, since we are inserting 
    # the item itself, like Item() only
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()
    
    #class method which takes care of the update method
    # We cannot use Flask-RESTful update() since it doesn't
    # work for sqlite3
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()