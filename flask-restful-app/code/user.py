'''
This basically contains an object of the user 
in the form of a class for the usage in the security.py file
'''
class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password