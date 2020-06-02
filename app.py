'''
This is a python app file which will help connecting with the flask
flask is a file name, starts with small f, having a class Flask,
starts with a capital one
'''
from flask import Flask

# Creating an object app from the Flask class with a unique name(__name__)
app = Flask(__name__)

'''
Now we have made the application to be able to take the request
We are now going to make the project listen to a particular
request and give out a response to the request maker
Request forward slash, like https://google.com/, so this is a route

Mapping User[Request with route] -> Browser -> Server[FLASK] -> Data Response which we will do here
'''
@app.route('/') # Python decorater route from Flask class followed by method
def home():
    # This response is the one which will be shown by the browser to the 
    # the request maker
    return 'Hello World!'

# This tells the app to run the app on a local server provided the port 
# in the run()
app.run(port=5000)


