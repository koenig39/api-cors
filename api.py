from distutils.log import debug
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)

# CORS(app)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

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