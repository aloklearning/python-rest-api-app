# safe for comparision of string, in almost every python version
# from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'Bob', 'asdf')
]

# for mapping ease we create two dict comprehension
# which goes through the users list and return the data
# accordingly
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# This is for authentication purpose
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password: #safe_str_cmp(user.password, password)
        return user

# Another form of authenticating the user, 
# above and below function will be combined 
# to make the authentication secure
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

