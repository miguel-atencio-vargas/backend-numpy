from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers import *


PORT = 5000
DEBUG = False
app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Employees, '/')
api.add_resource(Operacion, '/operacion', methods = ["POST"])
api.add_resource(Unimatriz, '/unimatriz', methods = ["POST"])
api.add_resource(Random, '/random', methods = ["POST"])

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
