from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Goes into the items which checks the Store id, 
    # and finds the relationship, checks for MANY TO ONE Relationship
    # the store can contain many items, hence we get the array or list
    # of items here
    items = db.relationship('ItemModel') 

    def __init__(self, name):
        self.name = name

    # going to return a JSON repr
    # of the result
    def json(self):
        return {'name': self.name, 'items': [item.json for item in self.items]}

    # Classmethod Cos it is gonna return an 
    # object of type item model instead 
    # of a dictionary
    @classmethod
    def find_by_name(cls, name):
        # Using SQLAlchemy
        # This is a one liner of all the code which we have written above using
        # Sqlite3, it gets the whole data, but we can get the data limiting using
        # filters like, first(). Query is coming from db.Model, since ItemModel is inheriting it
        return cls.query.filter_by(name=name).first() # SELECT * from __tablename__ WHERE name=name LIMIT 1
    
    # SQLAlchemy does both the things at the same time using 
    # a single operation, so insert and update is not required individually
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
