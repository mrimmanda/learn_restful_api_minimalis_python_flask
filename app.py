#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS 

# Inisiasi object flask
app = Flask(__name__)

# Inisiasi object flask_restful
api = Api(app)

# Inisiasi object flask_cors
CORS(app) 

# Inisiasi empty variable dictionary type 
# Global Variables
identitas = {}

# Make Class Resource
class ExampleResource(Resource):
    # GET / POST Method
    # GET METHOD
    def get(self):
        # response = {
        #     "message":"Immanda learn Python Restful API"
        # }
        return identitas
    
    # POST METHOD
    def post(self):
        name = request.form['name']
        age = request.form['age']
        identitas["name"] = name
        identitas["age"] = age
        response = {
            "message":"Data Succesfull Insert"
        }
        return response

# Resource Setup
api.add_resource(ExampleResource, "/api", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True, port=5005)
    