import catboost
import json
import pickle
import boto3
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

s3 = boto3.resource('s3')
s3.Bucket('house-prediction-project').download_file('catboost.pkl', 'mlmodel/catboost.pkl')
model = pickle.load(open("catboost.pkl", "rb"))

class Property(BaseModel):
    suburb: str
    rooms: int
    type: str
    postcode: str
    bathroom: int
    car: int
    landsize: float
    councilarea: str
    regionname: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(property: Property):
    with open("categorical.txt", "r") as f:
        categorical = f.read().split(",")
        f.close()

    with open("features.txt", "r") as f:
        features = f.read().split(",")
        f.close()

    data = jsonable_encoder(property)

    result = model.predict(list(data.values()))
    if result:
        return {200: {"value": result}}
    else:
        return {404: {"message": "data invalid"}}
