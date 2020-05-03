from flask import Flask
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class PredictPropertyPrice(Resource):
    def get(self):
        return {"hello": "world"}

api.add_resource(PredictPropertyPrice, "/")

if __name__ == "__main__":
    application.run(debug=True)
