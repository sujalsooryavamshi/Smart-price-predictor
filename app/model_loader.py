# app/model_loader.py
import joblib
import pandas as pd
import numpy as np

def load_model():
    model = joblib.load("models/price_model.pkl")
    brand_encoder = joblib.load("models/brand_encoder.pkl")
    category_encoder = joblib.load("models/category_encoder.pkl")
    return model, brand_encoder, category_encoder

def safe_encode(encoder, values):
    """
    Encode values using LabelEncoder, but replace unseen categories with a new index.
    """
    encoded = []
    known_classes = set(encoder.classes_)
    for val in values:
        if val in known_classes:
            encoded.append(int(encoder.transform([val])[0]))
        else:
            # If unseen, add to classes temporarily and assign new index
            encoded.append(len(encoder.classes_))
    return np.array(encoded)

def predict_price(model, brand_encoder, category_encoder, df):
    df = df.copy()
    df['brand'] = safe_encode(brand_encoder, df['brand'])
    df['category'] = safe_encode(category_encoder, df['category'])
    return model.predict(df)[0]
