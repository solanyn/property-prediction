import catboost
import pickle
import boto3
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

# s3 = boto3.resource('s3')
# s3.Bucket('house-prediction-project').download_file('mlmodel/catboost.pkl', 'catboost.pkl')

model = pickle.load(open("catboost.pkl", "rb"))

class Property(BaseModel):
    suburb: str
    rooms: float 
    type: str
    postcode: str
    bathroom: float
    car: float 


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(property: Property):
    data = jsonable_encoder(property)

    result = model.predict(list(data.values()))
    if result:
        return {"statusCode": 200,
                "body": {"price": result}}
    else:
        return {"status": 404,
                "body": {"message": "data invalid"}}
