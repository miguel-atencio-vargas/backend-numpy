from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers import *


PORT = 5000
DEBUG = False
app = Flask(__name__)
CORS(app)
api = Api(app)

#Router
api.add_resource(Employees, '/') # Route_1
api.add_resource(Suma, '/sumar', methods = ["POST"])

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
