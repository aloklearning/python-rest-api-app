'''
This file just tests the sqlite with the simpler SQL queries
It it not at all connected to the API yet, which controls the 
operation of CRUD. To run this file, python test.py is the one
as usual, but what the catch is, always delete the data.db file
which it creates every time you run the file, to avoid data 
overlappings
'''

# This is an inbuilt python library for using SQL
import sqlite3

'''
This connects to the sqlite and stores the 
data in to the current directory with the 
name provided in the connect(). sqlite stores 
all the data in the same file, hence makes it a
slower than other Database tech
'''
connection = sqlite3.connect('data.db')

# Select the database, and move like a cursor
# For retreiving data from DB. For doing the 
# Query to store the results
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table) # this runs the query and perform the operation

# Storing the data into DB
user = (1, 'alok', 'asdf')
insert_query = "INSERT INTO users VALUES(?, ?, ?)" # (? -> id, ? -> username, ? -> password)
cursor.execute(insert_query, user) # cursor is smart enough to replace the user value in place of ?

# Insert many users
users = [
    (2, 'jose', 'asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users) # to insert the users from the list one by one

# Retreive data out from SQL DB file
select_query = "SELECT * FROM users"

# Select the data and printing out from the result
# (1, 'alok', 'asdf')
# (2, 'jose', 'asdf')
# (3, 'anne', 'xyz')
for row in connection.execute(select_query):
    print(row)

connection.commit() # to save all our changes to the file which we defined
connection.close() # to close the connection, not to recieve any more data or consuming resources

