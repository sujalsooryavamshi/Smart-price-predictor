# app/main.py
from fastapi import FastAPI
from app.model_loader import load_model, predict_price
from app.schemas import Product, PredictionResponse
import pandas as pd

app = FastAPI(title="Smart Price Predictor")

# Load model and encoders
model, brand_encoder, category_encoder = load_model()

@app.post("/predict", response_model=PredictionResponse)
def predict(product: Product):
    data = pd.DataFrame([product.dict()])
    price = predict_price(model, brand_encoder, category_encoder, data)
    return {"predicted_price": float(price)}
