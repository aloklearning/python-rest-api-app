'''
This is responsible for creating the user in the DB
It is now inside the code folder to avoid any confusion
for running the test.py in parent folder, and creating the
data.db file there
'''
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# For creating the auto increment integer, we have 
# INTEGER and not int in SQL query
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # real is for real numbers
cursor.execute(create_table)

connection.commit()
connection.close()

