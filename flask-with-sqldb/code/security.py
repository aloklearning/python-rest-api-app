# safe for comparision of string, in almost every python version
# from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'Bob', 'asdf')
]

# Retrieve the user by username
# Retrieve the user by user_id
username_mapping = {u.username: u for u in users} # {'Bob': User list object}
userid_mapping = {u.id: u for u in users} # {1: User list object}

# This is for authentication purpose
#Generates JWT Token after performing this action
def authenticate(username, password):
    user = username_mapping.get(username, None) # <user.User object at 0x10ed0eb10>
    if user and user.password == password: #safe_str_cmp(user.password, password)
        return user # Becomes identiy for the JWT Token for authentication

'''
Now this identity is used when we perform @jwt_required()
How -> The token which will be passed will be passed to 
the identity() payload With the JWT token as a payload, 
checks the user is there and gets the correct user_id that 
the token repr. If there, it returns the identity, that 
is the user object which we returned in authentication()
That means that was a valid JWT token passsed by the user
'''
def identity(payload):
    user_id = payload['identity'] # identity is the user_id
    return userid_mapping.get(user_id, None)

