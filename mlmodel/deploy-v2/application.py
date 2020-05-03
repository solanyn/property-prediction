import catboost
import pickle
from flask import Flask, jsonify, request
from flask_restful import Resource, Api 

application = Flask(__name__)
api = Api(application)

model = pickle.load(open("catboost.pkl", "rb"))


class PredictPropertyPrice(Resource):
    @staticmethod
    def post(self):
        json = request.get_json()

        result = model.predict(list(json.values()))
        return jsonify({
            "price": result
        })

api.add_resource(PredictPropertyPrice, "/")

