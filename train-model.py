# train_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from math import sqrt
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load training data
train_df = pd.read_csv("data/train_products.csv")

# -----------------------
# Data Cleaning
# -----------------------
train_df['brand'] = train_df['brand'].fillna("Unknown")
train_df['category'] = train_df['category'].fillna("Unknown")
train_df['rating'] = train_df['rating'].fillna(train_df['rating'].mean())
train_df['reviews'] = train_df['reviews'].fillna(0)
train_df['quantity'] = train_df['quantity'].fillna(1)

# -----------------------
# Features and Target
# -----------------------
X = train_df[['brand', 'category', 'rating', 'reviews', 'quantity']].copy()
y = train_df['price']

# -----------------------
# Encode categorical features
# -----------------------
brand_encoder = LabelEncoder()
category_encoder = LabelEncoder()

X['brand'] = brand_encoder.fit_transform(X['brand'])
X['category'] = category_encoder.fit_transform(X['category'])

# Save encoders
joblib.dump(brand_encoder, 'models/brand_encoder.pkl')
joblib.dump(category_encoder, 'models/category_encoder.pkl')

# -----------------------
# Train-Test Split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------
# Train Random Forest
# -----------------------
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------
# Evaluate Model
# -----------------------
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
rmse = sqrt(mse)
print(f"Test MSE: {mse}")
print(f"Test RMSE: {rmse}")

# -----------------------
# Save Model
# -----------------------
joblib.dump(model, 'models/price_model.pkl')
print("Model and encoders saved successfully.")
