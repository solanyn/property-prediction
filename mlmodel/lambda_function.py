import catboost
import json
import pickle
import boto3

s3 = boto3.resource('s3')
s3.Bucket('house-prediction-project').download_file('catboost.pkl', 'catboost.pkl')
model = pickle.load(open("catboost.pkl", "rb"))

def predict(event, context):
    result = model.predict(list(event.values()))
    if result:
        return {200: {"price": result}}
    else:
        return {404: {"message": "data invalid"}}
