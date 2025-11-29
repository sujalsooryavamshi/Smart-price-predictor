# app/schemas.py
from pydantic import BaseModel

class Product(BaseModel):
    brand: str
    category: str
    rating: float
    reviews: int
    quantity: float

class PredictionResponse(BaseModel):
    predicted_price: float
