'''
This is a python app file which will help connecting with the flask
flask is a file name, starts with small f, having a class Flask,
starts with a capital one

jsonify on the other hand is a method, use to conver the data to JSON format
request is used to get the data from the user for post operation
render_template is helpful in rendering the HTML or any templates using Flask
'''
from flask import Flask, jsonify, request, render_template

# Creating an object app from the Flask class with a unique name(__name__)
app = Flask(__name__)

'''
Now we have made the application to be able to take the request
We are now going to make the project listen to a particular
request and give out a response to the request maker
Request forward slash, like https://google.com/, so this is a route

Mapping User[Request with route] -> Browser -> Server[FLASK] -> Data Response which we will do here
'''
# @app.route('/') # Python decorater route from Flask class followed by method
# def home():
#     # This response is the one which will be shown by the browser to the 
#     # the request maker
#     return 'Hello World!'

# Now we will look into more operations below
# POST - used to receieve data [AS A SERVER]
# GET - used to sedn data [AS A SERVER]

# Temp Database for the HTTP Operations
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# This is the home route, that is '/'
# This will be used to render the form which 
# we will be using to test our API
# templates folder name should be exactly like the one which is being 
# used, to make flask look for those templates inside the folder name specified
@app.route('/')
def home():
    return render_template('index.html')


# POST /store @require data: {name:}
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json() # this gets the json data user sends to us, and convert to a python dict
    new_store = {
        'name': request_data['name'],
        'items': []
    } 
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
# This is a flask wasy of getting inputs in GET. Ex: http://127.0.0.1:5000/store/some_name
@app.route('/store/<string:name>')
def getStore(name): # The name should match with the app route which is used as args
    # iterate over stores, if the store name matches return the data
    # an error message showing error
    for store in stores:
        if store['name'] == name: return jsonify(store)
    return jsonify({'message': f'No store with the name {name} found'})


# GET /stores
@app.route('/stores')
def getStores():
    # JSON only want one dictionary, which can contain list of data
    return jsonify({'stores': stores}) #convert the store variable into JSON


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createStoreItem(name):
    request_data = request.get_json()
    # to check whether the store exisits 
    # and then perform the operation
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
        return jsonify({'message': 'Could not perform operation due to store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getStoreItem(name):
    for store in stores:
        if store['name'] == name: return jsonify({'items': store['items']})
    return jsonify({'message': f'No store with the name {name} found'})


# This tells the app to run the app on a local server provided the port 
# in the run()
app.run(port=5000)


