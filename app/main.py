from fastapi import FastAPI
from app.predictor import predict
from app.schemas import Passenger

app = FastAPI(
    title="Titanic Survival Prediction API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Titanic Survival Prediction API is running"
    }


@app.post("/predict")
def predict_passenger(passenger: Passenger):

    prediction = predict(passenger.model_dump())

    return {
        "prediction": prediction
    }