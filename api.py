from distutils.log import debug
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TestApi(Resource):
    def get(self):
        return {'API version' : 0.1}

api.add_resource(TestApi, '/cors')

if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = '8080'
    )