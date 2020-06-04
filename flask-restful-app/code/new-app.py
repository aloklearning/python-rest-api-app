from flask import Flask
#ignore import error cos we this is not defined in our global Python Library list
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app) # this will allow very easily add resources to it, for any sort of operation PUT, POST, DELETE

# Every resources has to be a class, which will inherit the Resource
class Student(Resource):
    # this get method is from resource, which represents the GET method
    def get(self, name):
        return {'student': name}

# This adds the Resource to the api Class 
# and route will be mentioned here only
# It helps in saving time for doing @app.route(URL)
api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1:5000/student/student_name

app.run(port=5000)

    
