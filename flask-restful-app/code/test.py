# Testing file to understand the complicated code better
from user import User

usrs = [
    User(1, 'Test1', 'abc'),
    User(2, 'Test2', 'def')
]

user_table = {usr.username: usr for usr in usrs}
userid_table = {usr.id: usr for usr in usrs}
#print(user_table.get('Test1'))
print(userid_table.get(1))