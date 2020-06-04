# safe for comparision of string, in almost every python version
# from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'Bob', 'asdf')
]

# for mapping ease we create two dict comprehension
# which goes through the users list and return the data
# accordingly
username_mapping = {u.username: u for u in users} # {'Bob': User list object}
userid_mapping = {u.id: u for u in users} # {1: User list object}

# This is for authentication purpose
def authenticate(username, password):
    user = username_mapping.get(username, None) # <user.User object at 0x10ed0eb10>
    if user and user.password == password: #safe_str_cmp(user.password, password)
        return user #Non-readable and it will be passed to the identity() parameter

# JWT takes the return data from the authenticate
# and pass it as payload in identity()
# which performs authenticate the user and gives out the token
# to be passed to the HTTP request as a header to authenticate
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

